
import ipaddress

def analyze_network(cidr):
    network = ipaddress.ip_network(cidr, strict=False)

    print(f"\nAnalyzing : {cidr}")
    print(f"Network  : {network.network_address}")
    print(f"Mask : {network.netmask}")
    print(f"Broadcast ; {network.broadcast_address}")
    print(f"First IP : {list(network.hosts())[0]}")
    print(f"Last IP : {list(network.hosts())[-1]}")
    print(f"Total : {network.num_addresses -2}")

analyze_network("192.168.1.0/24")
analyze_network("10.0.0.0/16")
analyze_network("172.16.0.0/12")
