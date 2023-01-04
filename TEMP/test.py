import fltk
from variables import *

carre_clique = False

fltk.cree_fenetre(FENETRE_X, FENETRE_Y)

fltk.rectangle(100, 100, 200, 200, couleur='green', remplissage='green')

fltk.rectangle(300, 200, 400, 300, couleur='red', remplissage='red')
fltk.rectangle(400, 300, 500, 400, couleur='blue', remplissage='blue')


while True:

    ev = fltk.donne_ev()
    tev = fltk.type_ev(ev)

    if tev == "Quitte":
        break

    if fltk.abscisse_souris() > 100 \
    and fltk.ordonnee_souris() > 100 \
    and fltk.abscisse_souris() < 200 \
    and fltk.ordonnee_souris() < 200:

        if tev == "ClicGauche":
            fltk.rectangle(100, 100, 200, 200, couleur='yellow',
                                               epaisseur=10,
                                               tag='clic')
            carre_clique = True

    if carre_clique:

        # Carré rouge
        if fltk.abscisse_souris() > 300 \
        and fltk.ordonnee_souris() > 200 \
        and fltk.abscisse_souris() < 400 \
        and fltk.ordonnee_souris() < 300:

            if tev == "ClicGauche":
                fltk.rectangle(100, 100, 200, 200, couleur='red',
                               remplissage='red')
                fltk.efface('clic')

        # Carré bleu
        if fltk.abscisse_souris() > 400 \
        and fltk.ordonnee_souris() > 300 \
        and fltk.abscisse_souris() < 500 \
        and fltk.ordonnee_souris() < 400:

            if tev == "ClicGauche":
                fltk.rectangle(100, 100, 200, 200, couleur='blue',
                               remplissage='blue')
                fltk.efface('clic')






    fltk.mise_a_jour()
fltk.ferme_fenetre()


