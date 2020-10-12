import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	"""docstring for Player"""
	def __init__(self, name="Coloro",x=0,y=0,speed=0.1, image="./img/monster.png"):
		super().__init__()
		self.name = name
		self.x = x
		self.y = y
		self.speed = speed
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()

		self.rect.x = self.x 
		self.rect.y = self.y


	def move(self,direction):
		if direction=="UP":
			self.rect.y-=self.speed
		elif direction=="DOWN":
			self.rect.y+=self.speed
		elif direction =="RIGHT":
			self.rect.x+=self.speed
		elif direction=="LEFT":
			self.rect.x-=self.speed

	def attaque(spell, entity):
		"""Player attaque entity avec le sort spell"""
		print("J'attaque")
