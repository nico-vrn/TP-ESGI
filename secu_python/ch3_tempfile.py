import tempfile
import os

def main():
    # Création d'un fichier temporaire
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        print(f"Fichier temporaire créé à : {temp_file.name}")
        
        temp_file.write(b"Ici c'est Grenoble ! #BDL")
        
        temp_file.close()
        
        with open(temp_file.name, 'r') as file:
            content = file.read()
            print("Contenu du fichier temporaire :")
            print(content)
    
if __name__ == "__main__":
    main()
