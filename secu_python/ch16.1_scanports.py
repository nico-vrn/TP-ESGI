import socket
import time

def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
        except socket.gaierror as e:
            print(f"Erreur de connexion pour l'adresse {ip} : {e}")
            break
        except Exception as e:
            print(f"Erreur lors du scan du port {port}: {e}")
        finally:
            s.close()
    return open_ports

if __name__ == "__main__":
    target_ip = input("IP: ")
    start_port = int(input("Port de départ: "))
    end_port = int(input("Dernier port: "))

    start_time = time.time()
    open_ports = scan_ports(target_ip, start_port, end_port)
    end_time = time.time()

    scan_duration = end_time - start_time

    if open_ports:
        print(f"Ports ouverts sur {target_ip}: {open_ports}")
    else:
        print(f"Pas de ports ouverts sur {target_ip}")

    print(f"Temps pris pour le scan: {scan_duration:.2f} secondes")