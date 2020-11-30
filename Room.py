import pygame
from constants import *
from pygame.locals import *
from Ennemis import *
from Wall import *
from Bonus import *
from CreationTache import *
from Pnj import *


def salleNormale(top, bottom, left, right):
    """Retourne les murs et portes d'une salle selon ou on veut placer les portes
       top, bottom, left, right : Integer (l'id de la prochaine salle s'il y en a une)"""


    vertical_wall_height = (SCREEN_HEIGHT // 2) - (door_length // 2)
    horizontal_wall_width = (SCREEN_WIDTH // 2) - (door_length // 2)

    walls = []
    doors = []

    if top != -1:
        walls.append([0, 0, horizontal_wall_width, wall_size, BLACK])
        walls.append([(SCREEN_WIDTH // 2) + (door_length // 2), 0, horizontal_wall_width, wall_size, BLACK])

        doors.append([horizontal_wall_width, 0, door_length, wall_size, BROWN])
    else:
        walls.append([0, 0, SCREEN_WIDTH, wall_size, BLACK])

    if bottom != -1:
        walls.append([0, SCREEN_HEIGHT-wall_size, horizontal_wall_width, wall_size, BLACK])
        walls.append([(SCREEN_WIDTH // 2) + (door_length // 2), SCREEN_HEIGHT-wall_size, horizontal_wall_width, wall_size, BLACK])

        doors.append([horizontal_wall_width, SCREEN_HEIGHT-wall_size, door_length, wall_size, BROWN])
    else:
        walls.append([0, SCREEN_HEIGHT - wall_size, SCREEN_WIDTH, wall_size, BLACK])

    if right != -1:
        walls.append([SCREEN_WIDTH - wall_size, 0, wall_size, vertical_wall_height, BLACK])
        walls.append([SCREEN_WIDTH - wall_size, (SCREEN_HEIGHT // 2) + (door_length // 2), wall_size, vertical_wall_height, BLACK])

        doors.append([SCREEN_WIDTH - wall_size, vertical_wall_height, wall_size, door_length, BROWN])
    else:
        walls.append([SCREEN_WIDTH - wall_size, 0, wall_size, SCREEN_HEIGHT, BLACK])

    if left != -1:
        walls.append([0, 0, wall_size, vertical_wall_height, BLACK])
        walls.append([0, (SCREEN_HEIGHT // 2) + (door_length // 2), wall_size, vertical_wall_height, BLACK])

        doors.append([0, vertical_wall_height, wall_size, door_length, BROWN])
    else:
        walls.append([0, 0, wall_size, SCREEN_HEIGHT, BLACK])

    room = (walls, doors)

    return room

class Room(object):

    doors_close = True

    def __init__(self, player, id, top=-1, bottom=-1, left=-1, right=-1, difficulty="none"):
        """Chaque salle a une liste de monstre, de murs et de portes"""
        self.wall_list = pygame.sprite.Group()
        self.door_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.pnj_list = pygame.sprite.Group()
        self.taches = createNTaches(random.randint(3, 10), (6, 20))

        self.id = id
        self.doors_id = {"top": top, "bottom": bottom, "left": left, "right": right}
        self.difficulty = difficulty
        self.visited=False
        # Bonus de la salle
        self.bonus = Bonus(BONUS_TYPE[randint(0, 5)], player)
        #liste des items sur le sol de la salle
        self.loots=pygame.sprite.Group()
        # Création d'un monstre
        self.spawnMonsters(difficulty, player)

        # Création des murs avec la methode walls_creation() et ajout dans la liste
        self.walls_creation()
        # Création des portes avec la methode doors_creation() et ajout dans la liste
        self.doors_creation()

        # Creation du pnj si la sallest peacfull
        self.create_pnj()

    def walls_creation(self):
        # Création de la liste des murs
        # Les murs sont sont la forme [x, y, width, height, color]
        self.walls = salleNormale(self.doors_id["top"],
                                  self.doors_id["bottom"],
                                  self.doors_id["left"],
                                  self.doors_id["right"])[0]

        self.wall_list.empty()  # On supprime les anciens murs
        for item in self.walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])  # Appel du constructeur Wall()
            self.wall_list.add(wall)

    def doors_creation(self):
        # Création de la liste des portes
        # Les portes sont sont la forme [x, y, width, height, color]
        self.doors = salleNormale(self.doors_id["top"],
                                  self.doors_id["bottom"],
                                  self.doors_id["left"],
                                  self.doors_id["right"])[1]

        self.door_list.empty()  # On supprime les anciens portes
        for item in self.doors:
            door = Wall(item[0], item[1], item[2], item[3], item[4])  # Appel du constructeur Wall()
            self.door_list.add(door)
            self.wall_list.add(door)

    def doorsPossibleToOpen(self):
        lsDoors = []
        for k in self.doors_id.keys():
            if self.doors_id[k] == -1:
                lsDoors += [k]
        return lsDoors

    def openDoorFromPreviousRoom(self, previousRoom):
        res = "none"
        for k in previousRoom.doors_id:
            if previousRoom.doors_id[k] == self.id:
                res = k
        relationDoors = {"top": "bottom", "bottom": "top", "left": "right", "right": "left"}
        self.doors_id[relationDoors[res]] = previousRoom.id

    def spawnMonsters(self, difficulty, target, N=0, color="none"):
        """Cette fonction fait appraitre N enemies"""
        if difficulty == "peaceful":
            num_of_monsters = 0
        elif difficulty == "ultra_easy":
            num_of_monsters = 1
        elif difficulty == "easy":
            num_of_monsters = 2
        elif difficulty == "medium":
            num_of_monsters = 3
        elif difficulty == "hard":
            num_of_monsters = randint(5, 9)
        elif difficulty == "ultra_hard":
            num_of_monsters = randint(12, 20)
        else:
            num_of_monsters = 0 + N

        for i in range(0, num_of_monsters):
            monstre = Monstre1(random.randint(0, SCREEN_WIDTH),
                               random.randint(0, SCREEN_HEIGHT // 3),
                               target)
            if color != "none":
                monstre.setColor(color)
            self.enemy_list.add(monstre)



    def open_doors(self):
        if self.doors_close == True:
            self.doors_close = False

    def close_doors(self):
        if self.doors_close == False:
            self.doors_close = True

    def create_pnj(self):
        """Méthode ajoutant un PNJ a la pnj_list"""

        if self.difficulty == "peaceful":
            pnj = Merchant("Boby")
            self.pnj_list.add(pnj)

    def update(self):
        """Gestion d'ouverture fermeture des portes"""
        if len(self.enemy_list) == 0:
            self.open_doors()

        if self.doors_close and len(self.door_list) == 0:  # Gestion de la fermeture
            self.doors_creation()
        if (not self.doors_close) and len(self.door_list) != 0:  # Gestion de l'ouverture
            for door in self.door_list:
                door.kill()