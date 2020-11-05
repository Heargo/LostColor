import pygame
from constants import *
from pygame.locals import *
from Ennemis import *
from Wall import *

class Room(object):

    doors_close = True

    def __init__(self):
        """Chaque salle a une liste de monstre, de murs et de portes"""
        self.wall_list = pygame.sprite.Group()
        self.door_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()


class RoomTuto(Room):
    """Crée tous les murs portes et monstre de la salle tuto"""

    def __init__(self, player):
        super().__init__()
        # Création d'un monstre
        m1 = Monstre1(random.randint(0, SCREEN_WIDTH),
                      random.randint(0, SCREEN_HEIGHT // 3),
                      player)

        # Ajout du monstre sprite dans le Group enemy_list
        self.enemy_list.add(m1)

        # Création des murs.

        wall_size = 20
        door_length = 100
        vertical_wall_height = (SCREEN_HEIGHT//2)-(door_length//2)
        horizontal_wall_width = (SCREEN_WIDTH//2)-(door_length//2)
        # La liste des murs. Les murs sont sont la forme [x, y, width, height, color]
        self.walls = [[0, 0, wall_size, vertical_wall_height, BLACK],  # Mur de gauche
                      [0, (SCREEN_HEIGHT//2)+(door_length//2), wall_size, vertical_wall_height, BLACK],  # Mur de gauche
                      [SCREEN_WIDTH-wall_size, 0, wall_size, vertical_wall_height, BLACK],  # Mur de droite
                      [SCREEN_WIDTH-wall_size, (SCREEN_HEIGHT//2)+(door_length//2), wall_size, vertical_wall_height, BLACK],  # Mur de droite
                      [0, 0, horizontal_wall_width, wall_size, BLACK],  # Mur du haut
                      [(SCREEN_WIDTH//2)+(door_length//2), 0, horizontal_wall_width, wall_size, BLACK],  # Mur du haut
                      [0, SCREEN_HEIGHT-wall_size, SCREEN_WIDTH, wall_size, BLACK],  # Mur du bas
                      #[SCREEN_WIDTH//3, SCREEN_HEIGHT//2, SCREEN_WIDTH//3, wall_size, GRAY]  # Mur du milieu test
                      ]

        self.doors = [[0, vertical_wall_height, wall_size, door_length, BROWN],  # Porte de gauche
                      [SCREEN_WIDTH-wall_size, vertical_wall_height, wall_size, door_length, BROWN],  # Porte du droite
                      [horizontal_wall_width, 0, door_length, wall_size, BROWN]  # Porte de haut
                      ]

        # Création du mur avec le contructeur et ajout dans la liste
        for item in self.walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        # Création de morte avec le contructeur et ajout dans la liste
        for item in self.doors:
            door = Wall(item[0], item[1], item[2], item[3], item[4])
            self.door_list.add(door)
            self.wall_list.add(door)

    def open_doors(self):
        if self.doors_close == True:
            self.doors_close = False

    def close_doors(self):
        if self.doors_close == False:
            self.doors_close = True

    def update(self):
        """Gestion d'ouverture fermeture des portes"""
        if len(self.enemy_list) == 0:
            self.open_doors()

        if self.doors_close and len(self.door_list) == 0:
            for item in self.doors:
                doors = Wall(item[0], item[1], item[2], item[3], item[4])
                self.door_list.add(doors)
                self.wall_list.add(doors)
        if (not self.doors_close) and len(self.door_list) != 0:
            for door in self.door_list:
                door.kill()