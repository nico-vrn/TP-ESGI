from loguru import logger
import re
import os

# Configuration de loguru pour enregistrer les événements dans un fichier log
logger.add("analyse_forensique.log", format="{time} {level} {message}", level="INFO")

def analyser_journaux(fichier_journal):
    """
    Analyser les journaux d'un serveur web pour identifier des schémas d'attaques potentielles.

    Args:
        fichier_journal (str): Le chemin du fichier journal à analyser.
    """
    # Expressions régulières pour identifier des schémas d'attaques courantes
    patterns = {
        "Injection SQL": re.compile(r"(SELECT|UNION|INSERT|UPDATE|DELETE|DROP|ALTER|CREATE)\s", re.IGNORECASE),
        "XSS": re.compile(r"<script.*?>.*?</script>", re.IGNORECASE),
        "Inclusion de fichiers": re.compile(r"(\.\./|\.\./|%2e%2e|%252e%252e)", re.IGNORECASE)
    }

    # Ouvrir le fichier journal
    with open(fichier_journal, 'r') as fichier:
        lignes = fichier.readlines()
    
    # Analyser chaque ligne du fichier journal
    for ligne in lignes:
        for attaque, pattern in patterns.items():
            if pattern.search(ligne):
                logger.info(f"Attaque détectée ({attaque}): {ligne.strip()}")

if __name__ == "__main__":
    # Demander à l'utilisateur d'entrer le chemin du fichier journal à analyser
    fichier_journal = input("Entrez le chemin du fichier journal du serveur web à analyser : ").strip()
    
    # Vérifier si le chemin est correct et si le fichier existe
    if os.path.isfile(fichier_journal):
        try:
            # Analyser les journaux du serveur web
            analyser_journaux(fichier_journal)
        except Exception as e:
            print(f"Erreur lors de l'analyse du fichier {fichier_journal}: {e}")
    else:
        print(f"Erreur : le fichier {fichier_journal} n'existe pas.")
