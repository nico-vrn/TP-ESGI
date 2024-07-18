import os
import json
import hashlib
import secrets
import string
from cryptography.fernet import Fernet
import bcrypt
import re

VAULT_FILE = 'vault.json'
MASTER_KEY_FILE = 'master.key'

def generate_master_key():
    key = Fernet.generate_key()
    with open(MASTER_KEY_FILE, 'wb') as f:
        f.write(key)
    return key

def load_master_key():
    if not os.path.exists(MASTER_KEY_FILE):
        return generate_master_key()
    with open(MASTER_KEY_FILE, 'rb') as f:
        return f.read()

def encrypt(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()

def save_vault(vault, master_key):
    encrypted_vault = encrypt(json.dumps(vault), master_key)
    with open(VAULT_FILE, 'wb') as f:
        f.write(encrypted_vault)

def load_vault(master_key):
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, 'rb') as f:
        encrypted_vault = f.read()
    return json.loads(decrypt(encrypted_vault, master_key))

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def add_password(vault, username, password):
    vault[username] = hash_password(password)
    return vault

def list_passwords(vault):
    return list(vault.keys())

def test_password_strength(password):
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r'\d', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    symbol_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    if all([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, symbol_criteria]):
        return "Strong"
    else:
        return "Weak"

def main():
    master_key = load_master_key()
    vault = load_vault(master_key)

    while True:
        print("\n1. Save a password")
        print("2. List passwords")
        print("3. Generate a password")
        print("4. Test password strength")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            vault = add_password(vault, username, password)
            save_vault(vault, master_key)
            print("Password saved successfully.")
        elif choice == '2':
            passwords = list_passwords(vault)
            print("Stored passwords:")
            for p in passwords:
                print(p)
        elif choice == '3':
            length = int(input("Enter password length: "))
            new_password = generate_password(length)
            print(f"Generated password: {new_password}")
        elif choice == '4':
            password = input("Enter password to test: ")
            strength = test_password_strength(password)
            print(f"Password strength: {strength}")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
