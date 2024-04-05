import socket
import sys

def client(message):
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message.encode('utf-8'))
        response = client_socket.recv(1024)
        print(f"Réponse du serveur : {response.decode('utf-8')}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python client.py <message>")
        sys.exit(1)
    message = sys.argv[1]
    client(message)
