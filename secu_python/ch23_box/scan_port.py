import socket

def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

if __name__ == "__main__":
    target_ip = input("IP: ")
    start_port = int(input("Port de départ: "))
    end_port = int(input("last port: "))

    open_ports = scan_ports(target_ip, start_port, end_port)

    if open_ports:
        print(f"Port ouvert sur {target_ip}: {open_ports}")
    else:
        print(f"Pas de port ouvert sur {target_ip}")
