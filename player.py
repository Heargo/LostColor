import abc
from entity import Entity

class Player(Entity):
	"""docstring for Player"""
	def __init__(self, name="Coloro",x=0,y=0, avatar="./img/monster.png"):
		self.name = name
		self.x = x
		self.y = y
		self.dirX = 0
		self.dirY = 0
		self.avatar = avatar

	def attaque(spell, entity):
		"""Player attaque entity avec le sort spell"""
		print("J'attaque")
