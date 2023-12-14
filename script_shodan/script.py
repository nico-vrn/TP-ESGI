import shodan
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re
import csv

# Clé API Shodan
API_KEY = ''
api = shodan.Shodan(API_KEY)

# Fonction pour nettoyer la chaîne de requête pour l'utiliser comme nom de fichier
def sanitize_filename(query):
    # Supprimer les caractères non valides pour les noms de fichiers
    return re.sub(r'[^a-zA-Z0-9 \n\.]', '_', query)

# Fonction pour effectuer une recherche Shodan et retourner les résultats
def search_shodan(query):
    try:
        results = api.search(query)
        print('Résultats trouvés : {}'.format(results['total']))
        
        # Afficher les détails pour chaque correspondance
        for match in results['matches']:
            print("IP: {}".format(match.get('ip_str')))
            print("Organisation: {}".format(match.get('org')))
            print("Port: {}".format(match.get('port')))
            print("Pays: {}".format(match.get('location', {}).get('country_name')))
            print("Données: {}".format(match.get('data')))
            print("--------------------------------------------------")
        
        return results['matches']
    except shodan.APIError as e:
        print('Erreur : {}'.format(e))
        return []

# Fonction pour sauvegarder les résultats dans un fichier CSV
def save_results(matches, query):
    filename = sanitize_filename(query) + '_resultats.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ip_str', 'org', 'port', 'hostnames', 'location', 'timestamp', 'data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for match in matches:
            row = {field: match.get(field, '') for field in fieldnames}
            writer.writerow(row)

# Fonction pour créer et sauvegarder une visualisation des données
def visualize_data(matches, query):
    df = pd.DataFrame(matches)

    # Extraire le pays de chaque hôte et l'ajouter comme nouvelle colonne
    df['country'] = df['location'].apply(lambda x: x.get('country') if isinstance(x, dict) else 'Inconnu')

    # Nettoyer le nom de la requête pour l'utiliser comme nom de fichier
    filename_base = sanitize_filename(query)

    # Créer un graphique du nombre de ports
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='port', order=df['port'].value_counts().index)
    plt.title('Répartition des Ports Ouverts')
    plt.xticks(rotation=90)
    plt.tight_layout()
    ports_distribution_filename = f'{filename_base}_distribution_ports.png'
    plt.savefig(ports_distribution_filename)

    # Créer un graphique du nombre d'organisations
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='org', order=df['org'].value_counts().index)
    plt.title('Répartition des Organisations')
    plt.xticks(rotation=90)
    plt.tight_layout()
    orgs_distribution_filename = f'{filename_base}_distribution_organisations.png'
    plt.savefig(orgs_distribution_filename)

    # Créer un graphique du nombre d'hôtes par pays
    df['country_name'] = df.apply(lambda x: x.get('location', {}).get('country_name', 'Inconnu'), axis=1)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, y='country_name', order=df['country_name'].value_counts().index)
    plt.title('Répartition par Pays')
    plt.tight_layout()
    filename_base = sanitize_filename(query)
    country_distribution_filename = f'{filename_base}_distribution_pays.png'
    plt.savefig(country_distribution_filename)
    
    # Afficher les graphiques
    plt.show()

# Fonction principale pour gérer le flux de travail
def main():
    # Demander à l'utilisateur la requête de recherche
    query = input("Entrez la requête de recherche Shodan : ")
    filename_base = sanitize_filename(query)
    
    # Effectuer la recherche
    matches = search_shodan(query)
    
    # Sauvegarder les résultats
    save_results(matches, query)

    
    # Visualiser les données s'il y a des correspondances
    if matches:
        visualize_data(matches, query)

if __name__ == '__main__':
    main()
