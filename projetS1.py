import fltk
from variables import *

FENETRE_X = 900
FENETRE_Y = 600
taille_plateau = 300
rayon_intersection = 5
rayon_pion = 10
epaisseur_trait = 2
tour = 0 # tour ?
pions_version = 9

dico_pions ={"white":[],"black":[]}


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

    fltk.rectangle(FENETRE_X // 8,
                   FENETRE_Y - FENETRE_Y // 4,
                   FENETRE_X - FENETRE_X // 8,
                   FENETRE_Y - FENETRE_Y // 30,
                   couleur = 'black')


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
        if len(liste_points_possibles[i]) != 0:
            x_point, y_point = liste_points_possibles[i]

            if intersection_survolee(x_point, y_point):
                fltk.cercle(x_point, y_point, rayon_intersection,
                            couleur='blue',
                            remplissage='blue',
                            tag='point_survolé')

                if tev == "ClicGauche":
                    liste_points_possibles[i] = []
                    joueur = tour_joueur(tour_jeu)
                    fltk.cercle(x_point, y_point, rayon_pion,
                                couleur=joueur,
                                remplissage=joueur,
                                tag='')
                    dico_pions[joueur].append((x_point, y_point))
                    tour_jeu += 1

    return tour_jeu, liste_points_possibles

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


def efface_intersection_survolee():
    fltk.efface('point_survolé')


def intersection_survolee(x_point, y_point):
    if fltk.abscisse_souris() > x_point - rayon_intersection \
    and fltk.ordonnee_souris() > y_point - rayon_intersection \
    and fltk.abscisse_souris() < x_point + rayon_intersection \
    and fltk.ordonnee_souris() < y_point + rayon_intersection:
        return True
    return False


def premiere_partie(tour_jeu):
    return tour_jeu <= (2*pions_version)-1



def clic_pion(tour_jeu,tev):
    joueur = tour_joueur(tour_jeu)
    for i in range(len(dico_pions[joueur])):
        x_point, y_point = dico_pions[joueur][i]

        if intersection_survolee(x_point, y_point):
            if tev == "ClicGauche":
                temp = x_point, y_point
                return temp



def bouger_pion(tour_jeu,tev):
    # fonction de la Partie 2 #
    joueur = tour_joueur(tour_jeu)
    temp =
    for i in range(len(dico_pions[joueur])):
        x_point, y_point = dico_pions[joueur][i]

        if intersection_survolee(x_point, y_point):
            if tev == "ClicGauche":
                temp = x_point, y_point




def affichage():
    tour_jeu = 0

    fltk.cree_fenetre(FENETRE_X, FENETRE_Y)
    # Pour le fond
    fltk.rectangle(-10, -10, 9000, 9000, remplissage='#bababa')

    liste_points_possibles = plateau_de_jeu_9('A')
    interface()

    continuer = True

    while continuer:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)

        if premiere_partie(tour_jeu):
            efface_intersection_survolee()
            tour_jeu, liste_points_possibles = \
                intersection(liste_points_possibles, tour_jeu, tev)

        if tour_jeu >= 18:
            #clic_pion(tour_jeu,tev):
            #bouger_pion(liste_points_possibles,tour_jeu,tev)
            print("rien")
        if tev == "Touche":
            if fltk.touche(ev) == "a":
                print(dico_pions)
        if tev == "Quitte":
            continuer = False

        fltk.mise_a_jour()
    fltk.ferme_fenetre()
