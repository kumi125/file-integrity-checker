import argparse
from sign_baseline import sign_file
from verify_baseline import verify_file
from watcher import FileChangeHandler, Observer
from pathlib import Path
import time
import json
import hashlib

BASELINE_FILE = "baseline.json"

def compute_hash(file_path, chunk_size=2**20):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def init_baseline():
    baseline = {}
    for file in Path(".").rglob("*"):
        if file.is_file() and file.name not in [BASELINE_FILE, "baseline.json.sig"]:
            baseline[str(file)] = compute_hash(file)
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)
    sign_file(BASELINE_FILE)
    print(f"✅ Baseline created and signed: {BASELINE_FILE}")

def scan_baseline():
    if not verify_file(BASELINE_FILE):
        print("❌ Baseline verification failed!")
        return
    with open(BASELINE_FILE) as f:
        baseline = json.load(f)
    for file_path, old_hash in baseline.items():
        if Path(file_path).exists():
            new_hash = compute_hash(file_path)
            if new_hash != old_hash:
                print(f"⚠️ Modified: {file_path}")
        else:
            print(f"❌ Deleted: {file_path}")

def watch():
    from watchdog.observers import Observer
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, str(Path(".").resolve()), recursive=True)
    observer.start()
    print("👀 Watching for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def export_report():
    with open(BASELINE_FILE) as f:
        baseline = json.load(f)
    with open("baseline_report.json", "w") as f:
        json.dump(baseline, f, indent=4)
    print("📄 Baseline exported: baseline_report.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Integrity Checker CLI")
    parser.add_argument("command", choices=["init", "scan", "watch", "export"])
    args = parser.parse_args()

    if args.command == "init":
        init_baseline()
    elif args.command == "scan":
        scan_baseline()
    elif args.command == "watch":
        watch()
    elif args.command == "export":
        export_report()
