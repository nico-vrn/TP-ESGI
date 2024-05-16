import nmap

def port_scan(target_ip):
    nm = nmap.PortScanner()
    print(f"Scanning ports on {target_ip}...")
    nm.scan(target_ip, '1-1024', '-T4')
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            lport = nm[host][proto].keys()
            for port in lport:
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")

def main():
    target_ip = "192.168.56.104"
    port_scan(target_ip)

if __name__ == "__main__":
    main()
