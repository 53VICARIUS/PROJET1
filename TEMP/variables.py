# Constantes relatives à l'interface #
FENETRE_X = 900  # Dimension de la fenêtre sur l'axe x
FENETRE_Y = 600  # Dimension de la fenêtre sur l'axe y
TAILLE_PLATEAU = 300  # Longueur des côtés du plateau
EPAISSEUR_LIGNE = 2  # Epaisseur des lignes des éléments de l'interface
RAYON_INTERSECTION = 5  # Rayon des points situés aux intersections du plateau
RAYON_PION = 10

# Variables relatives au jeu #
liste_intersections = []  # Cf doc
liste_coups_possibles = []  # Cf doc
liste_pions_blanc = []
liste_pions_noir = []
tour_jeu = 0
pions_blancs = 0
pions_noirs = 0
pion_selectione = False
dico_adjacence = {
    (300, 120): [(450, 120), (300, 270)],
    (450, 120): [(300, 120), (450, 170), (600, 120)],
    (600, 120): [(450, 120), (600, 270)],
    (350, 170): [(450, 170), (350, 270)],
    (450, 170): [(450, 120), (350, 170), (550, 170), (450, 220)],
    (550, 170): [(450, 170), (550, 270)],
    (400, 220): [(400, 270), (450, 220)],
    (450, 220): [(400, 220), (450, 170), (500, 220)],
    (500, 220): [(450, 220), (500, 270)],
    (300, 270): [(300, 120), (350, 270), (300, 420)],
    (350, 270): [(300, 270), (350, 170), (400, 270), (350, 370)],
    (400, 270): [(400, 220), (350, 270), (400, 320)],
    (500, 270): [(500, 220), (550, 270), (500, 320)],
    (550, 270): [(500, 270), (550, 170), (600, 270), (550, 370)],
    (600, 270): [(600, 120), (550, 270), (600, 420)],
    (400, 320): [(400, 270), (450, 320)],
    (450, 320): [(400, 320), (500, 320), (450, 370)],
    (500, 320): [(450, 320), (500, 270)],
    (350, 370): [(350, 270), (450, 370)],
    (300, 420): [(300, 270), (450, 420)],
    (450, 420): [(300, 420), (450, 370), (600, 420)],
    (600, 420): [(450, 420), (600, 270)]}