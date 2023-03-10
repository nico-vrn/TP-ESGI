#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

typedef double ElementTableau;
typedef ElementTableau*Tableau;

typedef enum {DIVERS, VETEMENT, NOURRITURE, LIVRE} Type;

typedef struct {
    char a_nom[256];
    float a_prix;
    char a_description[1024];
    Type a_type;
} Article;