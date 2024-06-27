from ping3 import ping, verbose_ping
import subprocess

def get_interface_ip(interface):
    try:
        result = subprocess.run(["ipconfig"], capture_output=True, text=True, encoding="utf-8", errors="ignore")
        lines = result.stdout.splitlines()
        interface_found = False
        for line in lines:
            if interface in line:
                interface_found = True
            if interface_found and ("IPv4 Address" in line or "Adresse IPv4" in line):
                ip = line.split(":")[-1].strip()
                return ip
    except Exception as e:
        print(f"Error getting IP for interface {interface}: {e}")
    return None

def list_interfaces():
    interfaces = []
    try:
        result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True, encoding="utf-8", errors="ignore")
        print("Output from netsh command:")
        print(result.stdout)
        lines = result.stdout.splitlines()
        for line in lines:
            if "Ddi" in line or "Dedicated" in line:  # Adapt to your locale
                interface = line.strip().split()[-1]
                interfaces.append(interface)
    except Exception as e:
        print(f"Error listing interfaces: {e}")
    return interfaces

def check_connectivity(target_ip):
    response = ping(target_ip, unit='ms')
    if response:
        print(f"{target_ip} is reachable with latency {response} ms")
        return True
    else:
        print(f"{target_ip} is not reachable")
        return False

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")

    if not check_connectivity(target_ip):
        print("Target IP is not reachable. Exiting...")
        exit(1)

    interfaces = list_interfaces()
    if not interfaces:
        print("No network interfaces found. Please check your network settings.")
        exit(1)

    print("Available network interfaces and their IP addresses:")
    interface_ips = {}
    for iface in interfaces:
        ip = get_interface_ip(iface)
        interface_ips[iface] = ip
        print(f"{iface}: {ip}")

    # Automatically select the interface with the correct subnet
    iface = None
    source_ip = None
    for interface, ip in interface_ips.items():
        if ip and ip.startswith("192.168.1."):
            iface = interface
            source_ip = ip
            break

    if not iface:
        print("No suitable network interface found.")
        exit(1)

    print(f"Using interface {iface} with IP address {source_ip}")

    print("Sending 10 ICMP Echo Request packets to", target_ip)
    for _ in range(10):
        response = ping(target_ip, unit='ms')
        if response:
            print(f"Reply from {target_ip}: time={response} ms")
        else:
            print(f"No reply from {target_ip}")

    print("Thibault est le GOAT !")
