#include <time.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>

#ifndef TP3-Lefranc_H
#define TP3-Lefranc_H

/* prototype des fonctions de TP3-Lefranc.c */

/**
 * @brief Construit un tableau de double de taille donnée
 * @param dd pointeur sur le tableau de double
 * @param taille taille du tableau
 */
void TableauDouble_construire(PtrTableauDouble* dd, const unsigned taille);

/**
 * @brief Affiche un tableau de double
 * @param dd pointeur sur le tableau de double
 * @param taille taille du tableau
 */
void TableauDouble_afficher(const PtrTableauDouble dd, const unsigned taille);

/**
 * @brief Modifie un élément du tableau de double
 * @param dd pointeur sur le tableau de double
 * @param taille taille du tableau
 * @param index index de l'élément à modifier
 * @param valeur valeur à affecter à l'élément
 */
void TableauDouble_modifier(PtrTableauDouble dd, const unsigned taille, const unsigned index, const double valeur);

/**
 * @brief Libère un tableau de double
 * @param dd pointeur sur le tableau de double
 */
void TableauDouble_liberer(PtrTableauDouble* dd);

/**
 * @brief Retourne la valeur d'un élément du tableau de double
 * @param dd pointeur sur le tableau de double
 * @param taille taille du tableau
 * @param index index de l'élément à retourner
 * @return valeur de l'élément
 */
double TableauDouble_get(PtrTableauDouble dd, const unsigned taille, const unsigned index);

/**
 * @brief Modifie la valeur d'un élément du tableau de double
 * @param dd pointeur sur le tableau de double
 * @param taille taille du tableau
 * @param index index de l'élément à modifier
 * @param val valeur à affecter à l'élément
 */
void TableauDouble_set(PtrTableauDouble dd, const unsigned taille, const unsigned index, double val);

/**
 * @brief Exemple d'utilisation des fonctions de TP3-Lefranc.c
 * @return 0
 */
int C_1();

void construct_double_array(PtrDoubleArray* da,unsigned sz);
/**
 * @brief Construit un tableau de double de taille donnée
 * @param da pointeur sur le tableau de double
 * @param sz taille du tableau
 */

/**
 * @brief Affiche un tableau de double
 * @param da pointeur sur le tableau de double
*/
void print_double_array(const PtrDoubleArray da);

/**
 * @brief Modifie un élément du tableau de double
 * @param da pointeur sur le tableau de double
 * @param idx index de l'élément à modifier
 * @param val valeur à affecter à l'élément
 */
void modify_double_array(PtrDoubleArray da, const unsigned idx, const double val);

/**
 * @brief Libère un tableau de double
 * @param da pointeur sur le tableau de double
 */
void free_double_array(PtrDoubleArray* da);

/**
 * @brief Retourne la valeur d'un élément du tableau de double
 * @param da pointeur sur le tableau de double
 * @param idx index de l'élément à retourner
 * @return valeur de l'élément
 */
double get_value_double_array(const PtrDoubleArray da, const unsigned idx);

/**
 * @brief Modifie la valeur d'un élément du tableau de double
 * @param da pointeur sur le tableau de double
 * @param idx index de l'élément à modifier
 * @param val valeur à affecter à l'élément
 */
void set_value_double_array(PtrDoubleArray da, const unsigned idx, double val);

/**
 * @brief Exemple d'utilisation des fonctions 
 * @return 0
 */
int C_2();

/**
 * @brief Crée un livre
 * @param book pointeur sur le livre
 * @param name nom du livre
 * @param author auteur du livre
 * @param publisher éditeur du livre
 * @param barcode code barre du livre
 */
void create_book(Book* book, char* name, char* author, char* publisher, char* barcode);

/**
 * @brief Modifie un livre
 * @param book pointeur sur le livre
 * @param name nom du livre
 * @param author auteur du livre
 * @param publisher éditeur du livre
 * @param barcode code barre du livre
*/
void modify_book_attribute(Book* book, char* name, char* author, char* publisher, char* barcode);

void get_book_attribute(Book book, char* name, char* author, char* publisher, char* barcode);
/**
 * 
*/

/**
 * @brief Affiche un livre
 * @param book pointeur sur le livre
 */
void display_book_info(Book book);

/**
 * @brief Exemple d'utilisation des fonctions de livre
*/
int fct_book();

int main();
/**
 * 
*/

#endif /* TP3-Lefranc.h */