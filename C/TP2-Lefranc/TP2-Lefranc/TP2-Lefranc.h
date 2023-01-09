#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>

#ifndef TP2-Lefranc_H
#define TP2-Lefranc_H


/* prototype des fonctions de TP2-Lefranc.c */

//fonction qui demande 3 chiffre A B et C et résoud cette équation : Ax2 + Bx + C = 0
void equation();
/**
 * @brief equation
*/

//fonction qui calcul la suite défini par u0=2 un+1=1/2(un+2/un) qui demande N puis affiche toutes les dixaine jusqu'a N, le résultat de U[N] et ce vers quoi la suite tant que N est positif
void suite();
/**
 * @brief suite
*/
 
//fonction qui calcule le nombre de Fibonacci d'un nombre N
int fibonacci(int n);
/**
 * @brief fibonacci
 * @param n
*/

//fonction qui demande un nombre N puis affiche fibonacci(n+1)/fibonacci(N) affiche toutes les cinq jusqu'a N puis le résultat de O[N]
/**
 * @brief nb_or
*/
void nb_or();

/**
 * @brief lancer_des
 * @param nb
*/
void lancer_des(int nb);

//fonction qui demande un nombre N puis lance N parties du jeu des dés et affiche le nombre de parties gagnées et perdues
/**
 * @brief jeu_des
 * @param nb
*/
void jeu_des(nb_parties);

#endif /* TP2-Lefranc.h */