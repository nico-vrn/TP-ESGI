#include <stdio.h>
/*
int main() {
    int capaciteMax = 10;  
    int notes[capaciteMax];  
    int nombreDeNotes = 0;  
    int note;
    int total = 0;
    float moyenne;
    int notesSuperieures = 0;  

    printf("Saisissez des notes entre 0 et 20. Entrez -1 pour terminer la saisie.\n");

    while (nombreDeNotes < capaciteMax) {
        printf("Note %d : ", nombreDeNotes + 1);
        scanf("%d", &note);

        if (note == -1) {
            printf("Saisie terminée.\n");
            break;  
        }

        if (note < 0 || note > 20) {
            printf("Erreur : La note doit être entre 0 et 20.\n");
            continue;  
        }

        notes[nombreDeNotes] = note;
        total += note;
        nombreDeNotes++;
    }

    if (nombreDeNotes == 0) {
        printf("Pas de note saisie.\n");
    } else {
        moyenne = (float)total / nombreDeNotes;
        printf("La moyenne des notes saisies est : %.2f\n", moyenne);

        for (int i = 0; i < nombreDeNotes; i++) {
            if (notes[i] > moyenne) {
                notesSuperieures++;
            }
        }

        printf("Nombre de notes supérieures à la moyenne : %d\n", notesSuperieures);
    }

    return 0;
}*/
/*
#define Max(a,b) (a>b)?a:b
#define Min(a,b) (a<b)?a:b

int main() {
    int a;
    int b;
    printf("donner un entier"); 
    scanf("%d", &a);
    printf("donner un entier");
    scanf("%d", &b);
    printf("le max est %d", Max(a,b));
    printf("Le min est %d", Min(a,b));
}
*/
/*
struct enregistrement {
    int num;
    int quant;
    float prix;
};

int main() {
    struct enregistrement coucou[5];
    int i;
    
    for(i = 0; i < 5; i++) {
        printf("Donner le numero de l'article : ");
        scanf("%d", &coucou[i].num);
        
        printf("Donner la quantite de l'article : ");
        scanf("%d", &coucou[i].quant);
        
        printf("Donner le prix de l'article : ");
        scanf("%f", &coucou[i].prix);
    }
    
    for(i=0;i<5;i++){
        printf("Numero : %d\n", coucou[i].num);
        printf("Quantite : %d\n", coucou[i].quant);
        printf("Prix : %f\n", coucou[i].prix);
    }
    return 0;
}*/
/*

struct enregistrement {
    int num;
    int quant;
    float prix;
};

int main(){
    struct enregistrement *pt_struct, *pt_courant;

    pt_struct = malloc(5*sizeof(struct enregistrement));
    
    pt_courant = pt_struct;

    for(;pt_courant < pt_struct + 5; pt_courant++){
        printf("Donner le numero de l'article : ");
        scanf("%d", &pt_courant->num);
        
        printf("Donner la quantite de l'article : ");
        scanf("%d", &pt_courant->quant);
        
        printf("Donner le prix de l'article : ");
        scanf("%f", &pt_courant->prix);
    }

    pt_courant = pt_struct;

    for(;pt_courant<pt_struct+5;pt_courant++){
        printf("Numero : %d\n", pt_courant->num);
        printf("Quantite : %d\n", pt_courant->quant);
        printf("Prix : %f\n", pt_courant->prix);
    }

    free(pt_struct);
    return 0;
}*/

struct Node {
    int data;
    struct Node* next;
};

struct Node *head = NULL;

void insert(int new_data) {
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = head;
    head = new_node;
}