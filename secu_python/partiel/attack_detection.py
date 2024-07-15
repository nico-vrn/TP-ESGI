import psutil
from loguru import logger
import time

# Configuration de loguru pour enregistrer les événements dans un fichier log et dans la console
logger.add("connexions_suspectes.log", format="{time} {level} {message}", level="INFO")
logger.add(lambda msg: print(msg, end=""), format="{time} {level} {message}", level="INFO")

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
                logger.info(f"Connexion suspecte détectée: {conn}")
        
        # Attendre 5 secondes avant de vérifier à nouveau
        time.sleep(5)

if __name__ == "__main__":
    # Exécuter la fonction de détection des connexions suspectes
    detecter_connexions_suspectes()
