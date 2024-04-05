import argparse
import os

def process_file(path, mode, verbose):
    if not os.path.exists(path):
        print(f"Le fichier '{path}' n'existe pas.")
        return

    if mode == 'analyse':
        with open(path, 'r') as file:
            lines = file.readlines()
            print(f"Le fichier '{path}' contient {len(lines)} lignes.")
            if verbose:
                print("Détails du mode verbose : Analyse terminée avec succès.")

    elif mode == 'rapport':
        with open(path, 'r') as file:
            content = file.read()
            print(f"Contenu du fichier '{path}':\n{content}")
            if verbose:
                print("Détails du mode verbose : Rapport généré avec succès.")

    elif mode == 'nettoyage':
        os.remove(path)
        print(f"Le fichier '{path}' a été supprimé.")
        if verbose:
            print("Détails du mode verbose : Nettoyage effectué avec succès.")


def main():
    parser = argparse.ArgumentParser(description="Script de démonstration pour le traitement de fichiers.")

    parser.add_argument('-p', '--path', required=True, help="Chemin vers le fichier à traiter.")
    parser.add_argument('-m', '--mode', choices=['analyse', 'rapport', 'nettoyage'], default='analyse',
                        help="Mode de fonctionnement du script. Choix possibles : analyse, rapport, nettoyage.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Active le mode verbose pour afficher plus de détails.")

    args = parser.parse_args()

    process_file(args.path, args.mode, args.verbose)

if __name__ == "__main__":
    main()
