import pygame, sys
from pygame.locals import *
from functions import draw_text
from constants import *

class Item(pygame.sprite.Sprite):
	"""docstring for Item"""
	def __init__(self,slot,x,y,image="./img/item.png"):
		super().__init__()
		self.name=-1
		self.x = x
		self.y = y
		self.slot=slot
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()

		self.rect.x = self.x 
		self.rect.y = self.y


	def hoover(self, mx, my):
		if self.rect.collidepoint(mx, my):
			is_hoover = True
		else:
			is_hoover = False
		return is_hoover

	def pos(self):
		return (self.rect.x,self.rect.y)

	def move(self,pos):
		self.rect.x = pos[0]
		self.rect.y = pos[1]


class Slot(pygame.sprite.Sprite):
	"""docstring for Item"""
	def __init__(self,id,x,y,image="./img/slot.png"):
		super().__init__()
		self.id = id
		self.x = x
		self.y = y
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.rect.x = self.x 
		self.rect.y = self.y


	def hoover(self, mx, my):
		if self.rect.collidepoint(mx, my):
			is_hoover = True
		else:
			is_hoover = False
		return is_hoover

class Inventory(object):
	"""docstring for Inventory"""
	def __init__(self, size):
		self.size = size
		self.equipement ={}
		self.items = [False]*size
		self.slots=self.createSlots()

	def createSlots(self):
		lsSlots=[]
		for i in range(self.size):
			x=i%8 * 60 +700
			y=i//8 * 60 +150
			lsSlots+=[Slot(i,x,y)]
		return lsSlots

	def add(self,item):
		added=False
		i=0
		while not added and i<self.size:
			if self.items[i] ==False:
				print("ajouté !",item)
				self.items[i] = item
				item.slot=i
				item.move((self.slots[i].rect.x,self.slots[i].rect.y))
				added=True
			i+=1


		

pygame.init()
# Definition des FPS
fpsClock = pygame.time.Clock()

# --- Création de la fenetre
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("test inventaire")


#liste des slots
slotslist=pygame.sprite.Group()
#liste des items
itemlist = pygame.sprite.Group()


#liste de tout les sprites
all_sprites=pygame.sprite.LayeredUpdates()


######
######	INVENTAIRE
######
inventaire=Inventory(64)
#on créé les slots et on les ajoute a la liste des slots

for slot in inventaire.slots:
	slotslist.add(slot)


######
######	SPRITES
######


#en couche la plus basse on met les slots (pour qu'ils soit recouverts par les items)
all_sprites.add(slotslist)
all_sprites.add(itemlist)



running=True
locked=False
spritePosBeforeLock=0
spriteLocked=-1
# -------- Main Program Loop -----------
while running:
	#fermeture de la fenetre
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		# Detection d'utilisation du clavier pour faire spawner 3 monstres
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				item=Item(-1,0,0)
				itemlist.add(item)
				all_sprites.add(item)
				inventaire.add(item)
				print(inventaire.items)
			

	# Detection du clic gauche la souris et de sa position
	activeMouse = pygame.mouse.get_pressed()
	mx, my = pygame.mouse.get_pos()
	#si on clique
	if activeMouse[0] == True:
		#on regarde pour chaque item 
		for item in itemlist:
			#si on est dessus et qu'on ne bouge pas déja un 
			if item.hoover(mx,my) and not locked:
				locked = True
				spriteLocked= item
				spritePosBeforeLock=item.pos()
			#si on en bouge un et que c'est cet item
			if locked and spriteLocked==item:
				item.rect.x = mx - item.rect.width/2
				item.rect.y = my - item.rect.height/2

	#si on ne clique pas
	else:
		#si on avait un item
		if locked : 
			hoverASlot=False
			#on regarde chaque slot
			for slot in slotslist:
				#si on est au dessus du slot et qu'il est vide
				if slot.hoover(mx,my) and inventaire.items[slot.id]==False:
					inventaire.items[spriteLocked.slot]=False
					inventaire.items[slot.id] = spriteLocked
					spriteLocked.slot=slot.id
					spriteLocked.rect.x = slot.rect.x
					spriteLocked.rect.y = slot.rect.y
					hoverASlot=True
				#si on est au dessus du slot et qu'il est plein
				elif slot.hoover(mx,my) and inventaire.items[slot.id]!=False:
					spriteLocked.move(spritePosBeforeLock)
					hoverASlot=True
			if not hoverASlot:
				spriteLocked.move(spritePosBeforeLock)
			locked=False
			spritePosBeforeLock=0
			spriteLocked=-1


	# Appelle la méthode update() de tous les Sprites
	all_sprites.update()
	screen.fill((255,255,255))
	draw_text(screen,'Inventaire', 'fonts/No_Color.ttf', 60, BLACK, 964, 64, True)
	# Dessine tous les sprites (les blits sur screen)
	all_sprites.draw(screen)
	pygame.display.update()
	fpsClock.tick(60)

pygame.quit()
sys.exit()