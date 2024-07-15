import socket
import struct
import textwrap
import sqlite3
import datetime

DATABASE = '../siem_logs.db'

# Fonction pour écrire les logs dans la base de données SQLite
def log_to_db(source, message):
    timestamp = datetime.datetime.now().isoformat()
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (timestamp, source, message) VALUES (?, ?, ?)",
                       (timestamp, source, message))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erreur lors de l'écriture du log dans la DB: {e}")

def main():
    # Créer un socket brut pour capturer les paquets réseau
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        # Capturer les paquets
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        message = f"Ethernet Frame: Destination: {dest_mac}, Source: {src_mac}, Protocol: {eth_proto}"
        print(message)
        log_to_db("Surveillance du Réseau", message)

        # 8 pour IPv4
        if eth_proto == 8:
            (version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
            message = f"IPv4 Packet: Version: {version}, Header Length: {header_length}, TTL: {ttl}, Protocol: {proto}, Source: {src}, Target: {target}"
            print(message)
            log_to_db("Surveillance du Réseau", message)

            # ICMP
            if proto == 1:
                icmp_type, code, checksum, data = icmp_packet(data)
                message = f"ICMP Packet: Type: {icmp_type}, Code: {code}, Checksum: {checksum}"
                print(message)
                log_to_db("Surveillance du Réseau", message)

            # TCP
            elif proto == 6:
                (src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data) = tcp_segment(data)
                message = f"TCP Segment: Source Port: {src_port}, Destination Port: {dest_port}, Sequence: {sequence}, Acknowledgment: {acknowledgment}, Flags: URG: {flag_urg}, ACK: {flag_ack}, PSH: {flag_psh}, RST: {flag_rst}, SYN: {flag_syn}, FIN: {flag_fin}"
                print(message)
                log_to_db("Surveillance du Réseau", message)

            # UDP
            elif proto == 17:
                src_port, dest_port, length, data = udp_segment(data)
                message = f"UDP Segment: Source Port: {src_port}, Destination Port: {dest_port}, Length: {length}"
                print(message)
                log_to_db("Surveillance du Réseau", message)

# Fonction pour désassembler la trame Ethernet
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

# Retourne l'adresse MAC formatée correctement (AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

# Désassembler le paquet IPv4
def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

# Retourne une adresse IPv4 formatée correctement
def ipv4(addr):
    return '.'.join(map(str, addr))

# Désassembler le paquet ICMP
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

# Désassembler le segment TCP
def tcp_segment(data):
    (src_port, dest_port, sequence, acknowledgment, offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    return src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]

# Désassembler le segment UDP
def udp_segment(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, size, data[8:]

if __name__ == "__main__":
    main()
