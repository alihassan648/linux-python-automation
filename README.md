
# Linux Log Analyzer CLI

## 🚨 Problem Statement

Linux servers generate large log files daily (syslog, auth.log, application logs).  
Manually scanning logs to detect errors, warnings, or security events is inefficient and time-consuming.

This tool automates Linux log analysis by parsing log files, extracting critical entries, and generating structured summaries for faster troubleshooting.

---

## 🚀 Features

- Parses Linux system log files
- Extracts ERROR, WARNING, and CRITICAL entries
- Generates structured summary output
- CLI-based automation tool
- Modular project architecture
- Logging system integration
- Editable installation support

---

## 🧠 Use Cases

- Server troubleshooting automation
- Daily cron-based log monitoring
- VPS monitoring
- Freelance Linux administration tasks
- Error pattern detection

---

## 🏗 Project Architecture

```
src/
 └── log_analyzer_pkg/
     ├── cli.py
     ├── parser.py
     ├── report.py
     ├── logger.py
     └── utils.py
```

---

## 📦 Installation

Clone repository:

```bash
git clone https://github.com/yourusername/linux-log-analyzer-cli.git
cd linux-log-analyzer-cli
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install package:

```bash
pip install -e .
```

---

## 💻 Usage

Analyze a log file:

```bash
loganalyzer scan --file /var/log/syslog
```

Example Output:

```
Scan Summary
------------
Total Lines Processed: 12500
Errors Found: 15
Warnings Found: 32
Critical Events: 3
```

---

## 🔄 Automation Example (Cron)

Run daily at 1 AM:

```bash
0 1 * * * /usr/local/bin/loganalyzer scan --file /var/log/syslog
```

---

## 🛡 Why This Matters

This project demonstrates:

- Linux file handling
- Log parsing logic
- CLI application design
- DevOps-style automation principles
- Production-ready Python packaging

---

## 📜 License

MIT License
