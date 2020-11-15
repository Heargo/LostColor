import random
import pygame
from math import sqrt
from constants import *

########################################
###############ALGO 2 ##################
########################################

def randomPoints(n, size):
    """renvoie une liste de points tiré aléatoirement dans un rectangle de taile size"""
    lsPoints = []
    h = size[1]
    w = size[0]
    for i in range(n):
        x = random.randint(0, w)
        y = random.randint(0, h)
        lsPoints += [(x, y)]
    return lsPoints


def distPlusProche(p, pts):
    """Renvoie la distance entre le point p et le point le plus proche parmis les points"""
    points = pts[::]

    # on enleve p de la liste des points en cas de répétition
    if p in points:
        points.remove(p)
    # on initialise mini avec la distance au premier point de la liste des points
    mini = sqrt((p[0] - points[0][0]) ** 2 + (p[1] - points[0][1]) ** 2)
    # on compare chaque point avec p pour trouver la plus petite distance
    for p2 in points:
        dist = sqrt((p2[0] - p[0]) ** 2 + (p2[1] - p[1]) ** 2)
        if dist < mini:
            mini = dist

    return round(mini)


def randomHomogenePoints(n):
    """renvoie une liste de points qui sont répartis homogénement (a plus de 300px les uns des autres) mais aléatoirement """
    res = []
    lsbase = []
    for i in range(n):
        randomX = random.randint(0, SCREEN_WIDTH)
        randomY = random.randint(0, SCREEN_HEIGHT)
        if len(lsbase) > 1:
            while distPlusProche((randomX, randomY), lsbase) < 300:
                randomX = random.randint(0, SCREEN_WIDTH)
                randomY = random.randint(0, SCREEN_HEIGHT)

        lsbase += [(randomX, randomY)]
    return lsbase


def drawTache(screen, tache):
    # draw circles
    for cercle in tache[0]:
        centre = cercle[0]
        rayon = cercle[1]
        pygame.draw.circle(screen, tache[1], centre, rayon)


def createTache(taille):
    n = random.randint(taille[0], taille[1])
    lsCenters = randomPoints(n, (200, 200))
    lsCircles = []
    tot = (0, 0)
    for c in lsCenters:
        rayon = distPlusProche(c, lsCenters)
        tot = (tot[0] + c[0], tot[1] + c[1])
        lsCircles += [[c, rayon]]
    color = random.choice(COLORS)
    return [lsCircles, color]


def createNTaches(n, taille):
    lsTaches = []
    # on créer les taches
    for i in range(n):
        lsTaches += [createTache(taille)]
    # on créer une disposition aléatoire sur la map
    points = randomHomogenePoints(n)
    # on applique cette position a chaque tache
    for i in range(len(lsTaches)):
        tache = lsTaches[i][0]
        pos = points[i]
        for cercle in tache:
            cercle[0] = (cercle[0][0] + pos[0], cercle[0][1] + pos[1])
        lsTaches[i][0] = tache

    return lsTaches


def drawAllTaches(screen, taches):
    for tache in taches:
        drawTache(screen, tache)