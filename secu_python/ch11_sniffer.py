from scapy.all import *

def packet_callback(packet):
    try:
        print(f"Paquet : {packet.summary()}")
    except Exception as e:
        print(f"Erreur lors de l'affichage du paquet : {e}")

def main():
    print("Sniffing du trafic réseau...")
    sniff(prn=packet_callback, count=10)

if __name__ == "__main__":
    main()
