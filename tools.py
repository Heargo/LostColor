import pygame, sys
from pygame.locals import *
from math import sqrt

def draw_text(screen,text, font_name, size, color, x, y, center):
    """"""
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.centerx = x
        text_rect.centery = y
    else:
        text_rect.x = x
        text_rect.y = y

    screen.blit(text_surface, text_rect)

def estDansPolygone(x,y,polygone):
    bool = True
    n = len(polygone)
    a = polygone[n-1][0] - x
    b = polygone[n-1][1] - y
    c = polygone[0][0] - polygone[n-1][0]
    d = polygone[0][1] - polygone[n-1][1]
    z = a*d - b*c
    if z < 0:
        s = -1
    elif z > 0:
        s = 1
    else :
        s = 0
    if s!=0:
        for i in (0, n-2):
            a = polygone[i][0] - x
            b = polygone[i][1] - y
            c = polygone[i+1][0] - polygone[i][0]
            d= polygone[i+1][1] - polygone[i][1]
            z = a*d - b*c
            if z == 0:
                break
            if z * s < 0:
                bool = False
                break
    return bool


def estDansCercle(Cercle, M):
    a = Cercle[0][0] - M[0]
    b = Cercle[0][1] - M[1]
    c=sqrt(a**2 + b**2)
    if c <= Cercle[1]:
        bool = True
    else:
        bool = False
    return bool

def estDansEnsembleCercles(ensemble,M):
    n = len(ensemble)
    bool = False
    for i in range(n):
        if estDansCercle(ensemble[i], M):
            bool = True
            break
    return bool

def to_gold(price,lang="fr",emojis="none"):
    """converted a float with 4 decimal max into gold, silver and bronze
    1.4586 = 1 gold 45 silver and 86 bronze"""
    gold = int(price//1)
    silver = int(100*(price%1))
    copper = round(((100*(price%1))%1)*100)

    if gold >0:
        Isgold=1
    else:
        Isgold=0
    if silver >0:
        Issilver=1
    else:
        Issilver=0
    if copper >0:
        Iscopper=1
    else:
        Iscopper=0



    #print(gold,"gold",silver,"silver and",copper,"copper")
    if lang=="fr":
        res = Isgold*(str(gold)+" or ")+Issilver*(str(silver)+" argent ")+Iscopper*(str(copper)+" cuivre ")
    elif lang=="eng":
        res = str(gold)+" gold "+str(silver)+" silver "+str(copper)+" copper "
    elif lang=="discord":
        res = f"{gold} {emojis[0]}  {silver} {emojis[1]}  {copper} {emojis[2]}"
    return res

def random_key(dico):
    """pick a random key of a dictionary"""
    liste=[]
    for k in dico.keys():
        liste+=[k]
    return random.choice(liste)