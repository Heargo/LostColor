import pygame
from constants import *
from pygame.locals import *
class Player(pygame.sprite.Sprite):
	"""docstring for Player"""
	def __init__(self, name="Coloro",x=0,y=0,speed=3, image="img/monster.png"):
		super().__init__()
		self.name = name
		self.x = x
		self.y = y
		self.image = pygame.image.load(image)
		self.image_temp = pygame.image.load(image)
		self.rect = self.image.get_rect()

		self.rect.x = self.x 
		self.rect.y = self.y

		self.initStats(speed)

	def initStats(self,speed):
		# Statistiques du joueur
		self.HP_MAX = 100
		self.HP = self.HP_MAX
		self.DMG = 12
		self.tps = 2  # Tire par seconde
		self.cooldown = FPS // self.tps
		self.cooldown_max = FPS // self.tps
		self.shot_speed = 8
		self.speed = speed
		self.colorbuff= GRAY

		# Gestion de l'invincibilité apres avoir recus un coup
		self.get_hit = False
		self.invicibility_frame = 120
		self.curent_invicibility_frame = self.invicibility_frame
		self.filter_on = False

		# Gestion salle
		self.current_room_id = 0

	def pos(self):

		return(self.rect.x+0.5*self.rect.width,self.rect.y+0.5*self.rect.height)

	def move(self,direction, walls):
		if direction=="UP":
			self.rect.y-=self.speed
		elif direction=="DOWN":
			self.rect.y+=self.speed
		elif direction =="RIGHT":
			self.rect.x+=self.speed
		elif direction=="LEFT":
			self.rect.x-=self.speed

		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:
			# Si le joueur se déplace en direction d'un mur, cela
			# met le coté du joueur qui touche le mur sur le coté
			# du mur touché
			if direction == "RIGHT":
				self.rect.right = block.rect.left
			elif direction == "LEFT":
				self.rect.left = block.rect.right
			elif direction == "DOWN":
				self.rect.bottom = block.rect.top
			elif direction == "UP":
				self.rect.top = block.rect.bottom

	def invicibility_after_getting_hit(self):
		""""""

		if self.get_hit:
			self.curent_invicibility_frame -= 1

			if self.curent_invicibility_frame % 10 == 0:
				self.filter_on = not self.filter_on


			if self.filter_on:
				filtre = pygame.Surface((self.rect.width, self.rect.height), SRCALPHA)
				filtre_rect = filtre.get_rect()
				filtre.fill((255, 255, 255, 100))
				self.image.blit(filtre, filtre_rect)
			else:
				self.image = pygame.image.load("img/monster.png")


			if self.curent_invicibility_frame <= 0:
				self.get_hit = False
				self.curent_invicibility_frame = self.invicibility_frame

	def update(self):
		""""""
		self.cooldown += 1
		self.invicibility_after_getting_hit()
		self.cooldown_max = FPS // self.tps
		

