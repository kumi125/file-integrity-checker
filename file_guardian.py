import tkinter as tk
from tkinter import filedialog, messagebox
import os
import hashlib
import threading
import time

class FileGuardianApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛡️ File Guardian – Integrity Checker")
        self.root.geometry("700x450")
        self.root.configure(bg="#121212")

        self.folder_path = tk.StringVar()
        self.hashes = {}
        self.file_statuses = {}
        self.monitoring = False
        self.start_time = None

        # Title
        tk.Label(root, text="File Integrity Checker", font=("Helvetica", 18, "bold"),
                 fg="#00FFCC", bg="#121212").pack(pady=20)

        # Folder selection
        self.select_btn = tk.Button(root, text="📁 Select Folder", command=self.select_folder,
                                    bg="#00FFCC", fg="black", font=("Helvetica", 12, "bold"))
        self.select_btn.pack(pady=5)

        self.path_label = tk.Label(root, textvariable=self.folder_path, fg="white", bg="#121212")
        self.path_label.pack()

        # Start monitoring
        self.start_btn = tk.Button(root, text="🚀 Start Monitoring", command=self.start_monitoring,
                                   state=tk.DISABLED, bg="#00FFCC", fg="black", font=("Helvetica", 12, "bold"))
        self.start_btn.pack(pady=10)

        # Stop monitoring
        self.stop_btn = tk.Button(root, text="🛑 Stop Monitoring", command=self.stop_monitoring,
                                   state=tk.DISABLED, bg="red", fg="white", font=("Helvetica", 12, "bold"))
        self.stop_btn.pack(pady=5)

        # Export hash report
        self.export_btn = tk.Button(root, text="📄 Export Hash Report", command=self.export_hashes,
                                   state=tk.DISABLED, bg="#5555FF", fg="white", font=("Helvetica", 12))
        self.export_btn.pack(pady=5)

        # Status label
        self.status_label = tk.Label(root, text="Status: Waiting to start...", fg="white", bg="#121212", wraplength=600)
        self.status_label.pack(pady=10)

        # Timer label
        self.timer_label = tk.Label(root, text="", fg="yellow", bg="#121212", font=("Courier", 12))
        self.timer_label.pack(pady=5)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(f"Selected Folder: {folder}")
            self.start_btn.config(state=tk.NORMAL)

    def start_monitoring(self):
        folder = self.folder_path.get().replace("Selected Folder: ", "")
        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Invalid folder path!")
            return

        self.monitoring = True
        self.start_time = time.time()
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.export_btn.config(state=tk.DISABLED)

        self.status_label.config(text="Monitoring started...")
        self.hashes = self.get_hashes(folder)
        self.file_statuses = {f: "Unchanged" for f in self.hashes}
        threading.Thread(target=self.monitor_folder, args=(folder,), daemon=True).start()
        threading.Thread(target=self.update_timer, daemon=True).start()

    def stop_monitoring(self):
        self.monitoring = False
        self.stop_btn.config(state=tk.DISABLED)
        self.start_btn.config(state=tk.NORMAL)
        self.export_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Monitoring stopped.")

    def get_hashes(self, folder):
        hashes = {}
        for root_dir, _, files in os.walk(folder):
            for name in files:
                file_path = os.path.join(root_dir, name)
                try:
                    with open(file_path, "rb") as f:
                        content = f.read()
                        file_hash = hashlib.sha256(content).hexdigest()
                        hashes[file_path] = file_hash
                except:
                    continue
        return hashes

    def monitor_folder(self, folder):
        while self.monitoring:
            time.sleep(2)
            current_hashes = self.get_hashes(folder)
            new_events = []

            # Detect new/modified files
            for file, h in current_hashes.items():
                if file not in self.hashes:
                    self.file_statuses[file] = "New"
                    new_events.append(f"🆕 New file detected: {file}")
                elif self.hashes[file] != h:
                    self.file_statuses[file] = "Modified"
                    new_events.append(f"✏️ File modified: {file}")
                else:
                    self.file_statuses[file] = "Unchanged"

            # Detect deleted files
            for file in self.hashes:
                if file not in current_hashes:
                    self.file_statuses[file] = "Deleted"
                    new_events.append(f"❌ File deleted: {file}")

            # Update UI and logs
            if new_events:
                self.status_label.config(text="\n".join(new_events[-3:]))  # Show last 3 events
                with open("log.txt", "a") as log:
                    for event in new_events:
                        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                        log.write(f"[{timestamp}] {event}\n")

            self.hashes = current_hashes.copy()

    def export_hashes(self):
        try:
            with open("hash_report.txt", "w") as f:
                for file, h in self.hashes.items():
                    f.write(f"{file} : {h}\n")
            messagebox.showinfo("Exported", "Hash report saved as hash_report.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export hash report.\n{e}")

    def update_timer(self):
        while self.monitoring:
            elapsed = int(time.time() - self.start_time)
            mins, secs = divmod(elapsed, 60)
            self.timer_label.config(text=f"⏱️ Monitoring Time: {mins:02d}:{secs:02d}")
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileGuardianApp(root)
    root.mainloop()
