import fltk
from variables import *

##############################################################################
# Fonctions chargées de la création des éléments sur l'interface             #
##############################################################################

def creation_dico():
    global dico_plateau

    for i in range(len(liste_intersections)):
        dico_plateau[liste_intersections[i]] = False

    print(dico_plateau)


def plateau_de_jeu_9():

    global liste_coups_possibles

    # Création des lignes du plateau
    fltk.ligne(FENETRE_X // 3,
               FENETRE_Y // 5 + TAILLE_PLATEAU // 2,
               FENETRE_X // 3 + TAILLE_PLATEAU // 3,
               FENETRE_Y // 5 + TAILLE_PLATEAU // 2,
               epaisseur=2,
               couleur="black")
    fltk.ligne(FENETRE_X // 3 + TAILLE_PLATEAU // 2,
               FENETRE_Y // 5,
               FENETRE_X // 3 + TAILLE_PLATEAU // 2,
               FENETRE_Y // 5 + TAILLE_PLATEAU // 3,
               epaisseur=2,
               couleur="black")
    fltk.ligne(FENETRE_X // 3 + (TAILLE_PLATEAU // 3) * 2,
               FENETRE_Y // 5 + TAILLE_PLATEAU // 2,
               FENETRE_X // 3 + TAILLE_PLATEAU,
               FENETRE_Y // 5 + TAILLE_PLATEAU // 2,
               epaisseur=2,
               couleur="black")
    fltk.ligne(FENETRE_X // 3 + TAILLE_PLATEAU // 2,
               FENETRE_Y // 5 + TAILLE_PLATEAU,
               FENETRE_X // 3 + TAILLE_PLATEAU // 2,
               FENETRE_Y // 5 + (TAILLE_PLATEAU // 3) * 2,
               epaisseur=2,
               couleur="black")

    # Boucle chargée de créer les differents carrés et les points du plateau
    for p in range(0, TAILLE_PLATEAU // 3 + 1, TAILLE_PLATEAU // 6):

        # Création des carrés
        for carre in range(3):
            fltk.rectangle(FENETRE_X // 3 + p,
                           FENETRE_Y // 5 + p,
                           FENETRE_X // 3 + TAILLE_PLATEAU - p,
                           FENETRE_Y // 5 + TAILLE_PLATEAU - p,
                           epaisseur=EPAISSEUR_LIGNE)

        # Création des points situés aux intersections du plateau
        for x in range(FENETRE_X // 3 + p,
                       FENETRE_X // 3 + TAILLE_PLATEAU - p + 1,
                       TAILLE_PLATEAU // 2 - p):
            for y in range(FENETRE_Y // 5 + p,
                           FENETRE_Y // 5 + TAILLE_PLATEAU - p + 1,
                           TAILLE_PLATEAU // 2 - p):

                # Détecte si le point est au milieu du terrain : si oui, ne
                # le place pas
                if not (x == FENETRE_X // 3 + TAILLE_PLATEAU // 2
                   and y == FENETRE_Y // 5 + TAILLE_PLATEAU // 2):

                    fltk.cercle(x, y, RAYON_INTERSECTION,
                                couleur='black',
                                remplissage='black')
                    # Ajoute les coordonnées à la liste des intersections
                    liste_intersections.append((x, y))

    # Ajoute également les coordonnées à la liste des coups possibles
    liste_coups_possibles = liste_intersections
    creation_dico()


def interface():

    # Création de la "boite de texte"
    fltk.rectangle(FENETRE_X // 5,
                   FENETRE_Y - FENETRE_Y // 4,
                   FENETRE_X - FENETRE_X // 5,
                   FENETRE_Y - FENETRE_Y // 30,
                   epaisseur=EPAISSEUR_LIGNE,
                   couleur='black')

    # Création du plateau de jeu
    plateau_de_jeu_9()

    # Création du texte "TOUR"
    fltk.texte(FENETRE_X - FENETRE_X // 1.5,
               FENETRE_Y - FENETRE_Y // 5.5,
               chaine='TOUR',
               taille=45)


def affichage_tour():

    joueur = tour_joueur(tour_jeu)

    fltk.cercle(FENETRE_X - FENETRE_X // 3,
                FENETRE_Y - FENETRE_Y // 6.75,
                50,
                couleur=joueur,
                remplissage=joueur,
                tag='pion_joueur_actif')


def affichage_instruction():

    # tour_jeu sera inférieur à 18 durant tout le long de la phase 1 (car
    # 18 pions n'auront pas été posés
    if tour_jeu < 18:

        # Création de l'instruction
        fltk.texte(FENETRE_X - FENETRE_X // 2,
                   FENETRE_Y - FENETRE_Y // 1.1,
                   chaine='POSEZ UN PION',
                   taille=34,
                   ancrage='center',
                   tag='instruction')

    elif pion_selectionne:

        # Création de l'instruction
        fltk.texte(FENETRE_X - FENETRE_X // 2,
                   FENETRE_Y - FENETRE_Y // 1.1,
                   chaine='DEPLACEZ VOTRE PION',
                   taille=34,
                   ancrage='center',
                   tag='instruction')

    else:

        # Création de l'instruction
        fltk.texte(FENETRE_X - FENETRE_X // 2,
                   FENETRE_Y - FENETRE_Y // 1.1,
                   chaine='CHOISISSEZ UN PION À DEPLACER',
                   taille=34,
                   ancrage='center',
                   tag='instruction')


def efface_instruction():
    fltk.efface('instruction')


def cree_pion(cle, x, y):

    global pions_blancs, pions_noirs, dico_plateau

    joueur = tour_joueur(tour_jeu)

    if joueur == 'white':
        tag = f'pion_{joueur}_{pions_blancs}'
        fltk.cercle(x, y, RAYON_PION,
                    couleur=joueur,
                    remplissage=joueur,
                    tag=tag)

        dico_plateau[cle] = tag
        pions_blancs += 1

    else:
        tag = f'pion_{joueur}_{pions_noirs}'
        fltk.cercle(x, y, RAYON_PION,
                    couleur=joueur,
                    remplissage=joueur,
                    tag=tag)

        dico_plateau[cle] = tag
        pions_noirs += 1

    # liste_coups_possibles[i] = tag

##############################################################################
# Fonctions chargées de calculs                                              #
##############################################################################

def tour_joueur(tour_jeu):
    """
    Détermine le joueur à qui il est le tour de jouer.
    :param tour_jeu:
    :return:
    """

    if tour_jeu % 2 == 0:
        joueur = 'white'
        return joueur
    else:
        joueur = 'black'
        return joueur

##############################################################################
# Fonctions chargées de détecter (?)                                         #
##############################################################################

def moulin_vertical():

    # Pions blancs
    for i in range(len(liste_pions_blancs)):
        coordonnees_pion = liste_pions_blancs[i][1]

        for cle in dico_adjacence:
            if cle == coordonnees_pion:
                liste_voisins = dico_adjacence[cle]

        for j in range(len(liste_pions_blancs)):
            x, y = liste_pions_blancs[j][1]

            for k in range(len(liste_voisins)):
                x2, y2 = liste_voisins[k]

                if x == x2:
                    coordonnees_pion = liste_voisins[k]

                    for cle in dico_adjacence:
                        if cle == coordonnees_pion:
                            liste_voisins = dico_adjacence[cle]

                    for l in range(len(liste_pions_blancs)):
                        x, y = liste_pions_blancs[j][1]


def moulin_horizontal():
    dd = 2


def moulins():

    dd = 2

##############################################################################
# Fonctions chargées des interactions avec l'interface                       #
##############################################################################

def intersection_survolee(x, y):

    if fltk.abscisse_souris() > x - RAYON_INTERSECTION \
    and fltk.ordonnee_souris() > y - RAYON_INTERSECTION \
    and fltk.abscisse_souris() < x + RAYON_INTERSECTION \
    and fltk.ordonnee_souris() < y + RAYON_INTERSECTION:
        return True
    return False


def efface_intersection_survolee():
    """
    Si une intersection est survolée, elle est surlignée en bleue. Cette
    fonction est chargée d'effacer le survol une fois que la souris quitte la
    hitbox de l'intersection.
    (à changer en survol tout court parce que)

    :return: None
    """

    fltk.efface('point_survolé')


def intersection_valide(tev):
    """
    Fonctions regroupant tous les types d'interactions avec une
    intersection valide (= qui n'est pas occupée par un pion). Elle est
    chargée d'executer certains codes si les conditions sont remplies.
    :param tev:
    :return:
    """

    global tour_jeu

    for cle in dico_plateau:
        x, y = cle
        etat = dico_plateau[cle]

        if intersection_survolee(x, y) \
        and not isinstance(etat, str):
            fltk.cercle(x, y, RAYON_INTERSECTION,
                        couleur='blue',
                        remplissage='blue',
                        tag='point_survolé')

            if tev == "ClicGauche":
                cree_pion(cle, x, y)
                tour_jeu += 1
                print(dico_plateau)


def mouvement_pion(tev):

    global dico_plateau, pion_selectionne

    joueur = tour_joueur(tour_jeu)

    for cle in dico_plateau:
        etat = dico_plateau[cle]

        if isinstance(etat, str):
            if joueur == etat.split('_')[1]:
                x, y = cle

                if intersection_survolee(x, y):
                    fltk.cercle(x, y, RAYON_INTERSECTION * 2,
                                couleur='green',
                                epaisseur=5,
                                tag='point_survolé')

                    if tev == "ClicGauche" \
                    and not pion_selectionne:
                        fltk.cercle(x, y, RAYON_INTERSECTION * 2,
                                    couleur='green',
                                    remplissage='green',
                                    tag='pion_sélectioné')
                        pion_selectionne = True

                if pion_selectionne:
                    for cle2 in dico_adjacence:
                        if cle2 == cle:
                            liste_voisins = dico_adjacence[cle2]

                            for i in range(len(liste_voisins)):
                                etat2 = dico_plateau[liste_voisins[i]]

                                if isinstance(etat2, bool):
                                    x2, y2 = liste_voisins[i]
                                    fltk.cercle(x2, y2, RAYON_INTERSECTION,
                                                couleur='green',
                                                remplissage='green',
                                                tag='mouvements_possibles')

                                    if intersection_survolee(x2, y2):
                                        fltk.cercle(x2, y2,
                                                    RAYON_INTERSECTION,
                                                    couleur='blue',
                                                    remplissage='blue',
                                                    tag='point_survolé')

                                        if tev == "ClicGauche":

                                            dico_plateau[cle] = False
                                            dico_plateau[(x2, y2)] = etat

                                            fltk.efface('mouvements_possibles')
                                            fltk.efface('pion_sélectioné')
                                            fltk.efface(etat)
                                            fltk.cercle(x2, y2, RAYON_PION,
                                                        couleur=joueur,
                                                        remplissage=joueur,
                                                        tag=etat)
                                            pion_selectionne = False


def intersection(tev):

    if tour_jeu < 18:
        intersection_valide(tev)

    else:
        mouvement_pion(tev)

##############################################################################
# Fonction principale (jeu)                                                  #
##############################################################################

def affichage():

    fltk.cree_fenetre(FENETRE_X, FENETRE_Y)

    # Pour le fond !TEMP
    fltk.rectangle(-10, -10, 9000, 9000, remplissage='#bababa')

    interface()

    while True:

        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)

        if tev == "Quitte":
            break

        efface_intersection_survolee()
        efface_instruction()

        intersection(tev)

        affichage_tour()
        affichage_instruction()

        fltk.mise_a_jour()
    fltk.ferme_fenetre()
