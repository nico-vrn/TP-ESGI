#include "Partiel_C_Lefranc.h"

double mypow(double x, int n) {
    if (n == 0) {
        return 1;
    } else if (n > 0) {
        return x * mypow(x, n - 1);
    } else {
        return 1 / x * mypow(x, n + 1);
    }
}

double Suite(double x, unsigned N) {
    double U = x;
    double term;
    int n;
    for (n = 1; n <= N; n++) {
        term = mypow(-1, n) * mypow(x, 2*n-1) / (2*n-1);
        U += term;
    }

    return U;
}

void Exercice1() {
    double x = 0.5;
    unsigned N = 100;
    double suite = Suite(x, N);
    double Ratan = atan(x);

    printf("Suite(%.1f, %u) = %.4f\n", x, N, suite);
    printf("atan(%.1f) = %.4f\n", x, Ratan);
}
 

void permuter(ElementTableau *a, ElementTableau *b) {
    ElementTableau tmp = *a;
    *a = *b;
    *b = tmp;
}

void permuter_Tableau(Tableau tab, unsigned size) {
    ElementTableau temp;
    unsigned i;
    for (i = 0; i < size/2; i++) {
        temp = tab[i];
        tab[i] = tab[size-1-i];
        tab[size-1-i] = temp;
    }
}

Tableau creer_Tableau(unsigned size) {
    Tableau tab = malloc(sizeof(ElementTableau) * size);
    if (tab == NULL) {
        printf("Erreur d'allocation de mémoire pour le tableau.\n");
        return NULL;
    }
    unsigned i;
    srand(time(NULL));
    for (i = 0; i < size; i++) {
        tab[i] = (double)rand() / RAND_MAX;
    }

    return tab;
}

void liberer_Tableau(Tableau *tab) {
    free(*tab);
    *tab = NULL;
}

void afficher(const Tableau tab, unsigned size) {
    unsigned i;
    printf("[ ");
    for (i = 0; i < size; i++) {
        printf("%.2f ", tab[i]);
    }
    printf("]\n");
}


void Exercice2() {
    Tableau tab = creer_Tableau(5);

    printf("Tableau au début :\n");
    afficher(tab, 5);
    permuter_Tableau(tab, 5);
    printf("Tableau après permutation :\n");
    afficher(tab, 5);
    liberer_Tableau(&tab);
}


Article* creer_Article() {
    Article* article = malloc(sizeof(Article));
    if (article == NULL) {
        printf("Erreur d'allocation de mémoire pour l'article.\n");
        return NULL;
    }

    printf("Entrez le nom : ");
    fflush(stdin);
    fgets(article->a_nom, sizeof(article->a_nom), stdin);
    article->a_nom[strcspn(article->a_nom, "\n")] = '\0';

    printf("Entrez le prix : ");
    scanf("%f", &article->a_prix);
    getchar();

    printf("Entrez la description : ");
    fflush(stdin);
    fgets(article->a_description, sizeof(article->a_description), stdin);
    article->a_description[strcspn(article->a_description, "\n")] = '\0';

    printf("Entrez le type (0: DIVERS, 1: VETEMENT, 2: NOURRITURE, 3: LIVRE) : ");
    scanf("%d", &article->a_type);
    getchar();

    return article;
}


void afficher_Article(const Article* article) {
    printf("\nAffichage de l'article : \n");
    printf("\nNom : %s\n", article->a_nom);
    printf("Prix : %.2f\n", article->a_prix);
    printf("Description : %s\n", article->a_description);
    printf("Type : ");
    switch (article->a_type) {
        case DIVERS:
            printf("DIVERS\n");
            break;
        case VETEMENT:
            printf("VETEMENT\n");
            break;
        case NOURRITURE:
            printf("NOURRITURE\n");
            break;
        case LIVRE:
            printf("LIVRE\n");
            break;
    }
}

