import pygame
from constants import *
from Dialog_Box import *
from pygame.locals import *

class PNJ(pygame.sprite.Sprite):
    def __init__(self, name):
        # Appel du constructeur de la classe mère (Sprite)
        super().__init__()
        self.name = name

        self.dialog = "Dialogue par défaut blablabla"
        self.dialog_box = Dialog_Box(self.dialog, self.name)


class Merchant(PNJ):
    def __init__(self, name, x = SCREEN_WIDTH//2, y = SCREEN_HEIGHT//2):
        # Appel du constructeur de la classe mère (PNJ)
        super().__init__(name)

        # Mise en place de l'image du pnj
        self.image = pygame.image.load('img/pnjs/merchant.png')

        # Mise en place de la "hit-box" du pnj
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

        self.dialog = "Bonjour je suis le marchand " + "bla"*500
        self.dialog_box = Dialog_Box(self.dialog, self.name)

class Instructor(PNJ):
    def __init__(self, x = SCREEN_WIDTH//2, y = SCREEN_HEIGHT//2):
        # Appel du constructeur de la classe mère (Sprite)
        super().__init__()
        # Mise en place de l'image du pnj
        self.image = pygame.image.load('img/pnjs/instructor.png')

        # Mise en place de la "hit-box" du pnj
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

        self.dialog = "Je suis l'instructeur " + "AAA" * 500
        self.dialog_box = Dialog_Box(self.dialog, self.name)




