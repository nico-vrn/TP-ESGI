import os
import hashlib
import sqlite3
import datetime

DATABASE = '../siem_logs.db'

# Fonction pour écrire les logs dans la base de données SQLite
def log_to_db(source, message):
    timestamp = datetime.datetime.now().isoformat()
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (timestamp, source, message) VALUES (?, ?, ?)",
                       (timestamp, source, message))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erreur lors de l'écriture du log dans la DB: {e}")

def hash_file(filepath):
    """
    Calculer le hash MD5 d'un fichier.

    Args:
        filepath (str): Le chemin du fichier.

    Returns:
        str: Le hash MD5 du fichier sous forme de chaîne hexadécimale.
    """
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def lister_fichiers(repertoire):
    """
    Parcourir un répertoire et lister les fichiers avec leurs tailles et hash MD5.

    Args:
        repertoire (str): Le chemin du répertoire à parcourir.
    """
    for root, dirs, files in os.walk(repertoire):
        for file in files:
            filepath = os.path.join(root, file)
            file_size = os.path.getsize(filepath)
            file_hash = hash_file(filepath)
            message = f"Fichier: {filepath}, Taille: {file_size} octets, Hash MD5: {file_hash}"
            print(message)
            log_to_db("Gestion des Fichiers", message)

if __name__ == "__main__":
    # Demander à l'utilisateur d'entrer le répertoire à analyser
    repertoire_a_analyser = input("Entrez le répertoire à analyser : ")
    
    # Vérifier si le chemin entré est un répertoire valide
    if os.path.isdir(repertoire_a_analyser):
        # Lancer la fonction pour lister les fichiers
        lister_fichiers(repertoire_a_analyser)
    else:
        print(f"Erreur : {repertoire_a_analyser} n'est pas un répertoire valide.")
