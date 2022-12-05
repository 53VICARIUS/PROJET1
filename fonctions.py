import fltk


def plateau_de_jeu_9(version, taille_fenetre):

    '''
    Pour taille_fenetre = 600 :
    taille_fenetre // 2 = 300
    taille_fenetre // 3 = 200
    (taille_fenetre // 3) * 2 = 400
    taille_fenetre // 6 = 100 (<- à changer car '6' dépend de '600' et non de
    taille_fenetre).
    '''

    liste_points_possibles = []
    rayon = 5
    epaisseur_trait = 3

    # Création des lignes
    fltk.ligne(taille_fenetre // 2, 0, taille_fenetre // 2,
               taille_fenetre // 3,
               epaisseur=epaisseur_trait,
               couleur="blue")
    fltk.ligne(0, taille_fenetre // 2, taille_fenetre // 3,
               taille_fenetre // 2,
               epaisseur=epaisseur_trait,
               couleur="red")
    fltk.ligne(taille_fenetre, taille_fenetre // 2, (taille_fenetre // 3) * 2,
               taille_fenetre // 2,
               epaisseur=epaisseur_trait,
               couleur="black")
    fltk.ligne(taille_fenetre // 2, taille_fenetre, taille_fenetre // 2,
               (taille_fenetre // 3) * 2,
               epaisseur=epaisseur_trait,
               couleur="yellow")

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

    print(liste_points_possibles)
    return liste_points_possibles


def intersection(liste_points_possibles, ev):

    rayon = 5

    for i in range(len(liste_points_possibles)):
        x_point, y_point = liste_points_possibles[i]

        if fltk.abscisse(ev) > x_point - rayon \
        and fltk.ordonnee_souris() > y_point - rayon \
        and fltk.abscisse(ev) < x_point + rayon \
        and fltk.ordonnee_souris() < y_point + rayon:
            print('intersection')


def affichage():

    taille_fenetre = 600
    fltk.cree_fenetre(taille_fenetre, taille_fenetre)
    # Pour le fond
    fltk.rectangle(-10, -10, 1000, 1000, remplissage='#bababa')

    liste_points_possibles = plateau_de_jeu_9('A', taille_fenetre)

    continuer = True
    while continuer:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)

        if tev == "Quitte":
            continuer = False

        if tev == "ClicGauche":
            intersection(liste_points_possibles, ev)
            print(fltk.abscisse(ev), fltk.ordonnee(ev))

        fltk.mise_a_jour()

    fltk.ferme_fenetre()
