from scapy.all import *
import os

def send_icmp_broadcast(target_ip, source_ip, count=10):
    for i in range(count):
        packet = IP(src=source_ip, dst=target_ip) / ICMP()
        send(packet, verbose=0)
        print(f"Sent ICMP packet {i+1}")

def analyze_icmp_replies():
    def icmp_reply(packet):
        if packet.haslayer(ICMP) and packet[ICMP].type == 0:  # ICMP Echo Reply
            print(f"Received ICMP Echo Reply from {packet[IP].src}")

    sniff(filter="icmp", prn=icmp_reply, timeout=10)

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    broadcast_ip = input("Enter the broadcast IP address: ")
    
    print("Sending ICMP Echo Request packets with broadcast source IP")
    send_icmp_broadcast(target_ip, broadcast_ip)
    
    print("Analyzing ICMP Echo Replies")
    analyze_icmp_replies()
