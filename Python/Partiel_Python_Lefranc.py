#fonction qui vérifie si un nombre donnée est bien un nombre et pas un caractère
def estunnombre(X):
    if X.isdigit():
        return True
    else:
        print("Entrez un nombre entier comme indiqué") 
        return False

#fonction qui demande à l'utilisateur de rentrer un nombre et qui vérifie qu'il est bien un nombre
def entrez_nombre(texte):
    while True:
        print(texte, " : ")
        nombre = input()
        if estunnombre(nombre):
            nombre = int(nombre)
            break
    return nombre

def seuil(P, T):
    n=0
    while P < 1000:
        P *= T
        n += 1
        print("|   ", round(P,2), "   |   ", T, "   |   ", n, "   |")
    return n-1

def exercice1():
    print("Exercice 1 :")
    P = entrez_nombre("Entrez le prix initial de l'article")
    T = float(input("Entrez le prix initial de l'article : "))
    print("|      P      |      T      |      n      |")
    print("Le nombre de mois pour atteindre 1000 est de :", seuil(P, T))

#menu
def menu() :
    while True:
        print("\n1. Exercice 1")
        print("11. Quitter")
        choix = input("Entrez votre choix : ")
        if estunnombre(choix):
            print("\n")
            choix=int(choix)
            if choix == 1:
                exercice1()
            elif choix == 11:
                print("Merci d'avoir participé, au revoir")
                break
            else:
                print("\nErreur, veuillez recommencer en utilisant un nombre de la liste :")

menu()