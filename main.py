import pygame, sys
from pygame.locals import *

from functions import *
from constants import *
import math

pygame.init()
# Definition des FPS
fpsClock = pygame.time.Clock()

# --- Création de la fenetre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('LostColor')

initSprites()

# -------- Main Program Loop -----------
#on appele le menu principal
main_menu(screen,fpsClock)
pygame.quit()
sys.exit()
