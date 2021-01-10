import pygame, math, random
from constants import *
from pygame.locals import *
from random import randint
from inventaire import generateLoot
from Bullet import Bullet

class Monstre1(pygame.sprite.Sprite):
    """ Cette classe represente les objets Monstre1"""

    def __init__(self, spawn_x, spawn_y, target,lvl=1):
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
        self.originalImage=self.image
        # Mise en place de la "hit-box" du monstre
        self.rect = self.image.get_rect()

        # Mise en place de la cible du monstre
        self.target = target
        
        # Met le monstre au coordonées d'apparition mit en entrée
        self.rect.x = spawn_x
        self.rect.y = spawn_y
        
        # Statistiques du monstre #stat = lvl*statMax/lvlMax
        self.lvl=lvl
        self.HP_MAX = 4*(self.lvl*500/MONSTER_LEVEL_MAX)
        self.HP = self.HP_MAX
        self.DMG = 2*(self.lvl*80/MONSTER_LEVEL_MAX)
        self.speed = random.uniform(1.5, 2.8)
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
            self.originalImage=self.image
        else:
            self.image = pygame.image.load('img/blob_0.png')
            self.originalImage=self.image

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

    def hp_bar(self,):
        """"""
        HP_BAR_STATE = (self.HP * self.rect.width) / self.HP_MAX
        pygame.draw.rect(self.image, RED2, (0, 0, self.HP_BAR_WIDTH, self.HP_BAR_HEIGHT))
        pygame.draw.rect(self.image, GREEN2, (0, 0, HP_BAR_STATE, self.HP_BAR_HEIGHT))


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
    
    def checkdead(self,loots_list,all_sprites_list,lootEnable):
        res=False
        money=0
        if self.HP <=0 and self.colorbuff!=GRAY and randint(0,100)<=LOOTPOURCENTAGE and lootEnable:
            generateLoot(self.rect.x,self.rect.y,loots_list,all_sprites_list)
        if self.HP <=0 and lootEnable:
            if self.colorbuff!=GRAY:
                money = 0.05+((self.lvl*randint(1,10))/20)
            else:
                money = 0.05
        if self.HP <=0:
            res=True
        return res,money

class Boss1(pygame.sprite.Sprite):
    """ Cette classe represente le premier Boss"""

    def __init__(self, target):
        # Appel du constructeur de la classe mère (Sprite)
        super().__init__()

        # --- Tous ces atributs sont initialisés dans le classes filles ---
        self.image = None

        self.rect = None

        self.HP_MAX = None
        self.HP = None
        self.DMG = None
        self.colorbuff = None
        self.speed = None
        # -----------------------------------------------------------------

        # Mise en place de la cible du boss
        self.target = target

        # Liste des balle pour gerer les tirs du boss
        self.bullet_list = pygame.sprite.Group()

        # Phase du boss
        self.phase_no = 1

        self.phase = None

    def move(self, walls):
        pass

    def hp_bar(self, surface):
        """"""
        # Taille bare point de vie :
        HP_BAR_WIDTH = SCREEN_WIDTH-100
        HP_BAR_HEIGHT = 50

        HP_BAR_STATE = (self.HP * HP_BAR_WIDTH) / self.HP_MAX
        pygame.draw.rect(surface, RED2, (25, SCREEN_HEIGHT-25, HP_BAR_WIDTH, HP_BAR_HEIGHT))
        pygame.draw.rect(surface, GREEN2, (25, SCREEN_HEIGHT-25, HP_BAR_STATE, HP_BAR_HEIGHT))

