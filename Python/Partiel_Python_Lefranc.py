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


class Materiel:
    def __init__(self, nom, nb_serie):
        self.nom = nom
        self.nb_serie = nb_serie

class Clavier(Materiel):
    def __init__(self, nom, nb_serie, nb_touche):
        super().__init__(nom, nb_serie)
        self.nb_touche = nb_touche

class Ecran(Materiel):
    def __init__(self, nom, nb_serie, taille_ecran):
        super().__init__(nom, nb_serie)
        self.taille_ecran = taille_ecran

class PC:
    def __init__(self, nb_serie, ecran, clavier):
        self.nb_serie = nb_serie
        self.ecran = ecran
        self.clavier = clavier
    
    def sauvegarder(self, fichier):
        with open(fichier, 'w') as f:
            f.write(self.nb_serie + ' ' + self.ecran.nom + ' ' + self.ecran.nb_serie + ' ' + str(self.ecran.taille_ecran) + ' ' + self.clavier.nom + ' ' + self.clavier.nb_serie + ' ' + str(self.clavier.nb_touche))

    
    @staticmethod
    def lire(fichier):
        with open(fichier, 'r') as f:
            ligne = f.readline()
            ligne = ligne.split()
            ecran = Ecran(ligne[1], ligne[2], int(ligne[3]))
            clavier = Clavier(ligne[4], ligne[5], int(ligne[6]))
            return PC(ligne[0], ecran, clavier)

def exercice3():
    print("Exercice 3 :")
    mat= Materiel("Materiel", "123456")
    print(mat.nom)
    # Création d'un clavier
    clavier = Clavier('Clavier', '123456',108)
    print(clavier.nb_touche)

    # Création d'un écran
    ecran = Ecran('Ecran', '789012', 27)
    print(ecran.nom)

    # Création d'un PC avec l'écran et le clavier
    pc = PC('345678', ecran, clavier)

    # Sauvegarde du PC dans un fichier
    pc.sauvegarder('pc.txt')

    # Lecture du PC à partir du fichier
    pc2 = PC.lire('pc.txt')
    print(pc2.ecran.taille_ecran)    # affiche 27
    print(pc2.clavier.nb_touche) # affiche 108

#menu
def menu() :
    while True:
        print("\n1. Exercice 1")
        print("2. Exercice 2")
        print("3. Exercice 3")
        print("4. Quitter")
        choix = input("Entrez votre choix : ")
        if estunnombre(choix):
            print("\n")
            choix=int(choix)
            if choix == 1:
                exercice1()
            elif choix == 2:
                print("Exercice 2 :")
            elif choix == 3:
                exercice3()
            elif choix == 4:
                print("Merci d'avoir participé, au revoir")
                break
            else:
                print("\nErreur, veuillez recommencer en utilisant un nombre de la liste :")

menu()