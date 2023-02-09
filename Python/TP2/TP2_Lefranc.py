import random
import tkinter as tk
import json

#fonction qui vérifie si un nombre donnée est bien un nombre et pas un caractère
def estunnombre(X):
    if X.isdigit():
        return True
    else:
        print("Entrez un nombre entier comme indiqué") 
        return False

def surface_sous_courbe():
    print("Vous allez entrez 2 nombre réel et un nombre à virgule et je vais vous donner l'intégral de la fonction y=x*x")
    while True:
        a = input("Entrez A: ")
        b = input("Entrez B: ")
        p = input("Entrez P (nombre à virgule avec un . sous forme 0.1 ou 2.3): ")
        if estunnombre(a) and estunnombre(b) and estunnombre(p.replace(".", "", 1)):
            a = int(a)
            b = int(b)
            p=float(p)
            break
    #print(p)

    #Solution 1 :
    U0=int(a)*int(a)*p
    S=U0
    n=1
    while(int(a)+p*int(n)<int(b)):
        U0=(int(a)+p*n)*(int(a)+p*n)*p
        S=S+U0
        n=n+1
    print("Solution 1 : La surface sous la courbe est de : ",S)

    #Solution 2 :
    S=0
    L=int(a)
    while(L<int(b)):
        S=S+L*L*p
        L=L+p
    print("Solution 2 : La surface sous la courbe est de : ",S)

    print("Calcul de l'intégrale de la fonction y=x*x avec ",a, "<= x <", b, " et p =", p)
    print("La surface sous la courbe est de : ",S)

def jeu_allumettes():
    nom= input("Entrez votre nom : ")
    print("Bienvenue ",nom," dans le jeu des allumettes")
    print("Vous allez jouer contre l'ordinateur")
    while True:
        nb_allumettes= input("Choisir le nombre d'allumettes de départ:")
        if estunnombre(nb_allumettes):
            nb_allumettes=int(nb_allumettes)
            break
    print("\nVous allez pouvoir enlever 1,2 ou 3 allumettes :")
    while nb_allumettes>0:
        print("\nIl reste ",nb_allumettes," allumettes")
        #afficher les allumettes par des |
        for i in range (nb_allumettes):
            print("|",end="")
        nb_allumettes_joueur= input("\nCombien d'allumettes voulez-vous enlever ?")
        if estunnombre(nb_allumettes_joueur):
            nb_allumettes_joueur=int(nb_allumettes_joueur)
        if nb_allumettes_joueur>3 or nb_allumettes_joueur<1:
            print("Vous ne pouvez pas enlever plus de 3 allumettes ou moins d'une allumette")
        else:
            nb_allumettes=nb_allumettes-nb_allumettes_joueur
            if nb_allumettes==0:
                print("Vous avez perdu, l'ordinateur a gagné")
                break
            nb_allumettes_ordinateur=random.randint(1,3)
            print("L'ordinateur enlève ",nb_allumettes_ordinateur," allumettes")
            nb_allumettes=nb_allumettes-nb_allumettes_ordinateur
            if nb_allumettes<=0:
                print("Bravo",nom,"Vous avez gagné!!")
                break

def fichier():
    while True :
        num1=input("Entrez un premier nombre entier : ")
        num2=input("Entrez un second nombre entier : ")
        if estunnombre(num1) and estunnombre(num2):
            num1=int(num1)
            num2=int(num2)
            break
    with open ("BDD.bin","wb") as f:
        f.write(num1.to_bytes(4, "big"))
        f.write(num2.to_bytes(4, "big"))
    print("\nLes entiers ont été écrits dans le fichier BDD.bin")

    with open("BDD.txt", "w") as f:
        f.write(str(num1) + "\n")
        f.write(str(num2) + "\n")
    print("Les entiers ont été écrits dans le fichier BDD.txt")

    with open("BDD.bin", "rb") as f:
        num1 = int.from_bytes(f.read(4), "big")
        num2 = int.from_bytes(f.read(4), "big")
    print(f"\nLes entiers lus depuis le fichier BDD.bin sont {num1} et {num2}.")

    with open("BDD.txt", "r") as f:
        num1 = int(f.readline())
        num2 = int(f.readline())
    print(f"Les entiers lus depuis le fichier BDD.txt sont {num1} et {num2}.")

class Livre:
    def __init__(self, titre, auteur, edition,barcode):
        self.titre = titre
        self.auteur = auteur
        self.edition=edition
        self.barcode=barcode

    def afficher_livre(self):
        print("\n----------------")
        print("Nom : ", self.titre)
        print("Auteur : ", self.auteur)
        print("Editeur : ", self.edition)
        print("Barcode : ", self.barcode)
        print("----------------")
    
    def modifier_livre(self,titre=None, auteur=None, edition=None, barcode=None):
        if titre:
            self.titre=titre
        if auteur:
            self.auteur=auteur
        if edition:
            self.edition=edition
        if barcode:
            self.barcode=barcode
    

