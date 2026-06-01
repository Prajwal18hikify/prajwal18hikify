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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ip_intel.py <py>")
        print("Example: python ip_intel.py 8.8.8.8")
        sys.exit(1)

    intel = IPIntel(sys.argv[1])
    intel.analyse()
    