
import fltk

rayon = 10
taille_fenetre = 1000
epaisseur_trait = 3

def plateau_de_jeu_9(version, taille_fenetre):
    '''
    Pour taille_fenetre = 600 :
    taille_fenetre // 2 = 300
    taille_fenetre // 3 = 200
    (taille_fenetre // 3) * 2 = 400
    taille_fenetre // 6 = 100 (<- à changer car '6' dépend de '600' et non de
    taille_fenetre).
    '''
    # Crée un plateau de jeu dans la version la plus classique, c'est-à-dire 9 pions/joueur et 24 cases ! #
    liste_points_possibles = []
    # Création des lignes
    fltk.ligne(taille_fenetre // 2, 0, taille_fenetre // 2,
               taille_fenetre // 3,
               epaisseur=epaisseur_trait,
               couleur="black")
    fltk.ligne(0, taille_fenetre // 2, taille_fenetre // 3,
               taille_fenetre // 2,
               epaisseur=epaisseur_trait,
               couleur="black")
    fltk.ligne(taille_fenetre, taille_fenetre // 2, (taille_fenetre // 3) * 2,
               taille_fenetre // 2,
               epaisseur=epaisseur_trait,
               couleur="black")
    fltk.ligne(taille_fenetre // 2, taille_fenetre, taille_fenetre // 2,
               (taille_fenetre // 3) * 2,
               epaisseur=epaisseur_trait,
               couleur="black")

    # 200, 100 etc sont des valeurs obtenues en divisant taille_fenetre par
    # 3 ou 6 (car taille_fenetre == 600) et doivent être remplacée par des
    # variables
    for p in range(0, taille_fenetre // 3 + 1, taille_fenetre // 6):

        # Création des carrés : 'range(3)' pour trois carrés
        for carre in range(3):
            fltk.rectangle(0 + p, 0 + p, taille_fenetre - p,
                           taille_fenetre - p,
                           epaisseur=3)

        for x in range(0 + p, taille_fenetre - p + 1,
                       taille_fenetre // 2 - p):
            for y in range(0 + p, taille_fenetre - p + 100,
                           taille_fenetre // 2 - p):

                if not (x == taille_fenetre // 2
                        and y == taille_fenetre // 2):
                    fltk.cercle(x, y, rayon,
                                couleur='black',
                                remplissage='black')

                    liste_points_possibles.append((x, y))

    return liste_points_possibles


def intersection_survolee(liste_points_possibles):

    for i in range(len(liste_points_possibles)):
        x_point, y_point = liste_points_possibles[i]          # A MODIFIER? appel de la fonction intersection() ?
        if collision(x_point, y_point):
            fltk.cercle(x_point, y_point, rayon,
                        couleur='blue',
                        remplissage='blue',
                        tag='point_survolé')
            return True

def efface_intersection_survolee():
    fltk.efface('point_survolé')


def collision(x,y):
    if fltk.abscisse_souris() > x - rayon \
    and fltk.ordonnee_souris() > y - rayon \
    and fltk.abscisse_souris() < x + rayon \
    and fltk.ordonnee_souris() < y + rayon:
        return True

    return False


def affichage_principal():

    fltk.cree_fenetre(taille_fenetre, taille_fenetre)
    # Pour le fond
    #fltk.rectangle(-10, -10, 1000, 1000, remplissage='#bababa')

    liste_points_possibles = plateau_de_jeu_9('A', taille_fenetre)

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
