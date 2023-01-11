import random

#fonction qui vérifie si un nombre donnée est bien un nombre et pas un caractère
def estunnombre(X):
    if X.isdigit():
        return True
    else:
        print("Entrez un nombre entier comme indiqué") 
        return False

def surface_sous_courbe():
    print("Vous allez entrez 2 nombre réel et un nombre à virgule et je vais vous donner l'intégral de la fonction y=x*x")
    a = input("Entrez A: ")
    b = input("Entrez B: ")
    p = input("Entrez P: ")
    if estunnombre(a) and estunnombre(b) and estunnombre(p):
        a = int(a)
        b = int(b)
        p = int(p)
    p=float(p)
    U0=int(a)*int(a)*p
    S=U0
    n=1
    while(int(a)+p*int(n)<int(b)):
        U0=(int(a)+p*n)*(int(a)+p*n)*p
        S=S+U0
        n=n+1
    print("Calcul de l'intégrale de la fonction y=x*x avec ",a, "<= x <", b, " et p =", p)
    print("La surface sous la courbe est de : ",S)

def jeu_allumettes():
    nom= input("Entrez votre nom : ")
    print("Bienvenue ",nom," dans le jeu des allumettes")
    print("Vous allez jouer contre l'ordinateur")
    nb_allumettes= input("Choisir le nombre d'allumettes de départ:")
    print("Vous allez pouvoir enlever 1,2 ou 3 allumettes")
    if estunnombre(nb_allumettes):
        nb_allumettes=int(nb_allumettes)
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
    num1=int(input("Entrez un nombre entier : "))
    num2=int(input("Entrez un nombre entier : "))
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
                print("hola")
            elif choix == 5:
                print("hola")
            elif choix == 6:
                print("hola")
            elif choix == 7:
                print("Merci d'avoir participé, au revoir")
                break
            else:
                print("\nErreur, veuillez recommencer en utilisant un nombre de la liste :")

menu()