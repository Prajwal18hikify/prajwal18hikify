import socket
import datetime

PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-Alt"
}

DANGEROUS = [22,3306,5432,6379]

def scan_port(ip, port):
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        return True
    return False

def scan_target(ip):
    print(f"CloudGuard Port Scanner")
    print(f"Target : {ip}")
    print(f"Time : {datetime.datetime.now()}")
    print(f"---------------------------------------")

    open_ports = []

    for port, service in PORTS.items():
        is_open = scan_port(ip, port)
        if is_open:
            open_ports.append(port)
            if port in DANGEROUS:
                print(f"Port {port} {service} DANGEROUS")
            else:
                print(f"Port {port} {service} OPEN")
        else:
            print(f"Port {port} {service} closed")
    print(f"------------------------------------------------")
    print(f"Total open: {len(open_ports)}")

scan_target("127.0.0.1")