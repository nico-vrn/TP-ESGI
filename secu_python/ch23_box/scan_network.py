from ping3 import ping
import concurrent.futures

def ping_ip(ip):
    """
    Ping une adresse IP pour vérifier si elle est active.
    """
    try:
        response = ping(ip, timeout=1)
        if response:
            return ip
    except Exception as e:
        pass
    return None

def scan_network(base_ip, start, end):
    """
    Scanne les adresses IP dans la plage donnée.
    """
    active_ips = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(ping_ip, f"{base_ip}.{i}"): i for i in range(start, end + 1)}
        for future in concurrent.futures.as_completed(futures):
            ip = future.result()
            if ip:
                active_ips.append(ip)
    return active_ips

if __name__ == "__main__":
    base_ip = input("Entrez la base de l'adresse IP (par ex. 192.168.1): ")
    start_ip = int(input("Entrez le début de la plage d'IP: "))
    end_ip = int(input("Entrez la fin de la plage d'IP: "))

    print(f"Scanning the network {base_ip}.{start_ip} to {base_ip}.{end_ip}...")

    active_ips = scan_network(base_ip, start_ip, end_ip)

    if active_ips:
        print(f"Adresses IP actives trouvées sur le réseau {base_ip}:")
        for ip in active_ips:
            print(ip)
    else:
        print(f"Aucune adresse IP active trouvée sur le réseau {base_ip} dans la plage spécifiée.")
