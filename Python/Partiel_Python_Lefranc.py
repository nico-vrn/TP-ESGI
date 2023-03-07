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
        print("|    ",end="")
        print(round(P,2), end="")
        print("    |      ", end="")
        print(n, end="")
        print("      |",)
        #print("|   ", round(P,2), "   |   ", T, "   |   ", n, "   |")
    return n-1

def exercice1():
    print("Exercice 1 :")
    P = entrez_nombre("Entrez le prix initial de l'article")
    while True:
        T = input("Entrez taux (nombre à virgule avec un . sous forme 0.1 ou 2.3): ")
        if estunnombre(T.replace(".", "", 1)):
            T = float(T)
            break
        else:
            print("Entrez un nombre décimal comme indiqué")
            continue
    print("|      P      |      N      |")
    print("Le nombre de mois pour atteindre 1000 est de :", seuil(P, T))


def suite(A, B, N):
    U0 = A
    U1 = B
    Un=U1
    Un_1=U0
    for n in range(N):
        Un_1=2/(1/Un_1+1/Un)
        Un=(Un+Un_1)/2.0
        n+=1
        #print("a=",A, "b=",B, "n=",n, "=> suite = (",Un, " , ",Un_1, ")")
    return Un, Un_1

def exercice2():
    print("Exercice 2 :")
    A = entrez_nombre(texte="Entrez la valeur de A")
    B = entrez_nombre(texte="Entrez la valeur de B")
    N = entrez_nombre(texte="Entrez la valeur de N")
    resultat = suite(A, B, N)
    print("La suite final = ", resultat)


class Materiel:
    def __init__(self, nom, nb_serie):
        self.nom = nom
        self.nb_serie = nb_serie
    
    def __str__(self):
        return f"{self.nb_serie} ({self.nom})"

class Clavier(Materiel):
    def __init__(self, nom, nb_serie, nb_touche):
        super().__init__(nom, nb_serie)
        self.nb_touche = nb_touche
    
    def __str__(self):
        return f"Clavier {self.nb_serie} ({self.nom}) - Nombre de touches : {self.nb_touche}"

class Ecran(Materiel):
    def __init__(self, nom, nb_serie, taille_ecran):
        super().__init__(nom, nb_serie)
        self.taille_ecran = taille_ecran
    def __str__(self):
        return f"Ecran {self.nb_serie} ({self.nom}) - Taille : {self.taille_ecran} pouces"

class PC:
    def __init__(self, nb_serie, ecran, clavier):
        self.nb_serie = nb_serie
        self.ecran = ecran
        self.clavier = clavier
    
    def __str__(self):
        return f"PC {self.nb_serie} - {self.ecran} - {self.clavier}"
    
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

    # Création d'un matériel
    print("--------Exemple Matériel--------")
    mat= Materiel("Materiel", "123456")
    print(mat)
    print(mat.nb_serie, mat.nom)
    print("--------------------------------")

    # Création d'un clavier
    print("--------Exemple Clavier--------")
    clavier = Clavier('Clavier', '123456',108)
    print(clavier)
    print(clavier.nb_serie, clavier.nom, clavier.nb_touche)
    print("--------------------------------")

    # Création d'un écran
    print("--------Exemple Ecran--------")
    ecran = Ecran('Ecran', '789012', 27)
    print(ecran)
    print(ecran.nb_serie, ecran.nom, ecran.taille_ecran)
    print("--------------------------------")

    # Création d'un PC avec l'écran et le clavier
    print("--------Exemple PC--------")
    pc = PC('345678', ecran, clavier)
    print(pc)
    print(pc.nb_serie, pc.ecran, pc.clavier)
    print("--------------------------------")

    # Sauvegarde du PC dans un fichier
    pc.sauvegarder('pc.txt')

    # Lecture du PC à partir du fichier
    pc2 = PC.lire('pc.txt')
    print(pc2)
    print(pc2.ecran.taille_ecran)
    print(pc2.clavier.nb_touche)
    print("--------------------------------")

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
                exercice2()
            elif choix == 3:
                exercice3()
            elif choix == 4:
                print("Merci d'avoir participé, au revoir")
                break
            else:
                print("\nErreur, veuillez recommencer en utilisant un nombre de la liste :")

menu()