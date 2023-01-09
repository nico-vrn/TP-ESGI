void lancer(){
    int tab[3];
    int tab_valeur[3]={1,2,4};
    int value_got[3]={0,0,0};
    int index_value_got=0;

    int nb_parties;
    int nb_parties_gagnees=0;
    int nb_parties_perdues=0;
    int nb_des_depart=3;

    printf("Combien de partie voulez-vous jouez ? : ");
    scanf("%d", &nb_parties);

    for (int i=0;i<nb_parties;i++){
        //lancer 3 dés
        for (int j=0;j<nb_des_depart;j++){
            tab[j]=lance_des();
            printf("Lancé n° %d dé %d est tombé sur %d\n",i+1, j+1,tab[j]);
        }

        //cherchez si les valeurs sont les bonnes
        for(int i=0;i<nb_des_depart;i++){
            if(tab[i]!=1 && tab[i]!=2 && tab[i]!=4){
                printf("il n'y a pas les bons nombres\n");
            }
            else{
                for(int j=0;j<nb_des_depart;j++){
                    
                }
            }
                
        }
        else{

            }
        }
}