# WEBSITE_BLOCKER
A simple Python script to block websites (domains) and direct IP addresses on Windows using the system `hosts` file and Windows Firewall.

# 🔒 Website and IP Blocker (Windows Only)

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

⚠️ Requirements :

✅Windows OS
✅Run as Administrator
✅Python 3.x

📦 1. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

📦 2. Install dependencies
pip install -r requirements.txt

📦 3. Run the Flask app
python app.py
