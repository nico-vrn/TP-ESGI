# encrypt_files.py
import os
from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password):
    # Utiliser SHA-256 pour générer une clé à partir du mot de passe
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key[:32])

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        if not data:
            print(f"No data found in {file_path}")
            return

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(file_path, 'wb') as file:
            file.write(encrypted)
        print(f"Encrypted {file_path}")
    except Exception as e:
        print(f"Error encrypting {file_path}: {e}")

if __name__ == "__main__":
    password = input("Enter the password to generate the encryption key: ")
    key = generate_key(password)

    target_directory = input("Enter the target directory to encrypt files: ")

    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)
    print("Encryption completed.")
