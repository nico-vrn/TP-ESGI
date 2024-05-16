import re
import subprocess
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='Change MAC address of a specified network interface.')
    parser.add_argument('interface', type=str, help='Network interface to change MAC address')
    parser.add_argument('new_mac', type=str, help='New MAC address')
    args = parser.parse_args()
    return args.interface, args.new_mac

def is_valid_mac(mac):
    # MAC address should be in the format: XX:XX:XX:XX:XX:XX
    if re.match(r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$", mac):
        return True
    else:
        return False

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def main():
    interface, new_mac = get_arguments()
    
    if not is_valid_mac(new_mac):
        print("[-] Invalid MAC address format. Use format: XX:XX:XX:XX:XX:XX")
        exit(1)
    
    change_mac(interface, new_mac)
    
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    if new_mac in str(ifconfig_result):
        print(f"[+] MAC address was successfully changed to {new_mac} on {interface}")
    else:
        print("[-] Failed to change MAC address.")

if __name__ == "__main__":
    main()
