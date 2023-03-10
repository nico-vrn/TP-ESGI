#ifndef PARTIEL_C_LEFRANC_H_INCLUDED
#define PARTIEL_C_LEFRANC_H_INCLUDED

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>

#define NB_MAX_ARTICLES 1

typedef double ElementTableau;
typedef ElementTableau*Tableau;

typedef enum {DIVERS, VETEMENT, NOURRITURE, LIVRE} Type;

typedef struct {
    char a_nom[256];
    float a_prix;
    char a_description[1024];
    Type a_type;
} Article;

double mypow(double x, int n);

double Suite(double x, unsigned N);

void Exercice1();

void permuter(ElementTableau *a, ElementTableau *b);

void permuter_Tableau(Tableau tab, unsigned size);

Tableau creer_Tableau(unsigned size);

void liberer_Tableau(Tableau *tab);

void afficher(const Tableau tab, unsigned size);

void Exercice2();

Article* creer_Article();

void afficher_Article(const Article* article);

void modifier_Article(Article *article);

void liberer_Article(Article* article);

void save_Article(const Article* article, const char* nomFichier);

void load_Article(Article* article, FILE* fichier);

int main_Article();

int main();

#endif // PARTIEL_C_LEFRANC_H_INCLUDED