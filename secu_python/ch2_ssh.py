import spur

def connect_ssh(username, password, hostname):
    shell = spur.SshShell(hostname=hostname, username=username, password=password, missing_host_key=spur.ssh.MissingHostKey.accept)
    with shell:
        result = shell.run(["echo", "Connexion SSH réussie!"])
        print(result.output.decode())

if __name__ == "__main__":
    username = ""
    password = ""
    hostname = ""
    connect_ssh(username, password, hostname)
