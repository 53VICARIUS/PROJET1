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

    if moulin_cree:
        joueur = tour_joueur(tour_jeu - 1)

        fltk.cercle(FENETRE_X - FENETRE_X // 3,
                    FENETRE_Y - FENETRE_Y // 6.75,
                    50,
                    couleur=joueur,
                    remplissage=joueur,
                    tag='pion_joueur_actif')

    else:
        joueur = tour_joueur(tour_jeu)

        fltk.cercle(FENETRE_X - FENETRE_X // 3,
                    FENETRE_Y - FENETRE_Y // 6.75,
                    50,
                    couleur=joueur,
                    remplissage=joueur,
                    tag='pion_joueur_actif')


def affichage_instruction():

    if moulin_cree:
        # Création de l'instruction
        fltk.texte(FENETRE_X - FENETRE_X // 2,
                   FENETRE_Y - FENETRE_Y // 1.1,
                   chaine='CHOISISSEZ UN PION À SUPPRIMER',
                   taille=34,
                   ancrage='center',
                   tag='instruction')

    # tour_jeu sera inférieur à 18 durant tout le long de la phase 1 (car
    # 18 pions n'auront pas été posés
    elif tour_jeu < 18:

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


def texte_interface():

    efface_intersection_survolee()
    efface_instruction()

    affichage_tour()
    affichage_instruction()


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

def get_joueur_etat(etat):

    joueur = etat.split('_')[1]
    return joueur


def moulin():

    global moulin_cree, tour_jeu, cooldown

    if cooldown == 0:

        for cle in dico_plateau:
            etat = dico_plateau[cle]

            if isinstance(etat, str):
                x, y = cle
                joueur = get_joueur_etat(etat)
                liste_voisins = dico_adjacence[cle]

                for voisin in liste_voisins:
                    etat2 = dico_plateau[voisin]

                    if isinstance(etat2, str):
                        x2, y2 = voisin
                        joueur_voisin = get_joueur_etat(etat2)

                        if joueur == joueur_voisin:
                            cle2 = voisin
                            liste_voisins = dico_adjacence[cle2]

                            for voisin2 in liste_voisins:
                                if voisin2 != cle:
                                    etat3 = dico_plateau[voisin2]

                                    if isinstance(etat3, str):
                                        x3, y3 = voisin2
                                        joueur_voisin2 = get_joueur_etat(etat3)

                                        if joueur == joueur_voisin2:
                                            if x == x2 == x3 \
                                            or y == y2 == y3:
                                                moulin_cree = True
                                                cooldown += 1



def supprime_pion(tev):

    global moulin_cree, tour_jeu

    cle = get_pion()
    joueur = tour_joueur(tour_jeu - 1)

    if type(cle) is tuple:
        etat = dico_plateau[cle]

        if joueur != etat.split('_')[1]:
            x, y = cle

            if intersection_survolee(x, y, RAYON_PION):
                fltk.cercle(x, y, RAYON_INTERSECTION * 2,
                            couleur='green',
                            epaisseur=5,
                            tag='point_survolé')

                if tev == "ClicGauche":
                    fltk.efface(etat)
                    dico_plateau[cle] = False
                    moulin_cree = False
                    tev = None


def deplacement_possible(liste_voisins):

    cpt = 0
    nombre_voisins = len(liste_voisins)

    for voisin in liste_voisins:
        etat = dico_plateau[voisin]
        if isinstance(etat, str):
            cpt += 1

    if cpt == nombre_voisins:
        return False
    else:
        return True


def get_liste_coordonnees_pions():

    liste_coordonnees_pions = []
    for cle in dico_plateau:
        etat = dico_plateau[cle]
        if isinstance(etat, str):
            liste_coordonnees_pions.append(cle)

    return liste_coordonnees_pions


def get_pion():

    liste_coordonnees_pions = get_liste_coordonnees_pions()
    for coordonnee in liste_coordonnees_pions:
        x, y = coordonnee

        if intersection_survolee(x, y, RAYON_PION):
            return coordonnee


