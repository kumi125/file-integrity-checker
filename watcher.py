import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from sign_baseline import sign_file
from verify_baseline import verify_file
import hashlib
import json
import threading

BASELINE_FILE = "baseline.json"
IGNORED_FILES = ["baseline.json.sig"]
IGNORED_DIRS = ["venv"]


def compute_hash(file_path, chunk_size=2**20):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, baseline):
        self.baseline = baseline

    def _is_ignored(self, event):
        return (
            event.is_directory
            or any(d in event.src_path for d in IGNORED_DIRS)
            or any(f in event.src_path for f in IGNORED_FILES)
        )

    def _check_file(self, file_path):
        file_path = str(file_path)
        if Path(file_path).exists():
            new_hash = compute_hash(file_path)
            old_hash = self.baseline.get(file_path)
            if old_hash is None:
                print(f"➕ New file detected: {file_path}")
                self.baseline[file_path] = new_hash
                sign_file(BASELINE_FILE)
            elif new_hash != old_hash:
                print(f"⚠️ Modified: {file_path}")
                self.baseline[file_path] = new_hash
                sign_file(BASELINE_FILE)
        else:
            if file_path in self.baseline:
                print(f"❌ Deleted: {file_path}")
                del self.baseline[file_path]
                sign_file(BASELINE_FILE)

    def on_created(self, event):
        if not self._is_ignored(event):
            self._check_file(event.src_path)

    def on_modified(self, event):
        if not self._is_ignored(event):
            self._check_file(event.src_path)

    def on_deleted(self, event):
        if not self._is_ignored(event):
            self._check_file(event.src_path)


def start_watcher():
    if not verify_file(BASELINE_FILE):
        print("❌ Baseline verification failed! Exiting.")
        return

    with open(BASELINE_FILE) as f:
        baseline_data = json.load(f)

    path_to_monitor = str(Path(".").resolve())
    event_handler = FileChangeHandler(baseline_data)
    observer = Observer()
    observer.schedule(event_handler, path_to_monitor, recursive=True)
    observer.daemon = True  # runs in the background
    observer.start()
    print(f"👀 Watching for changes in {path_to_monitor} (daemon mode) ...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    # Save updated baseline on exit
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline_data, f, indent=4)
    sign_file(BASELINE_FILE)


if __name__ == "__main__":
    # Run watcher in a separate thread so terminal stays usable
    watcher_thread = threading.Thread(target=start_watcher, daemon=True)
    watcher_thread.start()

    print("Watcher is running in background. You can use the terminal freely.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting watcher...")
