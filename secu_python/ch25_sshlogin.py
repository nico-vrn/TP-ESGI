import paramiko
import threading

def ssh_connect(hostname, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port, username, password)
        print(f"Connected to {hostname} on port {port} with username {username}")
        return client
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
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

def main():
    hostname = "192.168.56.104"
    port = 22
    username = "test"
    password = "test"

    client = ssh_connect(hostname, port, username, password)
    if client:
        channel = client.invoke_shell()
        print("Interactive SSH session established. Type 'exit' to quit.")
        interactive_shell(channel)
        channel.close()
        client.close()

if __name__ == "__main__":
    main()
