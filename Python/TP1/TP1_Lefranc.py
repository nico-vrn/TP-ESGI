import turtle

def estunnombre(X):
    if X.isdigit():
        return True
    else:
        print("Entrez un nombre entier positif") 
        return False

#fonction qui donne le code ASCII d'un caractère et inversement
def ASCII () :
    print("\nVous allez entrer un caractère et un nombre entier et je vais vous donner le code ASCII du caractère et le caractère correspondant au nombre entier")
    while True:
        caractere = input("\nEntrez un caractère : ")
        while True:
            entier = input("Entrez un entier: ")
            if estunnombre(entier):
                entier=int(entier)
                break
        print("Le caractère", caractere, " en hexadécimal est : ", ord(caractere))
        print("L'entier", entier, "en hexadécimal est : ", chr(entier))
        print("Voulez-vous recommencer ? (O/N)")
        reponse = input()
        if reponse == "N" or reponse == "n":
            break
    print("Merci a bientôt")

#fonction qui calcule la surface d'un trapèze
def calcul_surface() :
    print("\nVous allez entrer la longueur des deux bases et la hauteur d'un trapèze et je vais vous donner sa surface\n")
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
        #print("factoriel de", n,"=",n * factoriel(n-1))
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

def U_V(N):
    for i in range(1,N+1):
        if i==1:
            un1=1
        un1=un1+1/factoriel(N)
        print("U(",i,") de",N,"=",round(un1,2))
        uv1=un1+1/(N*factoriel(N))
        print("V(",i,") de",N,"=",round(uv1,2))

def tierce(N,P):
    X=factoriel(N)/(factoriel(N-P))
    Y=factoriel(N)/(factoriel(P)*(factoriel(N-P)))
    print("Dans l'ordre: une chance sur",X,"de gagner")
    print("Dans le désordre: une chance sur",Y,"de gagner")

#menu
def menu() :
    while True:
        print("\n1. Convertisseur ASCII")
        print("2. Calcul de surface")
        print("3. Somme et factoriel")
        print("4. Arbre de noël")
        print("5. Fonctions mathématiques")
        print("6. Fonctions")
        print("7. fonctions U et V")
        print("8. Tiercé")
        print("9. Quitter")
        choix = input("Entrez votre choix : ")
        if estunnombre(choix):
            choix=int(choix)
            if choix == 1:
                ASCII()
            elif choix == 2:
                calcul_surface()
            elif choix == 3:
                somme_factoriel()
            elif choix == 4:
                while True:
                    nombre = input("Entrez le nombre de ligne (nombre positif) : ")
                    if estunnombre(nombre):
                        nombre=int(nombre)
                        if nombre>0:
                            break
                caractere = input("Entrez le caractère : ")
                arbre_noel(nombre,caractere)
            elif choix == 5:
                math()
            elif choix == 6:
                while True :
                    #demadner input d'un nombre négatif de l'UserWarning(
                    X = input("\nEntrez X un nombre négatif : ")
                    N = input("Entrez N, un nombre positif : ")
                    if estunnombre(N):
                        X=int(X)
                        N=int(N)
                        if X > 0 :
                            print("X doit être inférieur à 0")
                        else :
                            break
                print("RES=",RES(X,N))
            elif choix == 7:
                while True :
                    N = input("\nEntrez un nombre N, positif: ")
                    if estunnombre(N):
                        N=int(N)
                        break
                U_V(N)
            elif choix == 8:
                while True :
                    N = input("\nEntrez le nombre de chevaux partants (nombre positif): ")
                    P = input("Entrez le nombre de chevaux joués (nombre positif): ")
                    if estunnombre(N) and estunnombre(P):
                        N=int(N)
                        P=int(P)
                        break
                tierce(N,P)
            elif choix == 9:
                print("Merci d'avoir participé, au revoir")
                break
            else:
                print("\nErreur, veuillez recommencer en utilisant un nombre de la liste :")

menu()