void modifier_Article(Article *article) {
    printf("\nOn modifie l'article : \n");

    printf("Voulez-vous modifier le nom ? (Oui: 1, Non: 0) ");
    int choix;
    scanf("%d", &choix);
    getchar();
    if (choix == 1) {
        printf("Entrez le nom : ");
        fgets(article->a_nom, sizeof(article->a_nom), stdin);
        article->a_nom[strcspn(article->a_nom, "\n")] = '\0';
    }

    printf("Voulez-vous modifier le prix ? (Oui: 1, Non: 0) ");
    scanf("%d", &choix);
    getchar();
    if (choix == 1) {
        printf("Entrez le prix : ");
        scanf("%f", &article->a_prix);
        getchar();
    }

    printf("Voulez-vous modifier la description ? (Oui: 1, Non: 0) ");
    scanf("%d", &choix);
    getchar();
    if (choix == 1) {
        printf("Entrez la description : ");
        fgets(article->a_description, sizeof(article->a_description), stdin);
        article->a_description[strcspn(article->a_description, "\n")] = '\0';
    }

    printf("Voulez-vous modifier le type ? (Oui: 1, Non: 0) ");
    scanf("%d", &choix);
    getchar();
    if (choix == 1) {
        printf("Entrez le type (0: DIVERS, 1: VETEMENT, 2: NOURRITURE, 3: LIVRE) : ");
        scanf("%d", &article->a_type);
        getchar();
    }
}

void liberer_Article(Article* article) {
    free(article);
}

void save_Article(const Article* article, const char* nomFichier) {
    FILE* fichier = fopen(nomFichier, "a");

    if (fichier == NULL) {
        printf("Erreur d'ouverture du fichier.\n");
        return;
    }
    fprintf(fichier, "%s\n", article->a_nom);
    fprintf(fichier, "%.2f\n", article->a_prix);
    fprintf(fichier, "%s\n", article->a_description);
    fprintf(fichier, "%d\n", article->a_type);

    fclose(fichier);
    printf("Article sauvegarde.\n");
}

void load_Article(Article* article, FILE* fichier) {
    printf("\nChargement de l'article...");
    fscanf(fichier, "%s", article->a_nom);
    fscanf(fichier, "%f", &article->a_prix);
    fscanf(fichier, "%s", article->a_description);
    fscanf(fichier, "%d", &article->a_type);
}

#define NB_MAX_ARTICLES 1
int main_Article() {
    Article* tab_Article[NB_MAX_ARTICLES];

    for (int i = 0; i < NB_MAX_ARTICLES; i++) {
        tab_Article[i] = creer_Article();
        afficher_Article(tab_Article[i]);
        modifier_Article(tab_Article[i]);
        afficher_Article(tab_Article[i]);
        save_Article(tab_Article[i], "Article.txt");
    }

    for (int i = 0; i < NB_MAX_ARTICLES; i++) {
        liberer_Article(tab_Article[i]);
    }

    FILE* fichier = fopen("Article.txt", "r");
    for (int i = 0; i < NB_MAX_ARTICLES; i++) {
        load_Article(tab_Article[i], fichier);
        afficher_Article(tab_Article[i]);
    }

    fclose(fichier);

    for (int i = 0; i < NB_MAX_ARTICLES; i++) {
        liberer_Article(tab_Article[i]);
    }

    return 0;
}


//menu principal
int main()
{
	int choix;
	do
	{
		printf("\n \n Choississez votre Fonction a utiliser \n");
        printf("1. Exercice 1 \n");
        printf("2. Exercice 2 \n");
        printf("3. Exercice 3 \n");
		printf("4. Quitter \n");
		scanf("%d", &choix);
		switch (choix)
		{
		case 1:
            Exercice1();
			break;
		case 2:
            Exercice2();
			break;
		case 3:
            main_Article();
            break;
		case 4:
			printf("Au revoir \n");
			break;
		default:
			printf("Choix invalide");
			break;
		}
	} while (choix != 4);
	return 0;
}
