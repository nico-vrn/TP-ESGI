#fonction qui vérifie si un nombre donnée est bien un nombre et pas un caractère
def estunnombre(X):
    if X.isdigit():
        return True
    else:
        print("Entrez un nombre entier comme indiqué") 
        return False

#fonction qui demande à l'utilisateur de rentrer une chaine de caractère et qui vérifie qu'elle n'est pas vide
def entrez_chaine():
    while True:
        print("Entrer une chaine : ")
        chaine = input()
        if (len(chaine) == 0):
            print("Votre chaine est vide")
        else:
            break
    return chaine

#fonction qui demande à l'utilisateur de rentrer un nombre et qui vérifie qu'il est bien un nombre
def entrez_nombre():
    while True:
        print("Entrer un nombre : ")
        nombre = input()
        if estunnombre(nombre):
            nombre = int(nombre)
            break
    return nombre

#fonction qui inverse une chaine de caractère
def inverser_chaine(chaine):
    return chaine[::-1]

#fonction qui vérifie si une chaine de caractère est en ordre alphabétique
def est_en_ordre_alphabetique(chaine):
    for i in range(len(chaine) - 1):
        if chaine[i] > chaine[i+1]:
            return False
    return True

#fonction qui compte le nombre de mots dans une chaine de caractère
def nb_mot(chaine):
    return len(chaine.split(' '))

#fonction qui compte le nombre de majuscules et de minuscules dans une chaine de caractère
def nb_maj_min(chaine):
    maj = 0
    min = 0
    for i in range(len(chaine)):
        if chaine[i].isupper():
            maj += 1
        elif chaine[i].islower():
            min += 1
    return maj, min

#fonction qui supprime les caractères spéciaux d'une chaine de caractère
def suppr_caracteres_speciaux(chaine):
    resultat = ""
    for caractere_nrml in chaine:
        if caractere_nrml.isalnum() or caractere_nrml.isspace():
            resultat += caractere_nrml
    return resultat

#fonction qui répète les caractères d'une chaine de caractère
def repeter_caractere(chaine,nb):
    resultat = ""
    for caractere in chaine:
        resultat += caractere * nb
    return resultat

#fonction qui calcule la somme des nombres impairs inférieurs à nb
def somme_nb_impairs(nb):
    somme = 0
    for i in range(1, nb+1, 2):
        somme += i
    return somme

#fonction qui trouve tous les nombres pairs de 1 à nb
def nb_pairs(nb):
    liste_pairs = []
    for i in range(1, nb+1):
        if i%2 == 0:
            liste_pairs.append(i)
    return liste_pairs

#Fonction qui vérifie si un nombre est un palindrome
def est_palindrome(nb):
    nb = str(nb)
    if nb == nb[::-1]:
        return True
    else:
        return False

#fonction qui compte la distance de hamming entre 2 chaines de même taille passés en paramètres
def distance_hamming(chaine1, chaine2):
    if len(chaine1) != len(chaine2):
        print("Les deux chaînes doivent avoir la même longueur !")
        return
    distance = 0
    for i in range(len(chaine1)):
        if chaine1[i] != chaine2[i]:
            distance += 1
    return distance

#menu
def menu() :
    while True:
        print("\n1. Inverser une chaine")
        print("2. Chaine en ordre alphabétique ?")
        print("3. Nombre de mots")
        print("4. Nombre de majuscules et minuscules")
        print("5. Supprimer les caractères spéciaux")
        print("6. Répéter les caractères")
        print("7. Somme des nombres impairs inférieurs à X")
        print("8. Liste des nombres pairs inférieurs à X")
        print("9. Vérifier si un nombre est un palindrome")
        print("10. Calcul distance de Hamming")
        print("11. Quitter")
        choix = input("Entrez votre choix : ")
        if estunnombre(choix):
            print("\n")
            choix=int(choix)
            if choix == 1:
                print("Fonction qui inverse une chaine de caractère :")
                print("votre chaine à l'envers : ", inverser_chaine(entrez_chaine()))
            elif choix == 2:
                print("Fonction qui vérifie si une chaine de caractère est en ordre alphabétique :")
                if (est_en_ordre_alphabetique(entrez_chaine())):
                    print("Votre chaine est en ordre alphabétique")
                else:
                    print("Votre chaine n'est pas en ordre alphabétique")
            elif choix == 3:
                print("FOnction qui compte le nombre de mots dans une chaine de caractère :")
                print("Votre chaine contient ", nb_mot(entrez_chaine()), " mots")
            elif choix == 4:
                print("Fonction qui compte le nombre de majuscules et de minuscules dans une chaine de caractère :")
                maj, min = nb_maj_min(entrez_chaine())
                print("Votre chaine contient ", maj, " majuscules et ", min, " minuscules")
            elif choix == 5:
                print("Fonction qui supprime les caractères spéciaux d'une chaine de caractère :")
                print("Votre chaine sans caractères spéciaux de 1 façon : ", suppr_caracteres_speciaux(entrez_chaine()))
            elif choix == 6:
                print("Fonction qui répète les caractères d'une chaine de caractère :")
                print("Votre chaine avec les caractères répétés : ", repeter_caractere(entrez_chaine(), int(input("Entrez le nombre de répétition : "))))
            elif choix == 7:
                print('Fonction qui calcule la somme des nombres impairs inférieurs à X :')
                X=entrez_nombre()
                print("La somme des nombres impairs inférieurs à ", X, " est : ", somme_nb_impairs(X))
            elif choix == 8:
                print('Fonction qui trouve tous les nombres pairs de 1 à X :')
                X=entrez_nombre()
                print("La liste des nombres pairs inférieurs à ", X, " est : ", nb_pairs(X))
            elif choix == 9:
                print("Fonction qui vérifie si un nombre est un palindrome :")
                X=entrez_nombre()
                if est_palindrome(X):
                    print(X, " est un palindrome")
                else:
                    print(X, " n'est pas un palindrome")
            elif choix == 10:
                print("Fonction qui calcule la distance de Hamming entre 2 chaines de même taille :")
                print("Il va vous être demandé de rentrer deux chaines de même longueur")
                chaine1 = entrez_chaine()
                chaine2 = entrez_chaine()
                print("La distance de Hamming entre ", chaine1, " et ", chaine2, " est : ", distance_hamming(chaine1, chaine2))
                if (distance_hamming(chaine1, chaine2)==0):
                    print('Ces deux chaines sont identiques')
            elif choix == 11:
                print("Merci d'avoir participé, au revoir")
                break
            else:
                print("\nErreur, veuillez recommencer en utilisant un nombre de la liste :")

menu()