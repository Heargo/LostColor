import pygame, sys
from pygame.locals import *
from functions import draw_text
from constants import *

class Item(pygame.sprite.Sprite):
	"""docstring for Item"""
	def __init__(self,equipable,slotequipable,name,image="./img/items/item.png"):
		super().__init__()
		self.name="item"
		self.x = 0
		self.y = 0
		self.slot=-1
		self.equipable = equipable
		if self.equipable:
			self.slotequipable=slotequipable
		else:
			self.slotequipable=-1
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
	def __init__(self,id,x,y,image="./img/slots/slot.png",type="inv"):
		super().__init__()
		self.id = id
		self.type = type
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


class ProfilIMG(pygame.sprite.Sprite):
	"""docstring for Profil"""
	def __init__(self, x,y):
		super().__init__()
		self.x = x
		self.y = y
		self.image=pygame.image.load("./img/player/inventory_profil.png")
		self.rect = self.image.get_rect()

		self.rect.x = self.x 
		self.rect.y = self.y	




class Inventory(object):
	"""docstring for Inventory"""
	def __init__(self, size):
		self.size = size
		self.equipement ={"head":False,"chest":False,"glove":False,"boot":False,"weapon":False,"weaponbis":False,"earrings":False,"belt":False}
		self.createEquipementSlot()
		self.items = [False]*size
		self.createSlots()

	def createSlots(self):
		lsSlots=[]
		for i in range(self.size):
			x=i%8 * 60 +700
			y=i//8 * 60 +180
			lsSlots+=[Slot(i,x,y)]
		self.slots= lsSlots

	def createEquipementSlot(self):
		slotsNames=["head","chest","glove","boot","weapon","weaponbis","earrings","belt"]
		dicoSlots={}
		positions=[(85,150),(85,224),(330,224),(85,298),(175,364),(249,364),(330,150),(330,298)]
		for i in range(len(slotsNames)):
			name=slotsNames[i]
			x=positions[i][0]
			y=positions[i][1]
			dicoSlots[name]=[Slot(slotsNames[i],x,y,"./img/slots/"+name+".png")]

		self.equipementSlots=dicoSlots

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

	def remove(self,item):
		if item in self.items:
			self.items[item.slot]=False	
		if item.slot in self.equipementSlots.keys():
			self.equipement[item.slot]=False	
		

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

#list des autres sprites
otherlist = pygame.sprite.Group()


#liste de tout les sprites
all_sprites=pygame.sprite.LayeredUpdates()



#items
item1=Item(True,"head","helmet","./img/items/helmet.png")
item2=Item(True,"belt","belt","./img/items/belt.png")
item3=Item(True,"earrings","earrings","./img/items/earrings.png")
item4=Item(True,"chest","chestplate","./img/items/armor.png")
item5=Item(True,"weapon","wand","./img/items/wand.png")
item6=Item(False,-1,"cake au cerise","./img/items/cake.png")
item7=Item(False,-1,"tomato","./img/items/tomato.png")

itemlist.add(item1,item2,item3,item4,item5,item6,item7)



######
######	INVENTAIRE
######

inventaire=Inventory(64)

for item in itemlist:
	inventaire.add(item)
#on créé les slots et on les ajoute a la liste des slots

for slot in inventaire.slots:
	slotslist.add(slot)
for slot in inventaire.equipementSlots.values():
	slotslist.add(slot)



######
######	SPRITES
######


profilimg=ProfilIMG(132,100)
otherlist.add(profilimg)
#en couche la plus basse on met les slots (pour qu'ils soit recouverts par les items)
all_sprites.add(otherlist)
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
				item=Item(True,"head","item")
				itemlist.add(item)
				all_sprites.add(item)
				inventaire.add(item)
			

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
				#si c'est un slot de l'equipement
				if slot.id in inventaire.equipementSlots.keys():
					#si on est au dessus du slot et qu'il est vide
					if slot.hoover(mx,my) and inventaire.equipement[slot.id]==False:
						#si il est equipable sur ce slot
						if spriteLocked.equipable and spriteLocked.slotequipable==slot.id:
							#on l'enleve de la ou il était
							inventaire.remove(spriteLocked)
							inventaire.equipement[slot.id] = spriteLocked
							spriteLocked.slot=slot.id
							spriteLocked.rect.x = slot.rect.x
							spriteLocked.rect.y = slot.rect.y
							hoverASlot=True
					#si on est au dessus du slot et qu'il est plein
					elif slot.hoover(mx,my) and inventaire.equipement[slot.id]!=False:
						spriteLocked.move(spritePosBeforeLock)
						hoverASlot=True
				else:
					#si on est au dessus du slot et qu'il est vide
					if slot.hoover(mx,my) and inventaire.items[slot.id]==False:
						#on l'enleve de la ou il était
						inventaire.remove(spriteLocked)
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
	#on met l'ecran en blanc
	screen.fill((255,255,255))

	#on dessine les background
	#inventaire fond
	pygame.draw.rect(screen,(164,131,80),(690,40,505,635))
	#inventaire bords
	pygame.draw.rect(screen,(100,64,31),(690,40,505,635),5)

	#profil fond
	pygame.draw.rect(screen,(164,131,80),(50,40,505,635))
	#profil bords
	pygame.draw.rect(screen,(100,64,31),(50,40,505,635),5)
	

	#puis les texts
	draw_text(screen,'Inventaire', 'fonts/No_Color.ttf', 30, BLACK, 950, 80, True)
	draw_text(screen,'Profil', 'fonts/No_Color.ttf', 30, BLACK, 300, 80, True)
	# Dessine tous les sprites (les blits sur screen)
	all_sprites.draw(screen)
	pygame.display.update()
	fpsClock.tick(60)

pygame.quit()
sys.exit()