class Boss1P1(Boss1):
    """ Cette classe represente la phase 1 du boss 1"""

    def __init__(self, target, x, y):
        super().__init__(target)
        # Mise en place de l'image du boss
        self.image = pygame.image.load('img/boss1P1.png')

        # Mise en place de la "hit-box" du boss
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        # Statistiques du monstre
        self.HP_MAX = 600
        self.HP = self.HP_MAX
        self.DMG = 30
        self.colorbuff = BLACK
        self.speed = 3

        self.shot_speed = 7
        self.shoot_cd_max = 20
        self.shoot_cd = 20

        self.shot_phase = 1
        self.shoot_phase_cd = 0
        self.shoot_phase_cd_max = 160
        self.do_cardinal_shoot = True

        self.move_cd = 0
        self.move_cd_max = 75
        self.move_nb_rand = 1

    def move(self, walls):
        if self.move_cd == self.move_cd_max:
            self.move_nb_rand = randint(1, 4)
            self.move_cd = 0

        if self.move_nb_rand == 1: # Déplacement en haut
            self.rect.y -= self.speed
        elif self.move_nb_rand == 2: # Déplacement en bas
            self.rect.y += self.speed
        elif self.move_nb_rand == 3: # Déplacement a gauche
            self.rect.x -= self.speed
        elif self.move_nb_rand == 4: # Déplacement a droite
            self.rect.x += self.speed

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # Si le boss se déplace en direction d'un mur, cela
            # met le coté du boss qui touche le mur sur le coté
            # du mur touché
            if self.move_nb_rand == 4:
                self.rect.right = block.rect.left
            elif self.move_nb_rand == 3:
                self.rect.left = block.rect.right
            elif self.move_nb_rand == 2:
                self.rect.bottom = block.rect.top
            elif self.move_nb_rand == 1:
                self.rect.top = block.rect.bottom

        self.move_cd += 1



    def cardinal_shoot(self):
        top_bullet = Bullet(self, self.rect.centerx, self.rect.top, BLACK)
        bottom_bullet = Bullet(self, self.rect.centerx, self.rect.bottom, BLACK)
        right_bullet = Bullet(self, self.rect.right, self.rect.centery, BLACK)
        left_bullet = Bullet(self, self.rect.left, self.rect.centery, BLACK)

        self.bullet_list.add(top_bullet, bottom_bullet, right_bullet, left_bullet)

    def diagonal_shoot(self):
        top_right_bullet = Bullet(self, self.rect.right, self.rect.top, BLACK)
        top_left_bullet = Bullet(self, self.rect.left, self.rect.top, BLACK)
        bottom_right_bullet = Bullet(self, self.rect.right, self.rect.bottom, BLACK)
        bottom_left_bullet = Bullet(self, self.rect.left, self.rect.bottom, BLACK)

        self.bullet_list.add(top_right_bullet, top_left_bullet, bottom_right_bullet, bottom_left_bullet)

    def target_shoot(self):
        target_bullet = Bullet(self, self.target.rect.centerx, self.target.rect.centery, BLACK)

        self.bullet_list.add(target_bullet)


    def update(self):
        if self.shoot_phase_cd == self.shoot_phase_cd_max:
            self.shot_phase = randint(1,4)
            self.shoot_phase_cd = 0

            # Si paterne de tire regulier
            #self.shot_phase = (self.shot_phase + 1)
            #if self.shot_phase > 4:
            #    self.shot_phase = 1
            #self.shoot_phase_cd = 0

        if self.shot_phase == 1:
            if self.shoot_cd == self.shoot_cd_max:
                self.cardinal_shoot()
                self.shoot_cd = 0
        if self.shot_phase == 2:
            if self.shoot_cd == self.shoot_cd_max:
                self.diagonal_shoot()
                self.shoot_cd = 0
        if self.shot_phase == 3:
            if self.shoot_cd == self.shoot_cd_max:
                if self.do_cardinal_shoot:
                    self.cardinal_shoot()
                    self.do_cardinal_shoot = False
                else:
                    self.diagonal_shoot()
                    self.do_cardinal_shoot = True
                self.shoot_cd = 0
        if self.shot_phase == 4:
            if self.shoot_cd == self.shoot_cd_max:
                self.target_shoot()
                self.shoot_cd = 0

        self.shoot_cd += 1
        self.shoot_phase_cd += 1



        if self.HP <= 0:
            self.phase_no = 2
            self.kill()


class Boss1P2(Boss1):
    """"""
    pass


class Boss1P3(Boss1):
    """"""
    pass

