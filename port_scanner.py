#!/usr/bin/env python3
"""
port_scanner.py - Open Port & Risk Detector
CloudGuard Phase 1  | Day 2  | Prajwal CK

What it does:
- Scans any host for open TCP ports
- Flags dangerous services with risk levels
- Uses multi-threading for fast scanning

Why it matters for CloudGuard:
- Detects exposed databases and services
- Verifies AWS Security Group rules are enforced

Usage: python port_scanner.py 192.168.1.1
"""

# socket = Python networking library for TCP connections
# datetime = for timestamp in scan report

import socket
import datetime

# Dictionary of ports to scan - port: service name
PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-Alt"
}

# Ports that should NEVER be open to internet
# If open = flag as DANGEROUS in output
DANGEROUS = [22,3306,5432,6379]

# Try to connect to each port - if success = port is open
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