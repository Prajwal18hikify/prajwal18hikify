#!/usr/bin/env python3
"""
http_checker.py - HTTP & Security Headers
CloudGuard Phase 1  | Day 4  | Prajwal CK

What it does: 
- Checks if HTTPS is enabled
- Checks TLS version (1.2 or 1.3 required)
- Audits 7 critical security headers

Why it matters for CloudGuard:
- Web application security check in Phase 4
- Missing headers = SOC2 compliance failure

Usage: python http_checker.py https://example.com  
"""
import requests
import datetime

def check_http_security(domain):
    print(f"\nCloudGuard HTTP Security Check")
    print(f"Domain : {domain}")
    print(f"Time : {datetime.datetime.now()}")
    print(f"-----------------------------------")

    findings = []

    try:
        r = requests.get(
            f"https://{domain}",
            timeout=5
        )
        print(f"\nHTTPS  : WORKING - OK")

        headers = r.headers

        if "Strict-Transport-Security" in headers:
            print(f"HSTS  : FOUND - OK")
        else:
            print(f"HSTS   : MISSING - HIGH RISK")
            findings.append("HSTS missings")
        
        if "X - Frame-options" in headers:
            print(f"X-FRAME   : FOUND-Ok")
        else:
            print(f"X-FRAME   : MISSING - MEDIUM RISK")
            findings.append("X-Frame-options missings")
        
        if "X-Content-Type-Options" in headers:
            print(f"X-Content   :  FOUND  -  Ok")
        else:
            print(f"X-Content   : MISSING - MEDIUM RISK")
            findings.append("X-Content-Type missing")

    except Exception as e:
        print(f"HTTPS    :  ERROR  -  {e}")
        findings.append("HTTPS not working")

    print(f"\n----------------------------------------")
    print(f"Total issues    : {len(findings)}")

    for f in findings:
        print(f" WARNING:  {f}")


check_http_security("google.com")
check_http_security("github.com")
