#include <stdio.h>
#include <math.h>

// Fonction pour calculer l'hypoténuse
double calculer_hypotenuse(double a, double b) {
    return sqrt(a*a + b*b);
}

int main() {
    double a, b;

    printf("Veuillez entrer le premier cote: ");
    scanf("%lf", &a); 

    printf("Veuillez entrer le deuxième cote: ");
    scanf("%lf", &b); 

    double hypotenuse = calculer_hypotenuse(a, b);

    printf("L'hypoténuse du triangle est: %.2lf\n", hypotenuse);

    return 0;
}
