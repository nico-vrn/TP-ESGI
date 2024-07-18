import hashlib

def hash_password(password):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(password.encode('utf-8'))
    return sha1_hash.hexdigest()

if __name__ == "__main__":
    # Demander le mot de passe à l'utilisateur
    password = input("Enter the password to hash: ")
    hashed_password = hash_password(password)
    print(f"SHA-1 hash of the password: {hashed_password}")

    # Sauvegarder le hash dans un fichier
    with open('hashed_password.txt', 'w') as file:
        file.write(hashed_password)
    print("Password hash has been saved to 'hashed_password.txt'")
