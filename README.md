🛡️ File Guardian — Advanced File Integrity Checker

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
