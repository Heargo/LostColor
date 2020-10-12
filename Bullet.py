import pygame
import math

class Bullet(pygame.sprite.Sprite):
    """ Classe d'une balle """
 
    def __init__(self, start_x, start_y, dest_x, dest_y):
        """Constructeur"""
 
        # Utilise le constructeur du la classe sprite du pygame
        super().__init__()
 
        #visuel de la balle
        self.image = pygame.Surface([10, 10])
        self.image.fill((0,0,0))
 
        self.rect = self.image.get_rect()
 
        #Défini les coordonées
        self.rect.x = start_x
        self.rect.y = start_y
 
        # rect.x and rect.y sont des entiers
        # donc il nous faut des variables pour les float
        # (plus précis pour viser)
        self.floating_point_x = start_x
        self.floating_point_y = start_y
 
        # Calcule l'angle radians entre le point de départ et l'arrivé
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff);
 
        # Calcul du délacement en x et y en prenant en compte l'angle
        bullet_speed = 10
        self.change_x = math.cos(angle) * bullet_speed
        self.change_y = math.sin(angle) * bullet_speed
 
    def update(self):
        """ Déplace la balle """
 
        # On utilise les coordoonées en float pour plus de précision
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
 
        # Puis on change les coordonées de la hitbox.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)
 
        # Si la balle sors de l'écran, elle disparait //dans le futur, au bout d'un certain temps...
        if self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 720:
            self.kill()