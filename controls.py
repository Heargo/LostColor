# Controles
C_EXCEPTION = [32,273,274,275,276,9, 306, 304, 308]
C_EXCEPTION_CONVERT = {32 : "espace",
                       273 : "flèche haut",
                       274 : "flèche bas",
                       275 : "fleche droite",
                       276: "flèche gauche",
                       9: "tab",
                       306 : "ctrl",
                       304 : "shift",
                       308 : "alt"
                       }
C_HAUT = 119
C_BAS = 115
C_GAUCHE = 97
C_DROITE = 100
C_PARLER = 32
C_MANGER = 101
C_INVENTAIRE = 105
C_CARTE = 9
C_CRAFT = 114
affichageTouche = {"HAUT" : 'z',
                   "BAS" : 's',
                   "GAUCHE" : 'q',
                   "DROITE" : 'd',
                   "PARLER" : 'espace',
                   "CRAFT" : 'r',
                   "MANGER" : 'e',
                   "INVENTAIRE" : 'i',
                   "CARTE" : "tab"}


def binder(touche_a_bind, key_code, key_char):
    """Procedure qui bind une touche"""
    global C_HAUT, C_BAS, C_GAUCHE, C_DROITE, C_PARLER, C_CRAFT, C_MANGER, C_INVENTAIRE, C_CARTE

    if touche_a_bind == "HAUT":
        C_HAUT = key_code
    elif touche_a_bind == "BAS":
        C_BAS = key_code
    elif touche_a_bind == "GAUCHE":
        C_GAUCHE = key_code
    elif touche_a_bind == "DROITE":
        C_DROITE = key_code
    elif touche_a_bind == "PARLER":
        C_PARLER = key_code
    elif touche_a_bind == "CRAFT":
        C_CRAFT = key_code
    elif touche_a_bind == "MANGER":
        C_MANGER = key_code
    elif touche_a_bind == "INVENTAIRE":
        C_INVENTAIRE = key_code
    elif touche_a_bind == "CARTE":
        C_CARTE = key_code

    touche_a_affiche = key_char
    if key_code in C_EXCEPTION:
        touche_a_affiche = C_EXCEPTION_CONVERT[key_code]
    affichageTouche[touche_a_bind] = touche_a_affiche
