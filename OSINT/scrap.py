import requests
from bs4 import BeautifulSoup

url = 'https://www.lemondeinformatique.fr/actualites/lire-8-outils-osint-pour-le-cyber-renseignement-80484.html'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    titres = soup.find_all('h2')

    for titre in titres:
        print(titre.get_text())
else:
    print(f"Échec de la requête, code d'état: {response.status_code}")
