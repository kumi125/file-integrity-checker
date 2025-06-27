**🛡️ File Guardian – File Integrity Checker**
A GUI-based file integrity checker built with Python.
It helps detect file tampering, deletion, and suspicious additions in monitored folders using SHA256 hashing.

**💡 What It Does**
Scans all files in a selected folder

Calculates SHA256 hashes for integrity

**Flags any files that are:**

✅ Modified

❌ Deleted

🆕 Newly added

**Helps detect tampering, malware, or accidental changes**

GUI-based for ease of use (built with Tkinter)

**🔧 How to Run**
⚠️ Requires Python 3.x

Clone the Repo

bash
Copy
Edit
git clone https://github.com/kumi125/file-integrity-checker.git
cd file-guardian
Install dependencies (standard library only, no pip needed)

Run the app

bash
Copy
Edit
python file_guardian.py


**🚨 Features**
📁 Select any folder to monitor

🧠 SHA256 hashing of all files

🕵️ Detect modified, deleted, or new files

🪪 Simple and clean dark-themed GUI

📤 Option to export report (coming soon)

🔄 Re-scan and compare feature (coming next!)

**📂 Folder Structure**
bash
Copy
Edit
file-guardian/
├── file_guardian.py       # Main app
├── README.md              # You're here!
├── screenshot.png         # GUI preview (optional)
└── .gitignore             # Python ignored files
📜 License
MIT License — feel free to use, modify, and share.
Created with ❤️ by [KUMAIL HUSSAIN]

