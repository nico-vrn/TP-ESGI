#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include "TP1-Lefranc.h"


// Fonction qui calcule la surface d'un pentagone
int calculSurface()
{
	int longueur=0, nb_cote=0;
	float surface;
	printf("Valeur de la mesure d'un cote c (en m ) : ");
	scanf("%d", &longueur);
	printf("Nombre de cote n (en m ) : ");
	scanf("%d", &nb_cote);
	surface = (nb_cote * (longueur * longueur)) / (4 * tan(3.14 / nb_cote));
	printf("L'aire du pentagone est egal a : %.2f m", surface);
	return 0;
}


//fonction qui calcul la somme et le factoriel d'une suite de 0 jusqu'a un nombre donne par l'utilisateur
int sommeMultiplication()
{
	int nombre, somme = 0, factoriel = 1;
	do {
		printf("Entre une valeur superieur a 0 : ");
		scanf("%d", &nombre);
		if(nombre<=0){
			printf("La valeur doit etre superieur a 0 !\n");
		}
	} while (nombre <=0);
	for (int i = 1; i <= nombre; i++)
	{
		somme += i;
		factoriel *= i;
	}
	printf("- %d = ", somme);
	for (int i = 1; i <= nombre; i++)
	{
		if(i==nombre){
			printf("%d", i);
		}
		else{
			printf("%d + ", i);
		}
	}
	printf("\n- %d! = %d = ", nombre, factoriel);
	for (int i = 1; i <= nombre; i++)
	{
		if(i==nombre){
			printf("%d ", i);
		}
		else{
			printf("%d x ", i);
		}
	}
	return 0;
}


//fonction qui récupère 20 nombres saisies par l'utilisateur et qui affiche le plus grand et le plus petit de ces nombres avec leurs emplacement dans la liste
int plusGrand() 
{
	int nombre, plus_grand = 0, plus_petit = 0, position_plus_grand = 0, position_plus_petit = 0;
	for (int i = 1; i <= 20; i++)
	{
		printf("Entrer le nombre numero %d : ", i);
		scanf("%d", &nombre);
		if (i == 1)
		{
			plus_grand = nombre;
			plus_petit = nombre;
		}
		if (nombre > plus_grand)
		{
			plus_grand = nombre;
			position_plus_grand = i;
		}
		if (nombre < plus_petit)
		{
			plus_petit = nombre;
			position_plus_petit = i;
		}
	}
	printf("Le plus grand nombre est : %d et il est en position %d \n", plus_grand, position_plus_grand);
	printf("Le plus petit nombre est : %d et il est en position %d", plus_petit, position_plus_petit);
	return 0;
}


//fonction qui calcul la somme des premiers termes de la suite jusqu'a un nombre entré par l'utilisateur
int Suite()
{
	int nombre= 0;
	float somme = 0;
	do
	{
		printf("Entrez le nombre de terme de la suite a calculer n avec n > 0 (0 pour terminer) :");
		somme=0;
		scanf("%d", &nombre);
		if (nombre <0){
			printf("Erreur, la valeur ne peut pas etre negative.\n");
		}
		if (nombre > 0)
		{
			for (int i = 1; i <= nombre; i++)
			{
				somme += 1. / i ;
			}
			printf("U%d est : %.4f \n", nombre, somme);
		}
	} while (nombre != 0);
	printf("Fin du programme.");
	return 0;
}


//fonction qui affiche les caractère ASCII entre 34 et 127
int tableASCII()
{
	for (int i = 34; i <= 127; i++)
	{
		printf("[%d, %c] \t", i, i);
	}
	return 0;
}


//fonction qui fais un sapin du nombre de ligne et de caractère saisie par l'utilisateur
void Etoiles(const unsigned int nombre, const char caractere)
{
	unsigned int i = 1, j = 1, k = 1;
	while (i <= nombre)
	{
		while (j <= nombre - i)
		{
			printf(" ");
			j++;
		}
		while (k <= 2 * i - 1)
		{
			printf("%c", caractere);
			k++;
		}
		printf("\n");
		i++;
		j = 1;
		k = 1;
	}
	i = 2;
	while (i <= nombre - 1)
	{
		printf(" ");
		i++;
	}
	printf("%c%c%c", caractere, caractere, caractere);
	printf("\n ********************** Joyeux Noel *************");
}


//fonction qui demande la taille du tableau et les valeurs a l'utilisateur et qui affiche le tableau et la moyenne des lignes et des colonnes
int Tableau()
{
	int taille, somme_ligne = 0, somme_colonne = 0;
	do {
		printf("Entrez la taille du tableau (0 pour terminer) :  ");
		scanf("%d", &taille);
		int tableau[taille][taille];
		float liste_scolonne[4];
		// int liste_sligne[4];
		for (int i = 0; i < taille; i++)
		{
			for (int j = 0; j < taille; j++)
			{
				printf("Entrer un nombre [%d,%d]: ",i+1,j+1);
				scanf("%d", &tableau[i][j]);
			}
		}
		for (int i = 0; i < taille; i++)
		{
			for (int j = 0; j < taille; j++)
			{
				somme_ligne += tableau[i][j];
				somme_colonne += tableau[j][i];
			}
			for (int j = 0; j < taille; j++)
			{
				printf("%d \t", tableau[i][j]);
			}
			printf("(%.2f) \n", ((float)somme_ligne / taille));
			liste_scolonne[i] = ((float)somme_colonne / taille);
			somme_ligne = 0;		
			somme_colonne = 0;					
		}
		for (int i = 0; i < taille; i++)
		{
			printf("(%.2f) \t", liste_scolonne[i]);
		}
		printf("\n");	
	} while (taille != 0);
	printf("Fin du programme.");
	return 0;
}

//faire main qui appel les fonctions
 int main()
{
	int choix;
	const unsigned int nombre;
	const char caractere;
	do
	{
		printf("\n \n Choississez votre Fonction a utiliser \n");
		printf("1. Surface pentagone \n");
		printf("2. Somme \n");
		printf("3. plus grand \n");
		printf("4. Suite \n");
		printf("5. table ASCII \n");
		printf("6. Etoiles \n");
		printf("7. Tableau \n");
		printf("8. Quitter \n");
		printf("Entrer votre choix : ");
		scanf("%d", &choix);
		switch (choix)
		{
		case 1:
			calculSurface();
			break;
		case 2:
			sommeMultiplication();
			break;
		case 3:
			plusGrand();
			break;
		case 4:
			Suite();
			break;
		case 5:
			tableASCII();
			break;
		case 6:
			printf("Entrer un nombre : ");
			scanf("%d", &nombre);
			printf("Entrer un caractere : ");
			scanf(" %c", &caractere);
			Etoiles(nombre, caractere);
			break;
		case 7:
			Tableau();
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