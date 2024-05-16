import paramiko
import os

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

def upload_directory(client, local_directory, remote_directory):
    try:
        sftp = client.open_sftp()
        
        for root, dirs, files in os.walk(local_directory):
            for directory in dirs:
                local_path = os.path.join(root, directory)
                relative_path = os.path.relpath(local_path, local_directory)
                remote_path = os.path.join(remote_directory, relative_path)
                try:
                    sftp.mkdir(remote_path)
                except IOError:
                    print(f"Directory {remote_path} already exists")
                    
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, local_directory)
                remote_path = os.path.join(remote_directory, relative_path)
                print(f"Uploading {local_path} to {remote_path}")
                sftp.put(local_path, remote_path)
                
        sftp.close()
        print(f"Successfully uploaded {local_directory} to {remote_directory}")
    except Exception as e:
        print(f"Failed to upload directory: {e}")

def main():
    hostname = "192.168.56.104"  # Remplacez par l'adresse IP de votre serveur SSH
    port = 22
    username = "test"  # Remplacez par votre nom d'utilisateur SSH
    password = "test"  # Remplacez par votre mot de passe SSH
    
    local_directory = "/home/net/Documents/malware/TP-ESGI/secu_python/ch23_box/ranconware"  # Remplacez par le chemin du dossier local à envoyer
    remote_directory = "/home/test/ran"  # Remplacez par le chemin de destination sur le serveur

    client = ssh_connect(hostname, port, username, password)
    if client:
        upload_directory(client, local_directory, remote_directory)
        client.close()

if __name__ == "__main__":
    main()
