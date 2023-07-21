#les différentes classes :
class Utilisateur:
    def __init__(self, nom):
        self.nom = nom # Nom de l'utilisateur
        self.articles_empruntes = []  # Liste des articles empruntés par l'utilisateur

class Article:
    def __init__(self, titre, numero):
        self.titre = titre # Titre du livre ou du magazine
        self.numero = numero # Numéro du livre ou du magazine
        self.emprunte = False  # Par défaut, l'article n'est pas emprunté

class Livre(Article):
    def __init__(self, titre, auteur, isbn): 
        super().__init__(titre, isbn)  # Appelle le constructeur de la classe mère 'Article'
        self.auteur = auteur # Auteur du livre  

class Magazine(Article):
    def __init__(self, titre, numero, date_publication):
        super().__init__(titre, numero)  # Appelle le constructeur de la classe mère 'Article'
        self.date_publication = date_publication # Date de publication du magazine

class Bibliotheque: # Classe principale
    def __init__(self):
        self.utilisateurs = []  # Liste des utilisateurs de la bibliothèque
        self.articles = []  # Liste des articles de la bibliothèque

    def ajouter_utilisateur(self, nom): # Ajoute un utilisateur à la bibliothèque
        self.utilisateurs.append(Utilisateur(nom))
        return "Utilisateur créé avec succès."

    def ajouter_livre(self, titre, auteur, isbn): # Ajoute un livre à la bibliothèque
        self.articles.append(Livre(titre, auteur, isbn))
        return "Livre ajouté avec succès."

    def ajouter_magazine(self, titre, numero, date_publication): # Ajoute un magazine à la bibliothèque
        self.articles.append(Magazine(titre, numero, date_publication))
        return "Magazine ajouté avec succès."

    def emprunter_article(self, nom_utilisateur, titre_article): # Emprunte un article
        # Recherche de l'utilisateur et de l'article correspondants
        utilisateur = next((utilisateur for utilisateur in self.utilisateurs if utilisateur.nom == nom_utilisateur), None)
        if utilisateur is None: # Si l'utilisateur n'existe pas
            return "Utilisateur inconnu."
        article = next((article for article in self.articles if article.titre == titre_article), None)
        if article is None or article.emprunte: # Si l'article n'existe pas ou est déjà emprunté
            return "Article non disponible."
        article.emprunte = True
        utilisateur.articles_empruntes.append(article) # Ajoute l'article à la liste des articles empruntés par l'utilisateur
        return "Article emprunté avec succès."

    def rendre_article(self, nom_utilisateur, titre_article): # Rend un article
        # Recherche de l'utilisateur et de l'article correspondants
        utilisateur = next((utilisateur for utilisateur in self.utilisateurs if utilisateur.nom == nom_utilisateur), None)
        if utilisateur is None: # Si l'utilisateur n'existe pas 
            return "Utilisateur inconnu."
        article = next((article for article in utilisateur.articles_empruntes if article.titre == titre_article), None)
        if article is None: # Si l'article n'existe pas
            return "Article non emprunté par l'utilisateur."
        article.emprunte = False
        utilisateur.articles_empruntes.remove(article) # Retire l'article de la liste des articles empruntés par l'utilisateur
        return "Article rendu avec succès."

    def chercher_articles(self, titre_article): 
        # Recherche des articles correspondant au titre
        articles_trouves = [article for article in self.articles if article.titre == titre_article]
        if not articles_trouves: # Si aucun article n'est trouvé
            return "Aucun article trouvé."
        return articles_trouves

    def afficher_articles_empruntes(self, nom_utilisateur): 
        # Affichage des articles empruntés par un utilisateur
        utilisateur = next((utilisateur for utilisateur in self.utilisateurs if utilisateur.nom == nom_utilisateur), None)
        if utilisateur is None: 
            return "Utilisateur inconnu."
        if not utilisateur.articles_empruntes:
            return "Aucun article emprunté."
        return utilisateur.articles_empruntes # Retourne la liste des articles empruntés par l'utilisateur

bibliotheque = Bibliotheque() # Création de la bibliothèque

while True: # Menu
    print("\n1. Ajouter un utilisateur")
    print("2. Ajouter un livre")
    print("3. Ajouter un magazine")
    print("4. Emprunter un article")
    print("5. Rendre un article")
    print("6. Chercher un article par titre")
    print("7. Afficher les articles empruntés par un utilisateur")
    print("8. Afficher tous les articles (triés par titre)")
    print("9. Afficher tous les utilisateurs (triés par nom)")
    print("10. Quitter")

    choix = int(input("Choix: "))
    if choix == 1: # Ajout d'un utilisateur
        nom = input("Nom de l'utilisateur: ")
        print(bibliotheque.ajouter_utilisateur(nom))

    elif choix == 2: # Ajout d'un livre
        titre = input("Titre du livre: ")
        auteur = input("Auteur du livre: ")
        isbn = input("ISBN du livre: ")
        print(bibliotheque.ajouter_livre(titre, auteur, isbn))

    elif choix == 3: # Ajout d'un magazine
        titre = input("Titre du magazine: ")
        numero = input("Numéro du magazine: ")
        date_publication = input("Date de publication du magazine: ")
        print(bibliotheque.ajouter_magazine(titre, numero, date_publication))

    elif choix == 4: # Emprunt d'un article
        nom_utilisateur = input("Nom de l'utilisateur: ")
        titre_article = input("Titre de l'article: ")
        print(bibliotheque.emprunter_article(nom_utilisateur, titre_article))

    elif choix == 5: # Rendu d'un article
        nom_utilisateur = input("Nom de l'utilisateur: ")
        titre_article = input("Titre de l'article: ")
        print(bibliotheque.rendre_article(nom_utilisateur, titre_article))

    elif choix == 6: # Recherche d'un article
        titre_article = input("Titre de l'article: ")
        articles_trouves = bibliotheque.chercher_articles(titre_article)
        if isinstance(articles_trouves, str): # Si aucun article n'est trouvé
            print(articles_trouves)
        else: # Affichage des articles trouvés
            for article in articles_trouves:
                print(f"\nTitre: {article.titre}, Numéro: {article.numero}, Emprunté: {'Oui' if article.emprunte else 'Non'}")

    elif choix == 7: # Affichage des articles empruntés par un utilisateur
        nom_utilisateur = input("Nom de l'utilisateur: ")
        articles_empruntes = bibliotheque.afficher_articles_empruntes(nom_utilisateur)
        if isinstance(articles_empruntes, str): # Si aucun article n'est trouvé
            print(articles_empruntes)
        else: # Affichage des articles empruntés
            for article in articles_empruntes:
                print(f"\nTitre: {article.titre}, Numéro: {article.numero}, Emprunté: {'Oui' if article.emprunte else 'Non'}")

    elif choix == 8: # Affichage de tous les articles
        print("Tous les articles, triés par titre: ")
        for article in sorted(bibliotheque.articles, key=lambda a: a.titre):
            print(f"\nTitre: {article.titre}, Numéro: {article.numero}, Emprunté: {'Oui' if article.emprunte else 'Non'}")

    elif choix == 9: # Affichage de tous les utilisateurs
        print("Tous les utilisateurs, triés par nom: ")
        for utilisateur in sorted(bibliotheque.utilisateurs, key=lambda u: u.nom):
            print(f"Nom: {utilisateur.nom}")

    elif choix == 10: # Quitter
        break
    else: # Choix invalide
        print("Entrée non valide, veuillez essayer à nouveau.")
