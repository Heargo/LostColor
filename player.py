import pygame
from constants import *
from pygame.locals import *
from inventaire import Inventory
class Player(pygame.sprite.Sprite):
	"""docstring for Player"""
	def __init__(self, name="Coloro",x=0,y=0, image="img/player/player.png"):
		super().__init__()
		self.name = name
		self.x = x
		self.y = y
		self.image = pygame.image.load(image)
		self.image_temp = pygame.image.load(image)
		self.rect = self.image.get_rect()

		self.rect.x = self.x 
		self.rect.y = self.y

		self.inventaire = Inventory(64)
		self.initStats()

	def initStats(self):
		# Statistiques du joueur
		self.HP_MAX = PLAYER_HP
		self.HP = self.HP_MAX
		self.DMG = PLAYER_DMG
		self.tps = PLAYER_TPS  # Tire par seconde
		self.cooldown = FPS // self.tps
		self.cooldown_max = FPS // self.tps
		self.shot_speed = PLAYER_SHOOT_SPEED
		self.speed = PLAYER_SPEED
		self.colorbuff= GRAY

		#cd
		self.healed=0
		self.healCD=HEAL_COOLDOWN

		#bonus
		self.HP_MAX_bonus = 0
		self.DMG_bonus = 0
		self.tps_bonus = 0  # Tire par seconde
		self.shot_speed_bonus = 0
		self.speed_bonus = 0


		# Gestion de l'invincibilité apres avoir recus un coup
		self.get_hit = False
		self.invicibility_frame = 120
		self.curent_invicibility_frame = self.invicibility_frame
		self.filter_on = False

		# Gestion salle
		self.current_room_id = 0

	def updateStats(self):
		#on stocke les effets des items équipés
		effetsItems={"hp":0,"dmg":0,"tps":0,"speed":0,"shot_speed":0}
		for item in self.inventaire.equipement.values():
			if item!=False:
				for stat in item.stats:
					effetsItems[stat]+=item.stats[stat]

		#on met a jour les stats en prenant en compte les bonus 
		self.HP_MAX = PLAYER_HP + self.HP_MAX_bonus + effetsItems["hp"]
		self.DMG = PLAYER_DMG + self.DMG_bonus + effetsItems["dmg"]
		self.tps = PLAYER_TPS  + self.tps_bonus  +effetsItems["tps"]
		self.shot_speed = PLAYER_SHOOT_SPEED +self.shot_speed_bonus + effetsItems["shot_speed"]
		self.speed = PLAYER_SPEED +self.speed_bonus + effetsItems["speed"]

		#on cap si besoin
		if self.HP_MAX >STATS_MAX["hp"]:
			self.HP_MAX = STATS_MAX["hp"]
		if self.DMG >STATS_MAX["dmg"]:
			self.DMG =STATS_MAX["dmg"]
		if self.tps >STATS_MAX["tps"]:
			self.tps =STATS_MAX["tps"]
		if self.shot_speed >STATS_MAX["shot_speed"]:
			self.shot_speed =STATS_MAX["shot_speed"]
		if self.speed >STATS_MAX["speed"]:
			self.speed =STATS_MAX["speed"]

		self.cooldown = FPS // self.tps
		self.cooldown_max = FPS // self.tps

	def getStatsDico(self):
		return {"hp":self.HP_MAX,"dmg":self.DMG,"tps":self.tps,"speed":self.speed,"shot_speed":self.shot_speed}

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
				self.image = pygame.image.load("img/player/player.png")


			if self.curent_invicibility_frame <= 0:
				self.get_hit = False
				self.curent_invicibility_frame = self.invicibility_frame

	def update(self):
		""""""
		self.cooldown += 1
		self.invicibility_after_getting_hit()
		self.cooldown_max = FPS // self.tps
		

