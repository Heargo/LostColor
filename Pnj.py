import pygame
from constants import *
from Dialog_Box import *
from pygame.locals import *
from random import randint
from inventaire import Inventory
from Items import createRandomItem

class PNJ(pygame.sprite.Sprite):
    def __init__(self, name):
        # Appel du constructeur de la classe mère (Sprite)
        super().__init__()
        self.name = name

        self.dialog = "Dialogue par défaut blablabla"
        self.dialog_box = Dialog_Box(self.dialog, self.name)

    def say(self,newDialog):
        self.dialog = newDialog
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

        self.dialog = "Bonjour aventurier ! J'espère que vous trouverez votre bonheur dans ma boutique. Regardez ce que j'ai à vendre :"
        self.dialog_box = Dialog_Box(self.dialog, self.name)

        
        self.money = randint(500,1000)
        self.inventaire = Inventory(64)
        self.init_inventaire()

    def init_inventaire(self):
        for i in range(10):
            self.inventaire.add(createRandomItem())



class Instructor(PNJ):
    def __init__(self, name, x = SCREEN_WIDTH//2, y = SCREEN_HEIGHT//2):
        # Appel du constructeur de la classe mère (Sprite)
        super().__init__(name)
        # Mise en place de l'image du pnj
        self.image = pygame.image.load('img/pnjs/instructor.png')

        # Mise en place de la "hit-box" du pnj
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

        self.dialog = "Je suis l'instructeur " + "AAA" * 500
        self.dialog_box = Dialog_Box(self.dialog, self.name)




