import pygame, math, random
from constants import *
from pygame.locals import *
from random import randint

class Monstre1(pygame.sprite.Sprite):
    """ Cette classe represente les objets Monstre1"""

    def __init__(self, spawn_x, spawn_y, target):
        """ Constructeur.
        spawn_x et spawn_ y sont les coordonés d'aparition du monstre
        """
        # Appel du constructeur de la classe mère (Sprite)
        super().__init__()

        #la couleur du monstre est tiré
        num=randint(0,len(COLORS)-1)
        color = COLORS[num]


        #Mise en place de l'image du monstre
        self.image = pygame.image.load('img/blob_'+str(num+1)+'.png')

        # Mise en place de la "hit-box" du monstre
        self.rect = self.image.get_rect()

        # Mise en place de la cible du monstre
        self.target = target
        
        # Met le monstre au coordonées d'apparition mit en entrée
        self.rect.x = spawn_x
        self.rect.y = spawn_y
        
        # Statistiques du monstre
        self.HP_MAX = 20
        self.HP = self.HP_MAX
        self.DMG = 10
        self.speed = random.uniform(2.0, 3.0)
        self.colorbuff=color

        #si il est boost
        self.isboosted=False

        # Taille bare point de vie :
        self.HP_BAR_WIDTH = self.rect.width
        self.HP_BAR_HEIGHT = self.rect.height / 4

        # rect.x and rect.y sont convertit automatiquement en
        # entiers, on doit créer des variables flotant pour
        # pour contenir les coordonées flotante. Les
        # coordonées entieres ne fournissent pas assez de precision
        # pour la "visé".
        self.floating_point_x = self.rect.centerx
        self.floating_point_y = self.rect.centery


    def setColor(self,color):
        self.colorbuff=color
        if color!=GRAY:
            num = COLORS.index(color)
            self.image = pygame.image.load('img/blob_'+str(num+1)+'.png')
        else:
            self.image = pygame.image.load('img/blob_0.png')

    def calc_angle(self):
        """ Calcul de l'angle"""
        # Créations des coordonées de destination avec le
        # le joueur en entrée
        dest_x = self.target.rect.centerx
        dest_y = self.target.rect.centery

        # Calcul de l'angle en radian entre les coordonées du monstre
        # et le point qu'il vise.
        x_diff = dest_x - self.rect.centerx
        y_diff = dest_y - self.rect.centery
        angle = math.atan2(y_diff, x_diff);

        return angle

    def hp_bar(self):
        """"""
        HP_BAR_STATE = (self.HP * self.rect.width) / self.HP_MAX
        pygame.draw.rect(self.image, RED, (0, 0, self.HP_BAR_WIDTH, self.HP_BAR_HEIGHT))
        pygame.draw.rect(self.image, GREEN, (0, 0, HP_BAR_STATE, self.HP_BAR_HEIGHT))


    def update(self):
        """ Déplacement et condition de mort du monstre et affichage barre de vie. """
        # Appel de la méthode pour calculer l'angle
        angle = self.calc_angle()

        # En prenant en compte l'angle on calcul change_x
        # et change_y. La Velocity est la vitesse du monstre.
        
        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed
        
        # Les points flotant x et y donne une position plus precise.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
 
        # On convertit ces valeur en entier pour rect.x
        # et rect.y pour déplacer le monstre
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        #Calculs et affichage de la bare de point de vie


        self.hp_bar()

        # Si le monstre a ses HP en dessous de 0 appel la fonction sprite.kill()
        # ce qui le retire de tous les Groupes (all_sprite_list,...)
        if self.HP <= 0:
            self.kill()