class Roman(Livre):
    def __init__(self, titre, auteur, edition, barcode, genre, synopsis):
        Livre.__init__(self, titre, auteur, edition, barcode)
        self.genre = genre
        self.synopsis = synopsis
    
    def afficher_livre(self):
        Livre.afficher_livre(self)
        print("Genre : ", self.genre)
        print("Synopsis : ", self.synopsis)
        print("----------------")

    def modifier_livre(self,titre=None, auteur=None, edition=None, barcode=None, genre=None, synopsis=None):
        Livre.modifier_livre(self,titre,auteur,edition,barcode)
        if genre:
            self.genre=genre
        if synopsis:
            self.synopsis=synopsis


romans = []
class AjoutRomanUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ajouter un roman")
        self.geometry("400x300")
        
        tk.Label(self, text="Nom: ").grid(row=0, column=0, padx=10, pady=10)
        self.nom = tk.Entry(self)
        self.nom.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Auteur: ").grid(row=1, column=0, padx=10, pady=10)
        self.auteur = tk.Entry(self)
        self.auteur.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Editeur : ").grid(row=2, column=0, padx=10, pady=10)
        self.maison_edition = tk.Entry(self)
        self.maison_edition.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Barcode : ").grid(row=3, column=0, padx=10, pady=10)
        self.code_barre = tk.Entry(self)
        self.code_barre.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self, text="Genre : ").grid(row=4, column=0, padx=10, pady=10)
        self.type_roman = tk.StringVar(self)
        self.type_roman.set("roman d'analyse") 
        self.type_roman_menu = tk.OptionMenu(self, self.type_roman, "roman d'analyse", "roman d'aventures", "roman épistolaire", "roman autobiographique", "roman historique", "roman d'éducation", "roman réaliste", "roman naturaliste","roman de science-fiction", "roman policier", "roman noir","roman du terroir","roman fantastique","roman d'amour")
        self.type_roman_menu.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self, text="Synopsis : ").grid(row=5, column=0, padx=10, pady=10)
        self.synopsis = tk.Entry(self)
        self.synopsis.grid(row=5, column=1, padx=10, pady=10)

        tk.Button(self, text="Ajouter", command=self.ajouter_roman).grid(row=6, column=1, padx=10, pady=10)
        tk.Button(self, text="Fermer", command=self.destroy).grid(row=6, column=2, padx=10, pady=10)

    def ajouter_roman(self):
        nom = self.nom.get()
        auteur = self.auteur.get()
        maison_edition = self.maison_edition.get()
        code_barre = self.code_barre.get()
        type_roman = self.type_roman.get()
        synopsis = self.synopsis.get()

        roman = Roman(nom, auteur, maison_edition, code_barre, type_roman, synopsis)
        romans.append(roman)

        #tk.messagebox.showinfo("Info", "Roman ajouté avec succès!")
        print("Roman ajouté avec succès!")

        for roman in romans:
            roman.afficher_livre()

        self.nom.delete(0,tk.END)
        self.auteur.delete(0,tk.END)
        self.maison_edition.delete(0,tk.END)
        self.code_barre.delete(0,tk.END)
        self.synopsis.delete(0,tk.END)

#menu
def menu() :
    while True:
        print("\n1. Calcul surface sous la courbe")
        print("2. Jeu des allumettes")
        print("3. Les Fichiers")
        print("4. Classe Livre")
        print("5. Classe Roman")
        print("6. Entrer fiche Roman")
        print("7. Quitter")
        choix = input("Entrez votre choix : ")
        if estunnombre(choix):
            choix=int(choix)
            if choix == 1:
                surface_sous_courbe()
            elif choix == 2:
                jeu_allumettes()
            elif choix == 3:
                fichier()
            elif choix == 4:
                livre1 = Livre("Les Misérables", "Victor Hugo", "France Loisirs", "1234567890")
                livre1.afficher_livre()
                livre1.modifier_livre(titre="Le Rouge et le Noir", auteur="Stendhal", edition="Gallimard", barcode="0987654321")
                print("\nLes modifications ont été effectuées :")
                livre1.afficher_livre()
            elif choix == 5:
                roman1 = Roman("Les Misérables", "Victor Hugo", "France Loisirs", "1234567890", "Roman historique", "blabla")
                roman1.afficher_livre()
                roman1.modifier_livre(titre="Le Rouge et le Noir", auteur="Stendhal", edition="Gallimard", barcode="0987654321", genre="Roman réaliste", synopsis="blabla")
                print("\nLes modifications ont été effectuées :")
                roman1.afficher_livre()
            elif choix == 6:
                print("Vérifier, une page s'est ouverte sur votre ordi.")
                if __name__ == "__main__":
                    ui = AjoutRomanUI()
                    ui.mainloop()
            elif choix == 7:
                print("Merci d'avoir participé, au revoir")
                break
            else:
                print("\nErreur, veuillez recommencer en utilisant un nombre de la liste :")

menu()