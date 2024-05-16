import subprocess

def run_nmap_scan():
    try:
        command = ['sudo', 'nmap', '-sn', '192.168.56.0/24']
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        print(e.output)

def main():
    run_nmap_scan()

if __name__ == "__main__":
    main()
