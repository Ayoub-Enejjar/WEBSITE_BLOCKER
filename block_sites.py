import os
import json

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def block_domains():
    config = load_config()
    domains = config["domains"]
    with open(HOSTS_PATH, "r+") as file:
        content = file.read()
        for domain in domains:
            if domain not in content:
                file.write(f"{REDIRECT_IP} {domain}\n")

def unblock_domains():
    config = load_config()
    domains = config["domains"]
    with open(HOSTS_PATH, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(domain in line for domain in domains):
                file.write(line)
        file.truncate()

def block_ips():
    config = load_config()
    for ip in config["ips"]:
        os.system(f'netsh advfirewall firewall add rule name="Block {ip}" dir=out action=block remoteip={ip}')

def unblock_ips():
    config = load_config()
    for ip in config["ips"]:
        os.system(f'netsh advfirewall firewall delete rule name="Block {ip}"')
