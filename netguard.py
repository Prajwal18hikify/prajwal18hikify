import ipaddress
import socket
import datetime
import requests
import argparse

def header(title):
    print(f"\n{'='*45}")
    print(f"  {title}")
    print(f"  {datetime.datetime.now()}")

def subnet_info(cidr):
    print(f"\n---- SUBNET : {cidr}")
    net = ipaddress.ip_network(cidr, strict=False)
    hosts = list(net.hosts())
    print(f"Network  :  {net.network_address}")
    print(f"Mask  :  {net.netmask}")
    print(f"Broadcast  :  {net.broadcast_address}")
    print(f"First IP  :  {hosts[0]}")
    print(f"Last IP   :  {hosts[-1]} ")
    print(f"Total   :  {net.num_addresses-2} hosts")

DANGEROUS  = {
    22:"SSH", 23:"Telnet",
    3306:"MySQL", 5432:"PostgreSQL",
    6379:"Redis", 3389:"RDP"
}

def scan_ports(target):
    print(f"\n--- PORT SCAN: {target}")
    ports = {22:"SSH", 80:"HTTP",
            443:"HTTPS", 3306:"MySQL",
            5432:"PostgreSQL", 8080:"HTTP-Alt"}
    critical = 0
    for port, service in ports.items():
        sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        if result == 0:
            if port in DANGEROUS:
                print(f"[CRITICAL] {port} {service}")
                critical += 1
            else:
                print(f"[OK]        {port} {service}")
        else:
            print(f"    {port}closed")
    print(f"\nCritical:   {critical}")

def check_http(domain):
    print(f"]n---- HTTP:    {domain}")
    issues = 0
    try:
        r = requests.get(
            f"https://{domain}", timeout=5)
        print(f"[OK] HTTPS working")
        checks = {
            "Strict-Transport-Security": "HSTS", 
            "X-Frame-Options": "X-Frame",
            "X-content-Type-Options": "X-Content",
        }
        for h, name in checks.items():
            if h in r.headers:
                print(f"[OK]   {name}")
            else:
                print(f"[HIGH]  {name} MISSING")
                issues += 1
    except Exception as e:
        print(f"[ERROR] {e}")
    print(f"\nIssues:   {issues}")


def check_firewall():
    print(f"\n---- FIREWALL ANALYSIS")
    rules = [
        {"port": 80,   "source": "0.0.0.0/0"},
        {"port": 443,  "source": " 0.0.0.0/0"},
        {"port": 3306, "source": "0.0.0.0/0"},
        {"port": 5432, "source": "10.0.0.0/8"},
    ]
    critical = 0
    for rule in rules:
        port = rule["port"]
        source = rule["source"]
        if source ==  "0.0.0.0/0" and port in DANGEROUS:
            print(f"[CRITICAL] Port  {port} "
                  f"{DANGEROUS[port]}")
            critical += 1
        else:
            print(f"[OK]     port {port}    {source}")
    print(f"\nCritical:   {critical}")


def main():
    header("NETGUARD TOOLKIT v0.1.0")
    print("    by    Prajwal CK - CloudGuard")

    parser = argparse.ArgumentParser()
    parser.add_argument("---subnet")
    parser.add_argument("---scan")
    parser.add_argument("---http")
    parser.add_argument("---firewall",
                        action="store_true")
    parser.add_argument("---all",
                        action="store_true")
    args = parser.parse_args()

    if args.all:
        subnet_info("192.168.1.0/24")
        scan_ports("127.0.0.1")
        check_http("google.com")
        check_firewall()
        return
    
    if args.subnet:
        subnet_info(args.subnet)
    if args.scan:
        scan_ports(args.scan)
    if args.http:
        check_http(args.http)
    if args.firewall:
        check_firewall()

    
    if not any(vars(args).values()):
        print("\nUsage:")
        print("python netguard.py ---all")
        print("python netguard.py ---subnet 192.168.1.0/24")
        print("python netguard.py ---http google.com")
        print("python netguard.py ----firewall")

if __name__ == "__main__":
    main()

