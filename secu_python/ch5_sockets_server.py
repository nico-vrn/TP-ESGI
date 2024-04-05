import socket
import threading

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Message reçu : {message}")
        client_socket.send("Message reçu".encode('utf-8'))
    client_socket.close()

def server():
    host = '127.0.0.1'
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Le serveur écoute sur {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connexion établie avec {address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    server()
