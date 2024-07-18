import hashlib

def hash_password(password):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(password.encode('utf-8'))
    return sha1_hash.hexdigest()

def crack_password(hashed_password, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            for line in file:
                # Enlever les espaces et nouvelles lignes
                password = line.strip()
                # Comparer le hash du mot de passe à celui recherché
                if hash_password(password) == hashed_password:
                    return password
    except FileNotFoundError:
        print(f"File {wordlist_file} not found.")
        return None

    return None

if __name__ == "__main__":
    # Lire le hash du mot de passe depuis le fichier
    try:
        with open('hashed_password.txt', 'r') as file:
            hashed_password = file.read().strip()
    except FileNotFoundError:
        print("File 'hashed_password.txt' not found.")
        exit(1)

    # Spécifier le fichier de la liste de mots de passe
    wordlist_file = 'password-list.txt'

    # Essayer de cracker le mot de passe
    cracked_password = crack_password(hashed_password, wordlist_file)

    if cracked_password:
        print(f"Password found: {cracked_password}")
    else:
        print("Password not found in the wordlist.")
