import psutil
import sqlite3
import time
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

def detecter_connexions_suspectes():
    """
    Détecter les tentatives de connexion suspectes sur la machine locale.
    """
    # Liste des ports considérés comme sensibles
    ports_sensibles = [22, 23, 3389]  # Ajouter d'autres ports si nécessaire

    # Surveiller en continu les connexions réseau
    while True:
        # Récupérer la liste des connexions réseau
        connexions = psutil.net_connections()

        # Parcourir chaque connexion
        for conn in connexions:
            if conn.laddr.port in ports_sensibles and conn.status == 'LISTEN':
                # Enregistrer les informations sur la connexion suspecte
                message = f"Connexion suspecte détectée: {conn}"
                print(message)
                log_to_db("Détection des Attaques", message)
        
        # Attendre 5 secondes avant de vérifier à nouveau
        time.sleep(5)

if __name__ == "__main__":
    # Exécuter la fonction de détection des connexions suspectes
    detecter_connexions_suspectes()
