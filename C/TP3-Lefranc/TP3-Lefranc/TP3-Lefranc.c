#include "TP3-Lefranc.h"

typedef double* PtrTableauDouble;

void TableauDouble_construire(PtrTableauDouble* dd, const unsigned taille) {
    *dd = (PtrTableauDouble) calloc(taille, sizeof(double));
}

void TableauDouble_afficher(const PtrTableauDouble dd, const unsigned taille) {
    if (dd) {
        for (unsigned i = 0; i < taille; i++) {
            printf("%5.10f ", dd[i]);
        }
        printf("\n");
    }
}

void TableauDouble_modifier(PtrTableauDouble dd, const unsigned taille, const unsigned index, const double valeur) {
    if (dd && index < taille) {
        dd[index] = valeur;
    }
}

void TableauDouble_liberer(PtrTableauDouble* dd) {
    if (dd && *dd) {
        free(*dd);
        *dd = NULL;
    }
}

double TableauDouble_get(PtrTableauDouble dd, const unsigned taille, const unsigned index) {
    if (dd && index < taille) {
        return dd[index];
    }
    return 0;
}

void TableauDouble_set(PtrTableauDouble dd, const unsigned taille, const unsigned index, double val) {
    if (dd && index < taille) {
        dd[index] = val;
    }
}

int C_1() {
    PtrTableauDouble d1 = NULL;
    unsigned t1=5;
    TableauDouble_construire(&d1, t1);
    TableauDouble_afficher(d1, t1);
    TableauDouble_modifier(d1, t1, 2, 3.13589985);
    TableauDouble_afficher(d1, t1);
    printf("%5.10f\n", TableauDouble_get(d1, t1, 2));
    TableauDouble_set(d1, t1, 2, 62.1);
    printf("%5.10f\n", TableauDouble_get(d1, t1, 2));
    TableauDouble_afficher(d1, t1);
    TableauDouble_liberer(&d1);
    TableauDouble_afficher(d1, t1);
    return 0;
}

//menu principal
int main()
{
	int choix, n, nb_parties;
	do
	{
		printf("\n \n Choississez votre Fonction a utiliser \n");
		printf("1. Tableau 1 \n");
		printf("2. Tableau  \n");
		printf("3. Livre \n");
		printf("4. Quitter \n");
		scanf("%d", &choix);
		switch (choix)
		{
		case 1:
			C_1();
			break;
		case 2:
            //no
			break;
		case 3:
            //no
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