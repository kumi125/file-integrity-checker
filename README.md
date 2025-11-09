
**🛡️ File Guardian — Advanced File Integrity Checker**

A professional cybersecurity tool built in Python, designed to detect unauthorized file modifications, deletions, and suspicious additions using cryptographic hashing and digital signatures.

It’s built for penetration testers, blue teams, and cybersecurity learners who want to understand file integrity monitoring like a real-world FIM/IDS system.

💡 What It Does

🧩 Scans and signs all files in a monitored directory using SHA-256

🔏 Digitally signs the baseline for trusted verification

🕵️ Detects and reports:

✅ Modified files

❌ Deleted files

🆕 Newly added files

🔐 Verifies cryptographic signature before monitoring begins
to fix merge conflict
1️⃣ Open the conflicting file


👁️ Live Watch Mode – continuously monitors your folder in real-time

🌀 Daemon Mode – runs silently in background without blocking terminal

⚙️ Tech Features

Built in Python 3

Uses cryptography library for signing & verification

Uses watchdog for real-time folder monitoring

Cross-platform (Linux / Windows / macOS)

Lightweight – no heavy dependencies

🧠 Modules
File	Purpose
generate_baseline.py	Scans directory and generates baseline.json
sign_baseline.py	Creates digital signature for baseline
verify_baseline.py	Verifies signature integrity
watcher.py	Monitors folder changes (supports daemon mode)

# 🛡️ File Guardian — Advanced File Integrity Checker

A **professional cybersecurity tool** built in **Python**, designed to **detect unauthorized file modifications, deletions, and suspicious additions** using **cryptographic hashing and digital signatures**.

It’s built for **penetration testers, blue teams, and cybersecurity learners** who want to understand **file integrity monitoring** like a real-world FIM/IDS system.

---

## 💡 What It Does

- 🧩 **Scans and signs** all files in a monitored directory using **SHA-256**  
- 🔏 **Digitally signs** the baseline for trusted verification  
- 🕵️ **Detects and reports**:
  - ✅ Modified files  
  - ❌ Deleted files  
  - 🆕 Newly added files  
- 🔐 **Verifies cryptographic signature** before monitoring begins  
- 👁️ **Live Watch Mode** – continuously monitors your folder in real-time  
- 🌀 **Daemon Mode** – runs silently in background without blocking terminal  

---

## ⚙️ Tech Features

- Built in **Python 3**
- Uses **cryptography** library for signing & verification  
- Uses **watchdog** for real-time folder monitoring  
- **Cross-platform (Linux / Windows / macOS)**  
- Lightweight – no heavy dependencies  

---

## 🧠 Modules

| File | Purpose |
|------|----------|
| `generate_baseline.py` | Scans directory and generates baseline.json |
| `sign_baseline.py` | Creates digital signature for baseline |
| `verify_baseline.py` | Verifies signature integrity |
| `watcher.py` | Monitors folder changes (supports daemon mode) |

---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/kumi125/file-integrity-checker.git
cd file-integrity-checker

2️⃣ Setup virtual environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3️⃣ Generate and sign baseline

python3 generate_baseline.py
python3 sign_baseline.py

4️⃣ Start monitoring

python3 watcher.py

✅ Your system is now under file integrity watch.
All events (created, modified, deleted) will appear instantly.
🌀 Run in background (daemon mode)

python3 watcher.py --daemon

🧰 Future Improvements

    🧾 Export change reports to JSON or CSV

    📡 Email or Telegram alerts for tampering

    🌐 Web dashboard for remote monitoring

    🧠 Machine learning anomaly detection (planned upgrade)

📂 Folder Structure

file-integrity-checker/
├── generate_baseline.py
├── sign_baseline.py
├── verify_baseline.py
├── watcher.py
├── baseline.json
├── README.md
└── requirements.txt

📜 License

MIT License — free to use, modify, and share.
Created with ❤️ by Kumail Hussain