def moulins():

    dd = 2

##############################################################################
# Fonctions chargées des interactions avec l'interface                       #
##############################################################################

def intersection_survolee(x, y, rayon):

    if fltk.abscisse_souris() > x - rayon \
    and fltk.ordonnee_souris() > y - rayon \
    and fltk.abscisse_souris() < x + rayon \
    and fltk.ordonnee_souris() < y + rayon:
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

    global tour_jeu, cooldown

    for cle in dico_plateau:
        x, y = cle
        etat = dico_plateau[cle]

        if intersection_survolee(x, y, RAYON_INTERSECTION) \
        and not isinstance(etat, str):
            fltk.cercle(x, y, RAYON_INTERSECTION,
                        couleur='blue',
                        remplissage='blue',
                        tag='point_survolé')

            if tev == "ClicGauche":
                cree_pion(cle, x, y)
                tour_jeu += 1

                if cooldown != 0:
                    cooldown -= 1

                print(tour_jeu)
                print(dico_plateau)


def mouvement_pion(tev):

    global dico_plateau, pion_selectionne, tour_jeu, coord_pion_selectionne

    joueur = tour_joueur(tour_jeu)

    if not pion_selectionne:
        cle = get_pion()

    elif pion_selectionne:
        cle = coord_pion_selectionne


    if type(cle) is tuple:
        etat = dico_plateau[cle]
        liste_voisins = dico_adjacence[cle]

        if joueur == etat.split('_')[1]:
            x, y = cle

            if not pion_selectionne:
                if intersection_survolee(x, y, RAYON_PION) \
                and not deplacement_possible(liste_voisins):
                    fltk.cercle(x, y, RAYON_INTERSECTION * 2,
                                couleur='red',
                                epaisseur=5,
                                tag='point_survolé')

                elif intersection_survolee(x, y, RAYON_PION) \
                and deplacement_possible(liste_voisins):
                    fltk.cercle(x, y, RAYON_INTERSECTION * 2,
                                couleur='green',
                                epaisseur=5,
                                tag='point_survolé')

                    if tev == "ClicGauche":
                        fltk.cercle(x, y, RAYON_INTERSECTION * 2,
                                    couleur='green',
                                    remplissage='green',
                                    tag='pion_sélectioné')
                        pion_selectionne = True
                        tev = None

            if pion_selectionne:
                coord_pion_selectionne = cle

                for i in range(len(liste_voisins)):
                    voisin = liste_voisins[i]
                    x2, y2 = voisin
                    etat2 = dico_plateau[voisin]

                    if isinstance(etat2, bool):
                        fltk.cercle(x2, y2, RAYON_INTERSECTION,
                                    couleur='green',
                                    remplissage='green',
                                    tag='coups_possibles')

                    if intersection_survolee(x2, y2, RAYON_INTERSECTION):
                        fltk.cercle(x2, y2,
                                    RAYON_INTERSECTION,
                                    couleur='blue',
                                    remplissage='blue',
                                    tag='point_survolé')

                        if tev == "ClicGauche":
                            dico_plateau[cle] = False
                            dico_plateau[voisin] = etat
                            fltk.efface('coups_possibles')
                            fltk.efface('pion_sélectioné')
                            fltk.efface(etat)
                            fltk.cercle(x2, y2, RAYON_PION,
                                        couleur=joueur,
                                        remplissage=joueur,
                                        tag=etat)
                            pion_selectionne = False
                            tev = None
                            tour_jeu += 1


def intersection(tev):

    if moulin_cree:
        supprime_pion(tev)

    elif tour_jeu < 18:
        intersection_valide(tev)

    else:
        if moulin_cree:
            supprime_pion(tev)

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

        moulin()
        texte_interface()
        intersection(tev)

        fltk.mise_a_jour()
    fltk.ferme_fenetre()
