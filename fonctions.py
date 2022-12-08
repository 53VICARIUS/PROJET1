import fltk
from variables import *


def plateau_de_jeu_9(version, taille_plateau):

    liste_points_possibles = []
    rayon_intersection = 5
    epaisseur_trait = 3

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


def interface():
    dd = 4


def tour_joueur():
    dd = 2



def intersection_survolee(liste_points_possibles):

    for i in range(len(liste_points_possibles)):
        x_point, y_point = liste_points_possibles[i]

        if fltk.abscisse_souris() > x_point - rayon_intersection \
        and fltk.ordonnee_souris() > y_point - rayon_intersection \
        and fltk.abscisse_souris() < x_point + rayon_intersection \
        and fltk.ordonnee_souris() < y_point + rayon_intersection:

            fltk.cercle(x_point, y_point, rayon_intersection,
                        couleur='blue',
                        remplissage='blue',
                        tag='point_survolé')

def efface_intersection_survolee():
    fltk.efface('point_survolé')


def intersection(liste_points_possibles, ev):


    for i in range(len(liste_points_possibles)):
        x_point, y_point = liste_points_possibles[i]

        if fltk.abscisse(ev) > x_point - rayon_intersection \
        and fltk.ordonnee(ev) > y_point - rayon_intersection \
        and fltk.abscisse(ev) < x_point + rayon_intersection \
        and fltk.ordonnee(ev) < y_point + rayon_intersection:

            print('intersection')


def affichage():

    fltk.cree_fenetre(FENETRE_X, FENETRE_Y)
    # Pour le fond
    fltk.rectangle(-10, -10, 9000, 9000, remplissage='#bababa')

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
            intersection(liste_points_possibles, ev)
            print(fltk.abscisse(ev), fltk.ordonnee(ev))

        fltk.mise_a_jour()
    fltk.ferme_fenetre()
