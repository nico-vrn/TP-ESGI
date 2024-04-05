from scapy.all import *

def main():
    packet = IP(dst="8.8.8.8")/ICMP()
    packet.show()
    
    response = sr1(packet, timeout=5)
    
    if response:
        print("Réponse reçue :")
        response.show()
    else:
        print("Aucune réponse")

if __name__ == "__main__":
    main()
