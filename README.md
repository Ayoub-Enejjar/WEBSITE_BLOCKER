# WEBSITE_BLOCKER
A simple Python script to block websites (domains) and direct IP addresses on Windows using the system `hosts` file and Windows Firewall.

# 🔒 Website and IP Blocker (Windows Only)

## ⚠️ Requirements

- Windows OS
- Run as Administrator
- Python 3.x

## 🚀 How It Works

- Blocks **websites/domains** via the `hosts` file (maps to `127.0.0.1`)
- Blocks **IP addresses** via Windows Firewall using `netsh`

## 📦 Features

- ✅ Block and unblock websites
- ✅ Block and unblock IP addresses
- ✅ Simple command-line usage

## 📂 Usage

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/website-blocker.git
cd website-blocker

✅Run the script as Administrator: 

📂To block:
python block_sites.py block

📂To unblock:
python block_sites.py unblock