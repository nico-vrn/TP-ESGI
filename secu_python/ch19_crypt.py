import bcrypt
import itertools
import string
import logging
from tqdm import tqdm

logging.basicConfig(filename='bruteforce.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def encrypt_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def create_user_list(password):
    user_list = [
        {"login": "user1", "password": encrypt_password("password1").decode('utf-8')},
        {"login": "user2", "password": encrypt_password("password2").decode('utf-8')},
        {"login": "user3", "password": encrypt_password("password3").decode('utf-8')}
    ]

    user_list.append({"login": "my_user", "password": encrypt_password(password).decode('utf-8')})
    return user_list

def brute_force_decrypt(encrypted_password):
    characters = string.ascii_letters + string.digits
    max_length = 6  

    encrypted_password = encrypted_password.encode('utf-8')
    total_guesses = sum(len(characters) ** i for i in range(1, max_length + 1))

    logging.info(f"Starting brute force attack on {encrypted_password.decode('utf-8')}")
    
    for length in range(1, max_length + 1):
        for guess in tqdm(itertools.product(characters, repeat=length), total=total_guesses, unit=" guess"):
            guess = ''.join(guess)
            if bcrypt.checkpw(guess.encode('utf-8'), encrypted_password):
                logging.info(f"Password found: {guess}")
                return guess
            logging.debug(f"Tried password: {guess}")
    logging.info("Password not found within max length")
    return None

if __name__ == "__main__":
    password = input("Enter a password to encrypt: ")
    user_list = create_user_list(password)
    print("User list with encrypted passwords:")
    for user in user_list:
        print(user)

    for user in user_list:
        decrypted_password = brute_force_decrypt(user["password"])
        if decrypted_password:
            print(f"Decrypted password for {user['login']}: {decrypted_password}")
        else:
            print(f"Could not decrypt password for {user['login']}")
