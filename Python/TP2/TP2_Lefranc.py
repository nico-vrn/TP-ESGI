#fonction qui vérifie si un nombre donnée est bien un nombre et pas un caractère
def estunnombre(X):
    if X.isdigit():
        return True
    else:
        print("Entrez un nombre entier comme indiqué") 
        return False



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
                print("hola")
            elif choix == 2:
                print("hola")
            elif choix == 3:
                print("hola")
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