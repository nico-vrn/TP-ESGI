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

void Exercice2() {
    double x = 0.5;
    unsigned N = 100;

    double suite = Suite(x, N);
    double Ratan = atan(x);

    printf("Suite(%.1f, %u) = %.4f\n", x, N, suite);
    printf("atan(%.1f) = %.4f\n", x, Ratan);
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
		printf("4. Quitter \n");
		scanf("%d", &choix);
		switch (choix)
		{
		case 1:
            
			break;
		case 2:
            Exercice2();
			break;
		case 3:

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
