import turtle

#fonction qui donne le code ASCII d'un caractère et inversement
def ASCII () :
    while True:
        caractere = input("Entrez un caractère : ")
        entier = int(input("Entrez un entier: "))
        print("Le caractère", caractere, " en hexadécimal est : ", ord(caractere))
        print("L'entier", entier, "en hexadécimal est : ", chr(entier))
        print("Voulez-vous recommencer ? (O/N)")
        reponse = input()
        if reponse == "N" | reponse == "n":
            break
    print("Merci a bientôt")

#fonction qui calcule la surface d'un trapèze
def calcul_surface() :
    A = int(input("Entrez A (en m): "))
    B = int(input("Entrez B (en m): "))
    C = int(input("Entrez C (en m): "))
    print("La surface est de : ", (A+B)*C/2, "m²")

#fonction qui demande un entier positif et qui calcul la somme et le factoriel de l'entier
def somme_factoriel() :
    while True:
        entier = int(input("Entrez un entier positif : "))
        somme = 0
        factoriel = 1
        for i in range(1, entier+1):
            somme += i
            if i==entier :
                print(i, "=", somme)
            else:
                print(i, "+", end=" ")

        print(somme,' = ', end=" ")
        somme=0

        for i in range(1, entier+1):
            somme += i
            if i==entier :
                print(i, "\n")
            else:
                print(i, "+", end=" ")

        for i in range(1, entier+1):
            factoriel *= i
            if i==entier :
                print(i,"=", factoriel)
            else:
                print(i, "*", end=" ") 
        print(factoriel,' = ', end=" ")
        factoriel=1

        for i in range(1, entier+1):
            factoriel += i
            if i==entier :
                print(i)
            else:
                print(i, "+", end=" ")       
        print("Voulez-vous recommencer ? (O/N)")
        reponse = input()
        if reponse == "N" | reponse == "n":
            break
    print("Merci a bientôt")

#fonction qui fais un sapin du nombre de ligne et de caractère saisie par l'utilisateur
def arbre_noel(nombre,caractere) :
    for i in range(1, nombre+1):
        for j in range(1, nombre-i+1):
            print("=", end="")
        for j in range(1, i+1):
            print(caractere, end="")
        for j in range(1, i):
            print(caractere, end="")
        print("")
        i=1
    while (i<=nombre-1):
        print("=", end="")
        i+=1
    print(caractere)
    i=2
    while (i<=nombre-1):
        print("=", end="")
        i+=1
    for h in range (0,3):
        print(caractere, end="")
    print("\n************* Joyeux Noel *************")

#fonction qui demande un entier puis afficher son logarithme népérien, son sinus et son cosinus
def math() :
    entier = int(input("Entrez un entier : "))
    import math
    print("Le logarithme népérien de", entier, "est : ", math.log(entier))
    print("Le sinus de", entier, "est : ", math.sin(entier))
    print("Le cosinus de", entier, "est : ", math.cos(entier))

#fonction qui calcul le factoriel d'un nombre en paramètre
def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)

#fonction qui fait F1=x^N/factoriel(N)
def F1(X,N):
    f1=(X**N)/(factoriel(N))
    #print("factoriel de",N,"est : ",factoriel(N))
    return f1

def RES(X,N):
    res=0
    for i in range(1,N+1):
        #print("i=",i)
        res+=F1(X,i)
        #print("F1 de",X,"et",i,"est : ",F1(X,i))
    return res

#menu
def menu() :
    while True:
        print("\n1. Convertisseur ASCII")
        print("2. Calcul de surface")
        print("3. Somme et factoriel")
        print("4. Arbre de noël")
        print("5. Fonctions mathématiques")
        print("6. Fonctions")
        print("7. Quitter")
        choix = int(input("Entrez votre choix : "))
        if choix == 1:
            ASCII()
        elif choix == 2:
            calcul_surface()
        elif choix == 3:
            somme_factoriel()
        elif choix == 4:
            nombre = int(input("Entrez le nombre de lignes : "))
            caractere = input("Entrez le caractère : ")
            arbre_noel(nombre,caractere)
        elif choix == 5:
            math()
        elif choix == 6:
            while True :
                #demadner input d'un nombre négatif de l'UserWarning(
                X = int(input("Entrez X un nombre négatif : "))
                N = int(input("Entrez N, un nombre positif : "))
                if X > 0 :
                    print("X doit être inférieur à 0")
                elif N < 0 :
                    print("N doit être supérieur à 0")
                else :
                    break
            print("RES=",RES(X,N))
        elif choix == 7:
            print("Au revoir")
            break
        else:
            print("Erreur, veuillez recommencer")

menu()