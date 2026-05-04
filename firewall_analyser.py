import datetime

DANGEROUS_PORTS = {
    22 : "SSH",
    23 : "Telnet",
    3306 : " MySQL",
    5432 : "PostgreSQL",
    6379 : "Redis",
    27017 : "MangoDB",
    3389 : "RDP"
}

def analyse_firewall(rules):
    print(f"\nCloudGuard Firewall Analyzer")
    print(f"Time : {datetime.datetime.now()}")
    print(f"{'-'*40}")

    critical = 0

    for rule in rules:
        port = rule["port"]
        source = rule["source"]


        if source == "0.0.0.0/0" and port in DANGEROUS_PORTS:
            print(f"\n[CRITICAL] Port {port} {DANGEROUS_PORTS[port]}")
            print(f" open to : entire internet")
            print(f" Fix  : restrictr to your IP only")
            critical += 1
        else:
            print(f"\n[OK] Port {port}-{source}")

    print(f"\n{'-*40'}")
    print(f"Critical issues: {critical}")
    if critical == 0:
        print("Firewall secure!")
    else:
        print(f"Fix {critical} issues NOW!")

rules = [
    {"port" : 80, "source": "0.0.0.0/0"},
    {"port" : 443, "source": "0.0.0.0/0"},
    {"port" : 22, "source": "0.0.0.0/0"},
    {"port" : 3306, "source": "0.0.0.0/0"},
    {"port" : 5432, "source": "10.0.0.0/8"}
]

analyse_firewall(rules)

