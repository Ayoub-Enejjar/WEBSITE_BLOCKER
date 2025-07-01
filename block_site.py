import os
import sys

# ======= Configuration =======
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"

blocked_domains = [
    "www.facebook.com", "facebook.com",
    "www.youtube.com", "youtube.com"
]

blocked_ips = [
    "167.71.43.43",
    "142.250.190.14"  # Example IP (Google/YouTube)
]
# =============================

def block_domains():
    with open(hosts_path, "r+") as file:
        content = file.read()
        for domain in blocked_domains:
            if domain not in content:
                file.write(f"{redirect_ip} {domain}\n")
    print("✅ Domains blocked via hosts file.")

def unblock_domains():
    with open(hosts_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(domain in line for domain in blocked_domains):
                file.write(line)
        file.truncate()
    print("✅ Domains unblocked.")

def block_ips():
    for ip in blocked_ips:
        os.system(f'netsh advfirewall firewall add rule name="Block {ip}" dir=out action=block remoteip={ip}')
    print("✅ IPs blocked via Windows Firewall.")

def unblock_ips():
    for ip in blocked_ips:
        os.system(f'netsh advfirewall firewall delete rule name="Block {ip}"')
    print("✅ IPs unblocked.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python block_sites.py [block|unblock]")
    elif sys.argv[1] == "block":
        block_domains()
        block_ips()
    elif sys.argv[1] == "unblock":
        unblock_domains()
        unblock_ips()
    else:
        print("Invalid option. Use 'block' or 'unblock'.")
