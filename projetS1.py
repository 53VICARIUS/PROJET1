from fltk import *


largeur_fenetre = 1300
longueur_fenetre = 901

def creation_fenetre(x,y):
    cree_fenetre(x,y)

def table_jeu(version):
    ### Version à changer plus tard ? ###
    x=0
    epaisseur_trait = 3
    for i in range(3):
        rectangle(200+x, 3+x, 1100-x, 897-x, epaisseur=3)
        x+=150
    ligne(650,3,650,303, epaisseur=epaisseur_trait)
    ligne(650,597,650,897, epaisseur=epaisseur_trait)
    ligne(200,895/2+3,500,895/2+3, epaisseur=epaisseur_trait)
    ligne(800,895/2+3,1100,895/2+3, epaisseur=epaisseur_trait)



creation_fenetre(largeur_fenetre,longueur_fenetre)
table_jeu("A")



continuer = True
while continuer:
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "Quitte":
        continuer = False
    if tev == "ClicGauche":
        print(abscisse(ev), ordonnee(ev))

    mise_a_jour()

ferme_fenetre()
