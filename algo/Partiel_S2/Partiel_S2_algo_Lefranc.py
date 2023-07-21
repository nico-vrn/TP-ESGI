class Article:
    def __init__(self, titre):
        self.titre = titre
        self.est_emprunte = False

class Livre(Article):
    def __init__(self, titre, auteur, isbn):
        super().__init__(titre)
        self.auteur = auteur
        self.isbn = isbn

class Magazine(Article):
    def __init__(self, titre, numero, date_publication):
        super().__init__(titre)
        self.numero = numero
        self.date_publication = date_publication

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.articles_empruntes = []

class Bibliotheque:
    def __init__(self):
        self.articles = []
        self.utilisateurs = []

    def ajouter_article(self, article):
        self.articles.append(article)

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def emprunter_article(self, nom_utilisateur, titre_article):
        utilisateur = next((utilisateur for utilisateur in self.utilisateurs if utilisateur.nom == nom_utilisateur), None)
        article = next((article for article in self.articles if article.titre == titre_article), None)

        if utilisateur is None:
            return "Utilisateur non existant."
        elif article is None:
            return "Article non existant."
        elif article.est_emprunte:
            return "Article déjà emprunté."
        else:
            utilisateur.articles_empruntes.append(article)
            article.est_emprunte = True
            return "Article emprunté avec succès."

    def rendre_article(self, nom_utilisateur, titre_article):
        utilisateur = next((utilisateur for utilisateur in self.utilisateurs if utilisateur.nom == nom_utilisateur), None)
        article = next((article for article in self.articles if article.titre == titre_article), None)

        if utilisateur is None:
            return "Utilisateur non existant."
        elif article is None:
            return "Article non existant."
        elif article not in utilisateur.articles_empruntes:
            return "Cet article n'a pas été emprunté par cet utilisateur."
        else:
            utilisateur.articles_empruntes.remove(article)
            article.est_emprunte = False
            return "Article rendu avec succès."

    def chercher_articles(self, titre_ou_auteur):
        resultats = [article for article in self.articles if article.titre == titre_ou_auteur or (isinstance(article, Livre) and article.auteur == titre_ou_auteur)]
        return resultats

    def obtenir_articles_empruntes(self, nom_utilisateur):
        utilisateur = next((utilisateur for utilisateur in self.utilisateurs if utilisateur.nom == nom_utilisateur), None)
        if utilisateur:
            return utilisateur.articles_empruntes
        else:
            return None

# On initialise la bibliothèque
bibliotheque = Bibliotheque()

while True:
    print("\n--- Menu ---")
    print("1. Ajouter un utilisateur")
    print("2. Ajouter un livre")
    print("3. Ajouter un magazine")
    print("4. Emprunter un article")
    print("5. Rendre un article")
    print("6. Chercher des livres/magazines par titre ou auteur")
    print("7. Afficher les articles empruntés par un utilisateur")
    print("8. Afficher tous les articles (triés par titre)")
    print("9. Afficher tous les utilisateurs (triés par nom)")
    print("10. Quitter")

    try:
        choix = int(input("Choisissez une option: "))
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre correspondant à une des options.")
        continue

    if choix == 1:
        nom = input("Nom de l'utilisateur: ")
        if nom == "":
            print("Le nom est obligatoire.")
            continue
        bibliotheque.ajouter_utilisateur(Utilisateur(nom))
        print("Utilisateur ajouté avec succès.")

    elif choix == 2:
        titre = input("Titre du livre: ")
        auteur = input("Auteur du livre: ")
        isbn = input("ISBN du livre: ")
        if titre == "" or auteur == "" or isbn == "":
            print("Tous les champs sont obligatoires.")
            continue
        bibliotheque.ajouter_article(Livre(titre, auteur, isbn))
        print("Livre ajouté avec succès.")

    elif choix == 3:
        titre = input("Titre du magazine: ")
        numero = input("Numéro du magazine: ")
        date_publication = input("Date de publication du magazine (YYYY-MM-DD): ")
        if titre == "" or numero == "" or date_publication == "":
            print("Tous les champs sont obligatoires.")
            continue
        bibliotheque.ajouter_article(Magazine(titre, numero, date_publication))
        print("Magazine ajouté avec succès.")

    elif choix == 4:
        nom_utilisateur = input("Nom de l'utilisateur: ")
        titre_article = input("Titre de l'article: ")
        print(bibliotheque.emprunter_article(nom_utilisateur, titre_article))

    elif choix == 5:
        nom_utilisateur = input("Nom de l'utilisateur: ")
        titre_article = input("Titre de l'article: ")
        print(bibliotheque.rendre_article(nom_utilisateur, titre_article))

    elif choix == 6:
        titre_ou_auteur = input("Titre ou auteur de l'article: ")
        articles_trouves = bibliotheque.chercher_articles(titre_ou_auteur)
        if articles_trouves:
            print("Articles trouvés :")
            for article in articles_trouves:
                if isinstance(article, Livre):
                    print("Livre: {} par {}. ISBN: {}. {}".format(article.titre, article.auteur, article.isbn, "Emprunté" if article.est_emprunte else "Disponible"))
                else:
                    print("Magazine: {}, numéro {}, date de publication: {}. {}".format(article.titre, article.numero, article.date_publication, "Emprunté" if article.est_emprunte else "Disponible"))
        else:
            print("Aucun article correspondant trouvé.")

    elif choix == 7:
        nom_utilisateur = input("Nom de l'utilisateur: ")
        articles_empruntes = bibliotheque.obtenir_articles_empruntes(nom_utilisateur)
        if articles_empruntes is None:
            print("Utilisateur non existant.")
            continue
        elif not articles_empruntes:
            print("{} n'a emprunté aucun article.".format(nom_utilisateur))
            continue
        print("Articles empruntés par {}: ".format(nom_utilisateur))
        for article in articles_empruntes:
            print(article.titre)

    elif choix == 8:
        print("Tous les articles, triés par titre: ")
        for article in sorted(bibliotheque.articles, key=lambda a: a.titre):
            print(article.titre)

    elif choix == 9:
        print("Tous les utilisateurs, triés par nom: ")
        for utilisateur in sorted(bibliotheque.utilisateurs, key=lambda u: u.nom):
            print(utilisateur.nom)

    elif choix == 10:
        print("Au revoir !")
        break
