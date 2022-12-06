#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <math.h>
#include "TP2-Lefranc.h"

//fonction qui demande 3 chiffre A B et C et résoud cette équation : Ax2 + Bx + C = 0
void equation()
{
    float a, b, c, delta, x1, x2;
    printf("Resoudre l’equation du second degre : Ax2 + Bx + C = 0 \n");
    printf("Entrez A :");
    scanf("%f", &a);
    printf("Entrez B :");
    scanf("%f", &b);
    printf("Entrez C :");
    scanf("%f", &c);
    delta = b*b - 4*a*c;
    if (delta < 0)
    {
        printf("Pas de solution dans R");
    }
    else if (delta == 0)
    {
        x1 = -b/(2*a);
        printf("x = %f", x1);
    }
    else
    {
        x1 = (-b + sqrt(delta))/(2*a);
        x2 = (-b - sqrt(delta))/(2*a);
        printf("l'equation admet 2 solutions qui sont : \n -x1 = %f \n -x2 = %f", x1, x2);
    }
}

//fonction qui calcul la suite défini par u0=2 un+1=1/2(un+2/un) qui demande N puis affiche toutes les dixaine jusqu'a N, le résultat de U[N] et ce vers quoi la suite tant que N est positif
void suite()
{
    int n, i;
    float u0=2, un, un1;
    printf("Calcul de la suite definie par u0=2 un+1=1/2(un+2/un) \n");
    printf("Entrez N :");
    scanf("%d", &n);
    printf("U[0] = %.2f \n", u0);
    un = u0;
    for (i = 1; i <= n-1; i++)
    {
        un1 = 0.5*(un+2/un);
        un = un1;
        if (i%10 == 0)
        {
            printf("u[%d] = %.2f \n", i, un);
        }
    }
    printf("Le resultat de U[%d] = %.2f \n", n, un);
    if (un > 0)
    {
        printf("La suite tend vers l'infini");
    }
    else if (un < 0)
    {
        printf("La suite tend vers -l'infini");
    }
    else
    {
        printf("La suite tend vers 0");
    }
}

//fonction qui calcule le nombre de Fibonacci d'un nombre N
int fibonacci(int n)
{
    int i;
    long int f0=0, f1=1, fn;
    if (n == 0)
    {
        fn=f0;
    }
    else if (n == 1)
    {
        fn=f1;
    }
    else
    {
        for (i = 0; i <= n-2; i++)
        {
            fn = f0 + f1;
            f0 = f1;
            f1 = fn;
        }
    }
    return fn;
}

//fonction qui demande un nombre N puis affiche fibonacci(n+1)/fibonacci(N) affiche toutes les cinq jusqu'a N puis le résultat de O[N]
void nb_or()
{
    int n, i;
    float fn, fn1, fn2, on;
    printf("Calcul de la suite definie par O[n]=F[n+1]/F[n] \n");
    printf("Entrez N :");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        fn = fibonacci(i);
        fn1 = fibonacci(i+1);
        on = fn1/fn;
        if (i == 1)
        {
            printf("O[%d] = %.2f \n", i, on);
        }
        if (i%5 == 0)
        {
            printf("O[%d] = %.2f \n", i, on);
        }
    }
    printf("Le resultat de O[%d] = %.2f \n", n, on);
    printf("Le nombre d'or est egal a %f", on);
}


//--------Separation--------//


bool in(short value, short *array, short size){
    for (int i = 0; i < size; i++){
        if (array[i] == value) return true;
    }
    return false;
}

bool all_in(short *list, short *array, short size){
    for (int i = 0; i < size; i++){
        if (!in(list[i], array, size)) return false;
    }
    return true;
}

short roll_dice(){
    short value = rand() % 6 + 1;
    return value;
}

void display_gotten_numbers(short *list, int size){
    printf("[");    
    for (short i = 0; i < size; i++){
        if (list[i] != -1){
            printf("%d", list[i]);
            if (i < size - 2) printf(", ");
        }
    }
    printf("]\n");
}

