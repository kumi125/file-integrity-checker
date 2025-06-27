import tkinter as tk
from tkinter import filedialog, messagebox
import os
import hashlib

class FileGuardianApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛡️ File Guardian – Integrity Checker")
        self.root.geometry("600x300")
        self.root.configure(bg="#121212")

        self.folder_path = tk.StringVar()

        tk.Label(root, text="File Integrity Checker", font=("Helvetica", 18, "bold"),
                 fg="#00FFCC", bg="#121212").pack(pady=20)

        self.select_btn = tk.Button(root, text="📁 Select Folder", command=self.select_folder,
                                    bg="#00FFCC", fg="black", font=("Helvetica", 12, "bold"))
        self.select_btn.pack(pady=10)

        self.path_label = tk.Label(root, textvariable=self.folder_path, fg="white", bg="#121212")
        self.path_label.pack(pady=5)

        self.start_btn = tk.Button(root, text="🚀 Start Scan", state=tk.DISABLED,
                                   command=self.start_scan,
                                   bg="#00FFCC", fg="black", font=("Helvetica", 12, "bold"))
        self.start_btn.pack(pady=20)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)
            self.start_btn.config(state=tk.NORMAL)

    def start_scan(self):
        folder = self.folder_path.get()
        hash_results = self.hash_folder(folder)
        result_message = f"Scanned {len(hash_results)} files.\n\n"
        result_message += "\n".join([f"{os.path.basename(f)}: {h[:10]}..." for f, h in hash_results.items()][:10])
        result_message += "\n\n(Only showing first 10 files)"

        messagebox.showinfo("Scan Complete", result_message)

    def hash_folder(self, folder):
        file_hashes = {}
        for dirpath, _, filenames in os.walk(folder):
            for file in filenames:
                filepath = os.path.join(dirpath, file)
                try:
                    with open(filepath, "rb") as f:
                        file_data = f.read()
                        sha256 = hashlib.sha256(file_data).hexdigest()
                        file_hashes[filepath] = sha256
                except Exception as e:
                    print(f"Could not read {filepath}: {e}")
        return file_hashes

if __name__ == "__main__":
    root = tk.Tk()
    app = FileGuardianApp(root)
    root.mainloop()
