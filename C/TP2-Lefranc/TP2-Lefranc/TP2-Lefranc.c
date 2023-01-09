#include "TP2-Lefranc.h"

//fonction qui demande 3 chiffre A B et C et résoud cette équation : Ax2 + Bx + C = 0
void equation()
{
    float a, b, c, delta, x1, x2;
    printf("\nResoudre l\'equation du second degre : Ax2 + Bx + C = 0 \n");
    printf("Entrez A (un chiffre) :");
    scanf("%f", &a);
    printf("Entrez B (un chiffre) :");
    scanf("%f", &b);
    printf("Entrez C (un chiffre) :");
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
    printf("\nCalcul de la suite definie par u0=2 un+1=1/2(un+2/un) \n");
    printf("Entrez N (un chiffre) :");
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
    printf("\nCette suite tant vers le resultat positif de la resolution de l\'equation xcarre-2 qui est %.2f .", un);
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
    printf("\nCalcul de la suite definie par O[n]=F[n+1]/F[n] \n");
    printf("Entrez N (un chiffre) :");
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

int nb;
int tab_des[3];
int tab_bon[3]={0,0,0};

//fonction qui demande un nombre N puis lance N dés et affiche le résultat
void lancer_des(nb)
{
    //printf("nb_des= %d \n", nb);
    int i, des; 
    for (i = 0; i < nb; i++)
    {
        des = rand()%6+1;
        //printf("Le des %d est egal a %d \n", i, des);
        tab_des[i] = des;
        //printf("tab_des[%d] = %d \n", i, tab_des[i]);
    }
    printf("votre lancer est :");
    if (nb==1){
        printf(" %d ", tab_des[0]);
    }
    else if (nb==2){
        printf(" %d %d ", tab_des[0], tab_des[1]);
    }
    else if (nb==3){
        printf(" %d %d %d ", tab_des[0], tab_des[1], tab_des[2]);
    }
    printf("\n");
}

//fonction qui demande un nombre N puis lance N parties du jeu des dés et affiche le nombre de parties gagnées et perdues
void jeu_des(nb_parties)
{
    printf("\nBienvenue dans le jeu des des !\n");
    printf("Il va falloir obtenir 421 pour gagner en moins de 3 lancers. \n");

    int parties=0; int partie_gagne=0; int partie_perdu=0; nb=3;
    srand(time(NULL));
    for(int f=0;f<nb_parties;f++){
        int j=0;
        while (j<3){
            printf("\n\nLancer numero %d, partie numero %d avec %d des :\n", j+1, f+1, nb);
            lancer_des(nb);
            //printf("nb= %d \n", nb);
            for (int i = 0; i <=nb; i++)
            {
                //printf("\ni=%d, tab[%d]=%d \n", i, i, tab_des[i]);
                if (tab_des[i] == 4)
                {
                    printf("Le des %d est egal a 4, ", i+1);
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
                    printf("Le des %d est egal a 2, ", i+1);
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
                    printf("Le des %d est egal a 1, ", i+1);
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
            partie_gagne+=1;
        }
        else{
            printf("\nVous avez perdu vous n'avez pas obtenu 421 en 3 lancers \n");
            partie_perdu+=1;
        }
        tab_bon[0]=0; tab_bon[1]=0; tab_bon[2]=0; nb=3;
        //printf("tab_bon=%d %d %d", tab_bon[0], tab_bon[1], tab_bon[2]);
    }
    printf("\nVous avez joue %d parties, %d parties gagnes et %d parties perdus. Soit %d%% de gain. \n", nb_parties, partie_gagne, partie_perdu, partie_gagne*100/nb_parties);
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
            printf("\nCalcul du nombre de Fibonacci d'un nombre N \n");
            printf("Entrez la valeur de n (un chiffre) : ");
            scanf("%d", &n);
            printf("Le nombre de Fibonacci de %d est %d : F[%d] = %d", n,fibonacci(n),n,fibonacci(n));
			break;
		case 4:
			nb_or();
			break;
		case 5:
            printf("combien de partie voulez-vous jouez ? (un chiffre) :");
            scanf("%d", &nb_parties);
            jeu_des(nb_parties);
			break;
		case 6:
			printf("Au revoir \n");
			break;
		default:
			printf("Choix invalide");
			break;
		}
	} while (choix != 6);
	return 0;
}

