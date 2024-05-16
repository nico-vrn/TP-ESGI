from scapy.all import ARP, Ether, srp

def network_scan(target_ip):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []

    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients

def main():
    target_ip = "192.168.56.0/24" 
    print(f"Scanning network {target_ip}...")

    clients = network_scan(target_ip)

    print("Available devices in the network:")
    print("IP" + " "*18 + "MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))

if __name__ == "__main__":
    main()
