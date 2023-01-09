#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
//#include "TP2-Lefranc.h"

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

int nb=3;
int tab_des[2];
int tab_bon[2]={0,0,0};

void lancer_des(nb)
{
    int i, des; 
    for (i = 0; i <= nb; i++)
    {
        des = rand()%6+1;
        //printf("Le des %d est egal a %d \n", i, des);
        tab_des[i] = des;
        //printf("tab_des[%d] = %d \n", i, tab_des[i]);
    }
    printf("votre lancer est : %d, %d et %d \n", tab_des[0], tab_des[1], tab_des[2]);
}

//fonction qui vérifie pour chaque case du tableau si il contient un 4 un 2 ou un 1
void jeu_des(nb_parties)
{
    printf("\nBienvenue dans le jeu des des !\n");
    printf("Il va falloir obtenir 421 pour gagner en moins de 3 lancers. \n");

    int parties=0;
    srand(time(NULL));
    for(int f=0;f<nb_parties;f++){
        int j=0;
        while (j<3){
            printf("\n\nLancer numero %d, partie numero %d :\n", j+1, f+1);
            lancer_des(nb);
            int i;
            for (i = 0; i <= nb; i++)
            {
                if (tab_des[i] == 4)
                {
                    printf("Le des %d est egal a 4, ", i);
                    if (tab_bon[0]!=4){
                        tab_bon[0]=4;
                        nb-=1;
                        printf("top je garde ! \n");
                    }
                    else{
                        printf(" mais il est deja sorti .. \n");
                    }
                }
                else if (tab_des[i] == 2)
                {
                    printf("Le des %d est egal a 2, ", i);
                    if (tab_bon[1]!=2){
                        tab_bon[1]=2;
                        nb-=1;
                        printf("top je garde ! \n");
                    }
                    else{
                        printf(" mais il est deja sorti .. \n");
                    }
                }
                else if (tab_des[i] == 1)
                {
                    printf("Le des %d est egal a 1, ", i);
                    if (tab_bon[2]!=1){
                        tab_bon[2]=1;
                        nb-=1;
                        printf("top je garde ! \n");
                    }
                    else{
                        printf(" mais il est deja sorti .. \n");
                    }
                }
                tab_des[i]=0;
            }
            printf("Il vous reste %d des \n", nb);
            //printf("tab_des= %d %d %d \n", tab_des[0], tab_des[1], tab_des[2]);
            j++;
            printf("Des gardes : ");
            if(tab_bon[0]==4){
                printf("4 ");
            }
            if(tab_bon[1]==2){
                printf("2 ");
            }
            if(tab_bon[2]==1){
                printf("1");
            }
            if(tab_bon[0]!=4 && tab_bon[1]!=2 && tab_bon[2]!=1){
                printf("Aucun \n");
            }
            else if ((tab_bon[0]==4 && tab_bon[1]==2 && tab_bon[2]==1)&&j<3) {
                printf("\nBRAVO ! Vous avez gagne en %d lancers !!", j);
                break;
            }
        }
        if (tab_bon[0]==4 && tab_bon[1]==2 && tab_bon[2]==1){
            printf("\nVous avez gagnez !! \n");
        }
        else{
            printf("\nVous avez perdu vous n'avez pas obtenu 421 en 3 lancers \n");
        }
        tab_bon[0]=0; tab_bon[1]=0; tab_bon[2]=0; nb=3;
        //printf("tab_bon=%d %d %d", tab_bon[0], tab_bon[1], tab_bon[2]);
    }
    printf("\nVous avez joue %d parties \n", nb_parties);
}


int main()
{
	int choix, n, nb_parties;
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
            printf("combien de partie voulez-vous jouez ?");
            scanf("%d", &nb_parties);
            jeu_des(nb_parties);
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