void keep(short list[], short size){
    printf("Je garde ");
    for(short i = 0; i < size; i++){
        if (list[i] != -1){
            printf("%d ", list[i]);
            if (i < size - 2) printf("et ");
        }
    }

}

void dice(){

    // Déclaration des variables
    short dices[3];
    short value_we_need[3] = {1, 2, 4};
    short value_gotten[3] = {-1, -1, -1};
    short index_value_gotten = 0;

    short nb_games;
    short nb_wins = 0, nb_loses = 0;
    short nb_dice = 3;
    
    printf("Entrez le nombre de parties : ");
    scanf("%hd", &nb_games);


    // Boucle de jeu sur le nombre de parties
    for (short i = 0; i < nb_games; i++){

        // Boucle sur 3 lancer de dés
        for(short r = 0; r < 3; r++){

            // Ajout de la valeur obtenue dans le tableau de dés
            for (short j = 0; j < nb_dice; j++) dices[j] = roll_dice();

            printf("Lancer %d avec %d des : ", r+1, nb_dice);

            // Affichage des valeurs obtenues
            for (short j = 0; j < 3; j++){
                printf("%d ", dices[j]);
            }

            // Si aucun des dés n'a les valeurs recherchée
            if (!in(1, dices, nb_dice) && !in(2, dices, nb_dice) && !in(4, dices, nb_dice)){
                printf("Je ne garde rien ");
                display_gotten_numbers(value_gotten, 3);
            }
            else {
                for (short j = 0; j < 3; j++){
                    // Si la valeur recherchée est présente dans le tableau de dés et qu'elle n'a pas déjà été obtenue
                    if (in(value_we_need[j], dices, nb_dice) && !in(value_we_need[j], value_gotten, 3)){
                        value_gotten[index_value_gotten] = value_we_need[j];
                        index_value_gotten++;
                    }
                }
                keep(value_gotten, nb_dice);
                nb_dice -= index_value_gotten;
                display_gotten_numbers(value_gotten, 3);
            }

            // Si toute les valeurs recherchées sont présentes dans le tableau des valeurs obtenues
            if (all_in(value_we_need, value_gotten, 3)) {
                printf("Partie %d gagnee en %d coups", i+1, r+1);
                nb_wins++;
                break;
            }
            else if (r == 2){
                printf("Partie %d perdue", i+1);
                nb_loses++;
            } 
        }

        // Réinitialisation des variables
        printf("\n\n\n");
        nb_dice = 3;
        index_value_gotten = 0;
        for (short j = 0; j < 3; j++) value_gotten[j] = -1;
    }

    printf("Vous avez joue %d parties, %d gagnees et %d perdue(s) soit %.2f%% de gain\n", nb_games, nb_wins, nb_loses, (float)nb_wins / nb_games * 100);

}


//--------Separation--------//


int main()
{
	int choix, n;
	do
	{
		printf("\n \n Choississez votre Fonction a utiliser \n");
		printf("1. equation \n");
		printf("2. Suite \n");
		printf("3. Fibonacci \n");
		printf("4. nombre d'or et fibonacci \n");
		printf("5. Jeu de des \n");
		printf("6. Quitter \n");
		printf("Entrer votre choix : ");
		scanf("%d", &choix);
		switch (choix)
		{
		case 1:
			equation();
			break;
		case 2:
			suite();
			break;
		case 3:
            printf("Calcul du nombre de Fibonacci d'un nombre N \n");
            printf("Entrez la valeur de n : ");
            scanf("%d", &n);
            printf("Le nombre de Fibonacci de %d est %d : F[%d] = %d", n,fibonacci(n),n,fibonacci(n));
			break;
		case 4:
			nb_or();
			break;
		case 5:
            //lancer();
            dice();
			break;
		case 8:
			printf("Au revoir \n");
			break;
		default:
			printf("Choix invalide");
			break;
		}
	} while (choix != 8);
	return 0;
}

