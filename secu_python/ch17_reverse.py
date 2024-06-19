import paramiko
from scp import SCPClient
import time

def create_ssh_client(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def list_home_directory(ssh_client):
    stdin, stdout, stderr = ssh_client.exec_command('ls -la /home')
    print("Listing /home directory:")
    for line in stdout:
        print(line.strip())

def transfer_file_to_remote(ssh_client, local_file, remote_file):
    scp = SCPClient(ssh_client.get_transport())
    scp.put(local_file, remote_file)
    print(f"Transferred {local_file} to {remote_file} on remote host.")
    scp.close()

def transfer_file_from_remote(ssh_client, remote_file, local_file):
    scp = SCPClient(ssh_client.get_transport())
    scp.get(remote_file, local_file)
    print(f"Transferred {remote_file} from remote host to {local_file}.")
    scp.close()

def reverse_shell(ssh_client):
    print("Starting reverse shell...")
    channel = ssh_client.invoke_shell()
    while True:
        command = input("Enter command to execute on remote host: ")
        if command.lower() in ['exit', 'quit']:
            print("Exiting reverse shell.")
            break
        channel.send(command + '\n')
        while not channel.recv_ready():
            time.sleep(1)
        output = channel.recv(1024).decode('utf-8')
        print(output)

if __name__ == "__main__":
    server = input("Enter server address: ")
    port = int(input("Enter port number: "))
    user = input("Enter username: ")
    password = input("Enter password: ")

    ssh_client = create_ssh_client(server, port, user, password)

    list_home_directory(ssh_client)

    local_file = input("Enter the path of the local file to transfer to remote: ")
    remote_file = input("Enter the path on the remote host to save the file: ")
    transfer_file_to_remote(ssh_client, local_file, remote_file)

    reverse_shell(ssh_client)

    ssh_client.close()
