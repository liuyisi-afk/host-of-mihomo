# convert_hosts.py
import requests, yaml

URL = "https://raw.githubusercontent.com/lingeringsound/10007_auto/Feature/all"

def fetch_hosts(url):
    print(f"Fetching hosts from {url}")
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.text

def parse_hosts(text):
    hosts_dict = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        ip = parts[0]
        domains = parts[1:]
        for d in domains:
            hosts_dict[d] = ip
    return hosts_dict

def main():
    text = fetch_hosts(URL)
    hosts_dict = parse_hosts(text)
    out = {"hosts": hosts_dict}

    with open("mihomo_hosts.yaml", "w", encoding="utf8") as f:
        yaml.safe_dump(out, f, sort_keys=False, allow_unicode=True)
    print("✅ 已生成 mihomo_hosts.yaml")

if __name__ == "__main__":
    main()
