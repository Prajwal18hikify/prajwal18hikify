import dns.resolver
import datetime

dns .resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

def lookup_dns(domain):
    print(f"\nCloudGuard DNS Lookup")
    print(f"Domain : {domain}")
    print(f"Time : {datetime.datetime.now()}")
    print(f"-------------------------------------")

    record_types = ["A", "MX", "TXT", "NS"]

    for record_type in record_types:
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
lookup_dns("google.com")  

    