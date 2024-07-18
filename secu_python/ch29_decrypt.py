# decrypt_files.py
import os
from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password):
    # Utiliser SHA-256 pour générer une clé à partir du mot de passe
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key[:32])

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        if not encrypted_data:
            print(f"No encrypted data found in {file_path}")
            return

        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_data)

        with open(file_path, 'wb') as file:
            file.write(decrypted)
        print(f"Decrypted {file_path}")
    except Exception as e:
        print(f"Failed to decrypt {file_path}: {e}")

if __name__ == "__main__":
    password = input("Enter the password to generate the decryption key: ")
    key = generate_key(password)

    target_directory = input("Enter the target directory to decrypt files: ")

    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)
    print("Decryption completed.")
