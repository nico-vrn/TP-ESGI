import socket
import time
import threading
from queue import Queue

# Nmbrs threads à use
NUM_THREADS = 100

# scanne port spécifique
def scan_port(ip, port, open_ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
    except Exception as e:
        pass
    finally:
        s.close()

# Fct worker por threads
def worker(ip, port_queue, open_ports):
    while not port_queue.empty():
        port = port_queue.get()
        scan_port(ip, port, open_ports)
        port_queue.task_done()

# Fonct gérer le scan des ports
def scan_ports(ip, start_port, end_port):
    open_ports = []
    port_queue = Queue()

    # feed la file d'attente avec les ports
    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    # Créer et démarrer les threads
    threads = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=worker, args=(ip, port_queue, open_ports))
        thread.start()
        threads.append(thread)

    # Attendre que toutes les tâches de la file d'attente soient complétées
    port_queue.join()

    # Attendre que tous les threads soient terminés
    for thread in threads:
        thread.join()

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