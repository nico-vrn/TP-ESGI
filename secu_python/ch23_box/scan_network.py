import nmap

def network_scan(target_network):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_network, arguments='-sn')  # Ping scan
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    return hosts_list

def main():
    target_network = "192.168.56.0/24" 
    print(f"Scanning network {target_network}...")

    hosts = network_scan(target_network)

    print("Available devices in the network:")
    print("IP" + " "*18 + "State")
    for host, status in hosts:
        print("{:16}    {}".format(host, status))

if __name__ == "__main__":
    main()
