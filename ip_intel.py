#!/usr/bin/ env python 3
"""
ip_intel.py  - IP Intelligence Tool
CloudGuard Phase 1  | Day 15  | Prajwal CK

What it does:
- Takes any IP address
- Queries ipinfo.io API
- Returns country city, ISP, org
- Flags suspicious IPs

What it matters for CloudGuard:
- Phase 2: Check if AWS resources are connecting to suspicious IPs
- Becomes threat intelligence module

Usage: python ip_intel.py 8.8.8.8
"""

import requests
import json
import sys
import argparse

class IPIntel:
    """
    IP Intelligence class.
    Queries ipinfo.io for any IP address.
    """

    # API endpoint - free, no key needed
    BASE_URL = "https://ipinfo.io"

    def __init__(self, ip):
        self.ip = ip
        self.data = {}

    def lookup(self):
        try:
            r = requests.get(
                f"{self.BASE_URL}/{self.ip}/json",
                timeout=5
            )
            if r.status_code == 200:
                self.data = r.json()
                return self.data
            else:
                print(f"[ERROR] Ststus: {r.status_code}")
                return {}
        except requests.exceptions.Timeout:
            print("[ERROR] Request timed out")
            return {}
        except requests.exceptions.ConnectionError:
            print("[ERROR] No internet connection")
            return {}
        except Exception as e:
            print(f"[ERROR] {e}")
            return {}
    
    def analyse(self):
        print("\n" + "="*50)
        print("    CLOUDGAURD - IP INTELLIGENCE")
        print("="*50)

        data = self.lookup()

        if not data:
            print("[ERROR] Could not retrieve data")
            return
        
        # Basic Info
        print(f"\n[INFO] IP        : {data.get('ip')}")
        print(f"[INFO] Hostname    : {data.get('hostname')}")
        print(f"[INFO] City        : {data.get('city')}")
        print(f"[INFO] Region      : {data.get('region')}")
        print(f"[INFO] Country     : {data.get('country')}")
        print(f"[INFO] Organisation: {data.get('org')}")
        print(f"[INFO] Timezone    : {data.get('timezone')}")

        # Security Analysis
        print(f"\n[SECURITY ANALYSIS]")
        org = data.get('org', '').lower()

        suspicious = [
            'digitalocean', 'linode', 'vultr',
            'tor', 'vpn', 'proxy', 'hosting'
        ]

        if any(s in org for s in suspicious):
            print(f"[MEDIUM] Cloud/VPN provider detected")
            print(f"[MEDIUM] Verify if this IP should have access")
        else:
            print(f"[PASS] Organisation looks normal")

        print("\n" + "="*50 + "\n")
    def save_results(self, filename="results.json"):
            with open(filename, "a") as f:
                json.dump(self.data, f, indent=4)
                f.write("\n")
            print(f"[SAVED] Results saved to {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ips", nargs="*")
    parser.add_argument("--save", action="store_true")
    parser.add_argument("--file")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r") as f:
            ip_list = [line.strip() for line in f]
    else:
        ip_list = args.ips

    for ip in ip_list:
        intel = IPIntel(ip)
        intel.analyse()
        if args.save:
            intel.save_results()
    