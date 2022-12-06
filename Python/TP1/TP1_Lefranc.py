import math
import tkinter
from tkinter import *
from math import *

def estunnombre(X):
    if X.isdigit():
        return True
    else:
        print("Entrez un nombre entier") 
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
    print("\nVous allez entrer la longueur des deux bases et la hauteur d'un trapèze et je vais vous donner sa surface puis le dessiner\n")
    while True:
        A = input("Entrez A (en m): ")
        B = input("Entrez B (en m): ")
        C = input("Entrez C (en m): ")
        if estunnombre(A) and estunnombre(B) and estunnombre(C):
            A=int(A)
            B=int(B)
            C=int(C)
            break
    print("La surface est de : ", (A+B)*C/2, "m²")
    dessin(A, B, C)

#fonction qui dessine un trapèze avec tkinter de taille A B et C
def dessin(A,B,C):
    print('\nla définition d\'un trapèze est : Quadrilatère dont deux côtés sont parallèles (surtout lorsqu\'ils sont inégaux). ')
    print("en voici un que j'ai dessiné pour vous : (fermer la fenêtre de dessin pour continuer)")
    fenetre = Tk()
    if A<B:
        width=B*10
        X=(width/2)+B/2
    else :
        width=A*10
        X=(width/2)-A/2
    height=C*10
    canvas = Canvas(fenetre, width=width, height=height, bg='white')
    Y=(height/2)+C
    canvas.pack()
    canvas.create_line(X,Y,X+A,Y,fill='red',width=1)
    canvas.create_line(X+A,Y,X+A,Y-C,fill='red',width=2)
    canvas.create_line(X+A,Y-C,(X+A)-B,Y-C,fill='red',width=2)
    canvas.create_line((X+A)-B,Y-C,X,Y,fill='red',width=2)
    fenetre.mainloop()

#fonction qui demande un entier positif et qui calcul la somme et le factoriel de l'entier
def somme_factoriel() :
    print("\nVous allez entrer un entier positif et je vais vous donner la somme et le factoriel de l'entier\n")
    while True:
        while True:
            entier = input("Entrez un entier positif : ")
            if estunnombre(entier):
                entier=int(entier)
                break
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
                print(i, "*", end=" ")       
        print("Voulez-vous recommencer ? (O/N)")
        reponse = input()
        if reponse == "N" or reponse == "n":
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
    print("\nVous allez entrer un entier et je vais vous donner son logarithme népérien, son sinus et son cosinus\n")
    while True:
        entier = input("Entrez un entier : ")
        if estunnombre(entier):
            entier=int(entier)
            break
    import math
    print("Le logarithme népérien de", entier, "est : ", round(math.log(entier),2))
    print("Le sinus de", entier, "est : ", round(math.sin(entier),2))
    print("Le cosinus de", entier, "est : ", round(math.cos(entier),2))

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

#fonction qui calcul la fonfonction U(n) et V(n) en fonction de n
def U_V(N):
    for i in range(1,N+1):
        if i==1:
            un1=1
        un1=un1+1/factoriel(N)
        print("U(",i,") de",N,"=",round(un1,2))
        uv1=un1+1/(N*factoriel(N))
        print("V(",i,") de",N,"=",round(uv1,2))

#fonction qui permet de calculer ces chance de gagné au tiercé/quarté.. en fonction du nombre de chevaux et du nombre de chevaux joué
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
        print("5. Fonctions mathématiques (logarithme, sinus, cosinus)")
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
                print("\nVous allez entrer un nombre de ligne et un caractère et je vais vous faire un beau sapin\n")
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
                    X = input("\nEntrez X un nombre négatif : ")
                    N = input("Entrez N, un nombre positif : ")
                    if estunnombre(N) and estunnombre(X.lstrip('-')):
                        X=int(X)
                        N=int(N)
                        if X > 0 :
                            print("X doit être inférieur à 0")
                        else :
                            break
                print("RES=",RES(X,N))
            elif choix == 7:
                print("Entrez un nombre entier je vais vous donner les résultats des fonctions U et V")
                while True :
                    N = input("\nEntrez un nombre N, positif: ")
                    if estunnombre(N):
                        N=int(N)
                        break
                U_V(N)
            elif choix == 8:
                print("\nEntrez un nombre entier N correspondant aux nombres de chevaux partants et un nombre entier P correspondant aux nombres de chevaux joués, je vais vous donner les résultats des fonctions tiercé")
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