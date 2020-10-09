import abc

class Entity(metaclass=abc.ABCMeta):
	"""docstring for Entity"""

	#getters
	def getX(self):
		"""return x"""
		return self.x
	def getY(self):
		"""return y"""
		return self.y
	def getDirX(self):
		"""return direX"""
		return self.dirX
	def getDirY(self):
		"""return direY"""
		return self.dirY
	def getAvatar(self):
		"""return direY"""
		return self.avatar

	#setters
	def setX(self,x):
		"""set x"""
		self.x = x
	def setY(self,y):
		"""set y"""
		self.y = y


	#mouvements
	def moveTop(self,y):
		"""Déplace Player vers le haut"""
		self.dirY=-y

	def moveBottom(self,y):
		"""Déplace Player vers le bas"""
		self.dirY=y

	def moveLeft(self,x):
		"""Déplace Player vers la gauche"""
		self.dirX=-x

	def moveRight(self,x):
		"""Déplace Player vers la droite"""
		self.dirX=x

	def stopX(self):
		"""Arrete de deplace en x"""
		self.dirX=0

	def stopY(self):
		"""Arrete de deplacer en Y """
		self.dirY=0


	#méthodes 
	@abc.abstractmethod
	def attaque(spell, entity):
		"""Player attaque entity avec le sort spell"""
		pass

	# @abc.abstractmethod
	# def die():
	# 	"""Player attaque entity avec le sort spell"""
	# 	pass






