
import fltk

taille_fenetre = 1000
epaisseur_trait = 3
FENETRE_X = 900
FENETRE_Y = 600
taille_plateau = 300
rayon_intersection = 5


def plateau_de_jeu_9(version, taille_plateau):

    liste_points_possibles = []


    # Création des lignes
    fltk.ligne(FENETRE_X // 3,
               FENETRE_Y // 5 + taille_plateau // 2,
               FENETRE_X // 3 + taille_plateau // 3,
               FENETRE_Y // 5 + taille_plateau // 2,
               epaisseur=epaisseur_trait,
               couleur="black")
    fltk.ligne(FENETRE_X // 3 + taille_plateau // 2,
               FENETRE_Y // 5,
               FENETRE_X // 3 + taille_plateau // 2,
               FENETRE_Y // 5 + taille_plateau // 3,
               epaisseur=epaisseur_trait,
               couleur="black")
    fltk.ligne(FENETRE_X // 3 + (taille_plateau // 3) * 2,
               FENETRE_Y // 5 + taille_plateau // 2,
               FENETRE_X // 3 + taille_plateau,
               FENETRE_Y // 5 + taille_plateau // 2,
               epaisseur=epaisseur_trait,
               couleur="black")
    fltk.ligne(FENETRE_X // 3 + taille_plateau // 2,
               FENETRE_Y // 5 + taille_plateau,
               FENETRE_X // 3 + taille_plateau // 2,
               FENETRE_Y // 5 + (taille_plateau // 3) * 2,
               epaisseur=epaisseur_trait,
               couleur="black")


    # 200, 100 etc sont des valeurs obtenues en divisant taille_plateau par
    # 3 ou 6 (car taille_plateau == 600) et doivent être remplacée par des
    # variables
    for p in range(0, taille_plateau // 3 + 1, taille_plateau // 6):

        # Création des carrés : 'range(3)' pour trois carrés
        for carre in range(3):
            fltk.rectangle(FENETRE_X // 3 + p,
                           FENETRE_Y // 5 + p,
                           FENETRE_X // 3 + taille_plateau - p,
                           FENETRE_Y // 5 + taille_plateau - p,
                           epaisseur=3)

        for x in range(FENETRE_X // 3 + p, FENETRE_X // 3 + taille_plateau - p + 1,
                       taille_plateau // 2 - p):
            for y in range(FENETRE_Y // 5 + p, FENETRE_Y // 5 + taille_plateau - p + 100,
                           taille_plateau // 2 - p):

                if not (x == FENETRE_X // 3 + taille_plateau // 2
                        and y == FENETRE_Y // 5 + taille_plateau // 2):
                    fltk.cercle(x, y, rayon_intersection,
                                couleur='black',
                                remplissage='black')

                    liste_points_possibles.append((x, y))
    print(liste_points_possibles)
    return liste_points_possibles



def intersection_survolee(liste_points_possibles):

    for i in range(len(liste_points_possibles)):
        x_point, y_point = liste_points_possibles[i]          # A MODIFIER? appel de la fonction intersection() ?
        if collision(x_point, y_point):
            fltk.cercle(x_point, y_point, rayon_intersection,
                        couleur='blue',
                        remplissage='blue',
                        tag='point_survolé')
            return True

def efface_intersection_survolee():
    fltk.efface('point_survolé')


def collision(x,y):
    if fltk.abscisse_souris() > x - rayon_intersection \
    and fltk.ordonnee_souris() > y - rayon_intersection \
    and fltk.abscisse_souris() < x + rayon_intersection \
    and fltk.ordonnee_souris() < y + rayon_intersection:
        return True

    return False

def adjacence(test):
    dico_adjacence = {(300,120):[(450,120),(300,270)], (450,120):[(300,120),(450,170),(600,120)], (600,120):[(450,120),(600,270)],
                      (350,170):[(450,170),(350,270)], (450,170):[(450,120),(350,170),(550,170),(450,220)] ,(550,170):[(450,170),(550,270)],
                      (400,220):[(400,270),(450,220)], (450,220):[(400,220),(450,170),(500,220)], (500,220):[(450,220),(500,270)],
                      (300,270):[(300,120),(350,270),(300,420)], (350,270):[(300,270),(350,170),(400,270),(350,370)], (400,270):[(400,220),(350,270),(400,320)],
                      (500,270):[(500,220),(550,270),(500,320)], (550,270):[(500,270),(550,170),(600,270),(550,370)], (600,270):[(600,120),(550,270),(600,420)],
                      (400,320):[(400,270),(450,320)], (450,320):[(400,320),(500,320),(450,370)], (500,320):[(450,320),(500,270)],
                      (350,370):[(350,270),(450,370)], (450,370):[(350,370),(450,320),(550,370),(450,420)], (550,370):[(450,370),(550,270)],
                      (300,420):[(300,270),(450,420)], (450,420):[(300,420),(450,370),(600,420)], (600,420):[(450,420),(600,270)],
                      }
    # Retourne le dictionnaire d'adjacence de chaque points. EX: dico_adjacence[(x,y)] = [(a,b),(a',b')]
    return dico_adjacence[test]

def affichage_principal():

    fltk.cree_fenetre(FENETRE_X, FENETRE_Y)
    # Pour le fond
    #fltk.rectangle(-10, -10, 1000, 1000, remplissage='#bababa')

    liste_points_possibles = plateau_de_jeu_9('A', taille_plateau)

    continuer = True
    while continuer:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)

        efface_intersection_survolee()
        intersection_survolee(liste_points_possibles)

        if tev == "Quitte":
            continuer = False

        if tev == "ClicGauche":
            print(fltk.abscisse(ev), fltk.ordonnee(ev))

        fltk.mise_a_jour()

    fltk.ferme_fenetre()

affichage_principal()