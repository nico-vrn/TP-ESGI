#include "TP3-Lefranc.h"
#include <stdio.h>
#include <stdlib.h>

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


typedef struct {
    double* array;
    unsigned int size;
} DoubleArray;
typedef DoubleArray* PtrDoubleArray;

void construct_double_array(PtrDoubleArray* da,unsigned sz) {
    *da = (PtrDoubleArray) malloc(sizeof(DoubleArray));
    (*da)->array = (double*) calloc(sz, sizeof(double));
    (*da)->size = sz;
}

void print_double_array(const PtrDoubleArray da) {
    if (da && da->array) {
        for (unsigned i = 0; i < da->size; i++) {
            printf("%5.10f ", da->array[i]);
        }
        printf("\n");
    }
}

void modify_double_array(PtrDoubleArray da, const unsigned idx, const double val) {
    if (da && da->array && idx < da->size) {
        da->array[idx] = val;
    }
}

void free_double_array(PtrDoubleArray* da) {
    if (da && *da) {
        free((*da)->array);
        free(*da);
        *da = NULL;
    }
}

double get_value_double_array(PtrDoubleArray da, const unsigned idx) {
    if (da && da->array && idx < da->size) {
        return da->array[idx];
    }
    return 0;
}

void set_value_double_array(PtrDoubleArray da, const unsigned idx, double val) {
    if (da && da->array && idx < da->size) {
        da->array[idx] = val;
    }
}

void C_2() {
    PtrDoubleArray data = NULL;
    unsigned size=5;
    construct_double_array(&data, size);
    print_double_array(data);
    modify_double_array(data, 2, 3.13589985);
    print_double_array(data);
    printf("%5.10f\n", get_value_double_array(data, 2));
    set_value_double_array(data, 2, 62.1);
    printf("%5.10f\n", get_value_double_array(data, 2));
    print_double_array(data);
    free_double_array(&data);
    print_double_array(data);
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
            C_2();
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