import requests

def request_http(url):
    try:
        reponse = requests.get(url)
                
        print(reponse.content) 
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")

if __name__ == "__main__":
    url = "https://google.fr" 
    request_http(url)
