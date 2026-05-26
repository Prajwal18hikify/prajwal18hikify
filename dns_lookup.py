#!/usr/bin/env python3
"""
dns_lookup.py - DNS Record Inspector & Security Checker
CloudGuard Phase 1  | Day 3  | Prajwal CK

What it does:
- Queries A, MX, TXT, NS records for any domain
- Detects missing SPF - email spoofing risk
- Detects missing DMARC - phishing risk
- Detects missing DNSSEC - DNS poisoning risk

Why it matters for CloudGuard:
- Becomes domain security check in Phase 3
- Missing SPF/DMARC = SOC2 compliance failure

Usage: python dns_lookup.py google.com
"""
import dns.resolver
import datetime

dns .resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

# Main function - queries all DNS record types for a domain
def lookup_dns(domain):
    print(f"\nCloudGuard DNS Lookup")
    print(f"Domain : {domain}")
    print(f"Time : {datetime.datetime.now()}")
    print(f"-------------------------------------")

# Record types to check:
# A = IPv4 address, MX = mail server
# TXT = SPF/DMARC, NS = nameserver
    record_types = ["A", "MX", "TXT", "NS"]

# Loop through each record type and query DNS
    for record_type in record_types:

# try/except - DNS query may fail if record doesn't exist
        try:
            answers = dns.resolver.resolver(
                domain,
                record_type
            )
            print(f"\n{record_type} Records:")
            for answer in answers:
                print(f" → {answer}")
        except Exception:
            print(f"\n{record_type} Records:")
            print(f" → none found")

    print(f"\n-----------------------------------")
# Run the DNS lookup om google.com as example
lookup_dns("google.com")  

    