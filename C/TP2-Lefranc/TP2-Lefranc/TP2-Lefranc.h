#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

#ifndef TP2-Lefranc_H
#define TP2-Lefranc_H


/* prototype des fonctions de tp2.c */

/*fonction qui demande 3 chiffre A B et C et résoud cette équation : Ax2 + Bx + C = 0
*/
void equation();

/*//fonction qui calcul la suite défini par u0=2 un+1=1/2(un+2/un) qui demande N puis affiche toutes les dixaine jusqu'a N, le résultat de U[N] et ce vers quoi la suite tant que N est positif
*/
void suite();

/*//fonction qui calcule le nombre de Fibonacci d'un nombre N
*/
int fibonacci(int n);

/*//fonction qui demande un nombre N puis affiche fibonacci(n+1)/fibonacci(N) affiche toutes les cinq jusqu'a N puis le résultat de O[N]
*/
void nb_or();

void dice();


/* prototype des fonctions de utils_fonc.c */

extern bool in(short value, short *array, short size);

/**
 * @brief Fonction qui permet de savoir si tous les nombres d'un tableau sont dans un autre tableau
 * 
 * @param list [short *]
 * @param array [short *]
 * @param size [short]
 * @return true 
 * @return false 
 */
extern bool all_in(short *list, short *array, short size);

/**
 * @brief Fonction qui permet de lancer un dé
 * 
 * @return short 
 */
extern short roll_dice();

/**
 * @brief Fonction qui permet d'afficher les nombres obtenus
 * 
 * @param list [short *]
 * @param size [int]
 */
extern void display_gotten_numbers(short *list, int size);

/**
 * @brief Fonction qui permet d'afficher les nombres gardés
 * 
 * @param list [short *]
 * @param size [short]
 */
extern void keep(short list[], short size);



#endif /* TP2_H */