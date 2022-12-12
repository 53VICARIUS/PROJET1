import fltk
from variables import *


def plateau_de_jeu_9(version):
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

    for p in range(0, taille_plateau // 3 + 1, taille_plateau // 6):

        # Création des carrés : 'range(3)' pour trois carrés
        for carre in range(3):
            fltk.rectangle(FENETRE_X // 3 + p,
                           FENETRE_Y // 5 + p,
                           FENETRE_X // 3 + taille_plateau - p,
                           FENETRE_Y // 5 + taille_plateau - p,
                           epaisseur=epaisseur_trait)

        for x in range(FENETRE_X // 3 + p,
                       FENETRE_X // 3 + taille_plateau - p + 1,
                       taille_plateau // 2 - p):
            for y in range(FENETRE_Y // 5 + p,
                           FENETRE_Y // 5 + taille_plateau - p + 1,
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


# Pour trier la liste_points_possibles plus tard
def sort():
    dd = 2


def tour_joueur(tour_jeu):
    if tour_jeu % 2 == 0:
        joueur = 'white'
        return joueur
    else:
        joueur = 'black'
        return joueur


def intersection(liste_points_possibles, tour_jeu, tev):
    for i in range(len(liste_points_possibles)):
        x_point, y_point = liste_points_possibles[i]

        if intersection_survolee(x_point, y_point):
            fltk.cercle(x_point, y_point, rayon_intersection,
                        couleur='blue',
                        remplissage='blue',
                        tag='point_survolé')

            if tev == "ClicGauche":
                joueur = tour_joueur(tour_jeu)
                fltk.cercle(x_point, y_point, rayon_pion,
                            couleur=joueur,
                            remplissage=joueur,
                            tag='')

                print(x_point, y_point)
                tour_jeu += 1

    return tour_jeu


def efface_intersection_survolee():
    fltk.efface('point_survolé')


def intersection_survolee(x_point, y_point):
    if fltk.abscisse_souris() > x_point - rayon_intersection \
    and fltk.ordonnee_souris() > y_point - rayon_intersection \
            and fltk.abscisse_souris() < x_point + rayon_intersection \
            and fltk.ordonnee_souris() < y_point + rayon_intersection:
        return True

    return False


def affichage():
    tour_jeu = 0

    fltk.cree_fenetre(FENETRE_X, FENETRE_Y)
    # Pour le fond
    fltk.rectangle(-10, -10, 9000, 9000, remplissage='#bababa')

    liste_points_possibles = plateau_de_jeu_9('A')

    continuer = True

    while continuer:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)

        efface_intersection_survolee()
        tour_jeu = intersection(liste_points_possibles, tour_jeu, tev)

        if tev == "Quitte":
            continuer = False

        fltk.mise_a_jour()
    fltk.ferme_fenetre()
