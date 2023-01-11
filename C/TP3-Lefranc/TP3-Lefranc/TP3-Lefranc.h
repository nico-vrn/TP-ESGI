#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

#ifndef TP3_LEFRANC_H
#define TP3_LEFRANC_H

typedef double* PtrTableauDouble;

/**
 * @brief TableauDouble_construire
 * @param dd : pointeur sur le tableau
 * @param taille :taille du tableau
 */ 
void TableauDouble_construire(PtrTableauDouble* dd, const unsigned taille);

/**
 * @brief TableauDouble_afficher
 * @param dd : pointeur sur le tableau
 * @param taille : taille du tableau
 */
void TableauDouble_afficher(const PtrTableauDouble dd, const unsigned taille);

/**
 * @brief TableauDouble_modifier
 * @param dd : pointeur sur le tableau
 * @param taille : taille du tableau
 * @param index : index du tableau
 * @param valeur : valeur à modifier
 */
void TableauDouble_modifier(PtrTableauDouble dd, const unsigned taille, const unsigned index, const double valeur);

/**
 * @brief TableauDouble_liberer
 * @param dd : pointeur sur le tableau
 */
void TableauDouble_liberer(PtrTableauDouble* dd);

/**
 * @brief TableauDouble_get
 * @param dd : pointeur sur le tableau
 * @param taille : taille du tableau
 * @param index : index du tableau
 * @return la valeur à l'index
 */
double TableauDouble_get(PtrTableauDouble dd, const unsigned taille, const unsigned index);

/**
 * @brief TableauDouble_set
 * @param dd : pointeur sur le tableau
 * @param taille : taille du tableau
 * @param index : index du tableau
 * @param val : valeur à modifier
 */
void TableauDouble_set(PtrTableauDouble dd, const unsigned taille, const unsigned index, double val);

/**
 * @brief appel les fonctions
 */
void C_1();


typedef struct {
    double* array;
    unsigned int size;
} DoubleArray;
typedef DoubleArray* PtrDoubleArray;

/**
 * @brief construct_double_array
 * @param da : pointeur sur le tableau
 * @param sz : taille du tableau
*/
void construct_double_array(PtrDoubleArray* da,unsigned sz);

/**
 * @brief print_double_array
 * @param da : pointeur sur le tableau
 */
void print_double_array(PtrDoubleArray da);

void modify_double_array(PtrDoubleArray da, const unsigned idx, const double val);
/**
 * @brief modify_double_array
 * 
*/

/**
 * @brief free_double_array
 * @param da : pointeur sur le tableau
 */
void free_double_array(PtrDoubleArray* da);

/**
 * @brief get_double_array
 * @param da : pointeur sur le tableau
 * @param index : index du tableau
 * @return la valeur à l'index
 */
double get_value_double_array(PtrDoubleArray da, const unsigned idx);

/**
 * @brief set_double_array
 * @param da : pointeur sur le tableau
 * @param index : index du tableau
 * @param val : valeur à modifier
 */
void set_value_double_array(PtrDoubleArray da, const unsigned idx, double val);

/**
 * @brief appel les fonctions
 */
void C_2();

#endif