import pygame, sys
from pygame.locals import *
#from functions import draw_text
from constants import *







def draw_text(screen,text, font_name, size, color, x, y, center):
    """"""
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.centerx = x
        text_rect.centery = y
    else:
        text_rect.x = x
        text_rect.y = y

    screen.blit(text_surface, text_rect)



class Item(pygame.sprite.Sprite):
	"""docstring for Item"""
	def __init__(self,equipable,slotequipable,name,shortName="none",image="./img/items/item.png"):
		super().__init__()
		self.name=name
		if shortName=="none":
			self.shortName=name
		else:
			self.shortName = shortName
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
	def __init__(self,id,x,y,image="./img/slots/slot.png"):
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
			dicoSlots[name]=Slot(slotsNames[i],x,y,"./img/slots/"+name+".png")

		self.equipementSlots=dicoSlots

	def add(self,item):
		added=False
		i=0
		while not added and i<self.size:
			if self.items[i] ==False:
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

	def updateSlotsImg(self):
		for slot,item in self.equipement.items():
			if item!=False:
				self.equipementSlots[slot].image = pygame.image.load("./img/slots/full.png")
			else:
				self.equipementSlots[slot].image =  pygame.image.load("./img/slots/"+slot+".png")




def switch(item1,item2,inventaire):
	""" ehange la position d'item1 et item2 si c'est possible
	ENTREE:
	- item1 [item]
	- item2 [item]
	- inventaire [Inventory]
	"""
	res = False
	#si c'est un des objet est equipé
	if item1.slot in inventaire.equipement.keys() or item2.slot in inventaire.equipement.keys():
		if item1.slotequipable == item2.slotequipable:
			#on recupère les slots
			slot1=item1.slot
			slot2=item2.slot

			#on met l'item 1 à la place de l'item 2 
			item1.slot = slot2
			item2.slot = slot1
			print(slot1,slot2)
			if slot1 in inventaire.equipement.keys():
				inventaire.items[slot2] = item1
				item1.move((inventaire.slots[slot2].rect.x,inventaire.slots[slot2].rect.y))

				inventaire.equipement[slot1] = item2
				item2.move((inventaire.equipementSlots[slot1].rect.x,inventaire.equipementSlots[slot1].rect.y))
			else:
				inventaire.equipement[slot2] = item1
				item1.move((inventaire.equipementSlots[slot2].rect.x,inventaire.equipementSlots[slot2].rect.y))

				inventaire.items[slot1] = item2
				item2.move((inventaire.slots[slot1].rect.x,inventaire.slots[slot1].rect.y))

			res = True
	#si aucun objet n'est equipable
	else:
		#on recupère les slots
		slot1=item1.slot
		slot2=item2.slot

		#on met l'item 1 à la place de l'item 2 
		item1.slot = slot2
		inventaire.items[slot2] = item1
		item1.move((inventaire.slots[slot2].rect.x,inventaire.slots[slot2].rect.y))

		item2.slot = slot1
		inventaire.items[slot1] = item2
		item2.move((inventaire.slots[slot1].rect.x,inventaire.slots[slot1].rect.y))

		res = True
	return res



def checkmoveInInv(mx,my,spriteLocked,spritePosBeforeLock,slotslist,inventaire):
	"""verifie si c'est possible de poser l'item la ou il est. Si c'est possible on deplace l'item (ou les items si on inverse de place)
	ENTREE : 
	- spriteLocked [Item]
	- spritePosBeforeLock [tuple] (x,y)
	- slotslist [pygame.sprite.Group()]
	- inventaire [Inventory]
	"""
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
					spriteLocked.move((slot.rect.x,slot.rect.y))
					hoverASlot=True
			#si on est au dessus du slot et qu'il est plein et que ce n'est pas le même item
			elif slot.hoover(mx,my) and inventaire.equipement[slot.id]!=False and spriteLocked!=inventaire.equipement[slot.id]:
				switched = switch(spriteLocked, inventaire.equipement[slot.id],inventaire)
				if not switched:
					spriteLocked.move(spritePosBeforeLock)
				hoverASlot=True
		else:
			#si on est au dessus du slot et qu'il est vide
			if slot.hoover(mx,my) and inventaire.items[slot.id]==False:
				#on l'enleve de la ou il était
				inventaire.remove(spriteLocked)
				inventaire.items[slot.id] = spriteLocked
				spriteLocked.slot=slot.id
				spriteLocked.move((slot.rect.x,slot.rect.y))
				hoverASlot=True

			#si on est au dessus du slot et qu'il est plein
			elif slot.hoover(mx,my) and inventaire.items[slot.id]!=False:
				switched = switch(spriteLocked ,inventaire.items[slot.id],inventaire)
				if not switched:
					spriteLocked.move(spritePosBeforeLock)
				hoverASlot=True

	if not hoverASlot:
			spriteLocked.move(spritePosBeforeLock)



def checkRightClick(inventaire):
	mx, my = pygame.mouse.get_pos()
	#on regarde pour les objets de l'inventaire
	for item in inventaire.items:
		#si on est dessus
		if item != False and item.hoover(mx,my) and item.slotequipable in inventaire.equipement.keys():
			#si son emplacement est deja  rempli on switch
			if inventaire.equipement[item.slotequipable]!=False:
				switch(item ,inventaire.equipement[item.slotequipable],inventaire)
			#sinon on le met direct
			else:
				#on l'enleve de la ou il était
				inventaire.remove(item)
				inventaire.equipement[item.slotequipable] = item
				item.slot=item.slotequipable
				item.move((inventaire.equipementSlots[item.slot].rect.x,inventaire.equipementSlots[item.slot].rect.y))
	#on regarde pour les objets de l'equipement
	for item in inventaire.equipement.values():
		#si on est dessus
		if item != False and item.hoover(mx,my):
			#si il reste un emplacement vide on l'équipe
			if inventaire.equipement[item.slotequipable]!=False:
				inventaire.remove(item)
				inventaire.add(item)

				


def drawInventory(screen):
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


def drawItemOverlay(screen,mx, my,itemlist,inventaire):
	
	hoverAnItem=False
	for item in itemlist:
		if item.hoover(mx, my):
			itemHoover=item
			hoverAnItem=True

	if hoverAnItem:
		width=200
		height=300

		if itemHoover.slot in inventaire.equipement.keys():
			decalX=0
			decalXText = 360
			#on dessine le cadre
			border = pygame.Rect(mx,my,width+10,height+10)
			fond = (mx+5,my+5,width,height)
		else:
			decalX = -200
			decalXText = -200
			#on dessine le cadre
			border =(mx+decalX-5,my-5,width+10,height+10)
			fond = (mx+decalX,my,width,height)
		
		
		#on dessine le cadre
		pygame.draw.rect(screen,(100,64,31),border)
		pygame.draw.rect(screen,(164,131,80),fond)

		#on recupère l'image du l'item
		img = pygame.transform.scale(itemHoover.image,(50,50))
		#on la resize
		rect = img.get_rect()
		#on la place en haut à gauche du cadre
		rect = rect.move((mx+decalX+10, my+10))
		screen.blit(img, rect)

		#on dessine le nom (titre):
		if len(itemHoover.name) > 10:
			txt=itemHoover.shortName
		else:
			txt=itemHoover.name
		draw_text(screen,txt, 'fonts/No_Color.ttf', 20, BLACK, mx+(0.75*(decalXText//2)), my+30, True)



def invetoryScreen(screen,fpsClock,inventaire):
	#liste des slots
	slotslist=pygame.sprite.Group()
	#liste des items
	itemlist = pygame.sprite.Group()

	#list des autres sprites
	otherlist = pygame.sprite.Group()


	#liste de tout les sprites
	all_sprites=pygame.sprite.LayeredUpdates()

	######
	######	INVENTAIRE
	######

	#on ajoute les slots a la liste des slots
	for slot in inventaire.slots:
		slotslist.add(slot)
	for slot in inventaire.equipementSlots.values():
		slotslist.add(slot)

	#de meme avec les items
	for item in inventaire.items:
		if item !=False:
			itemlist.add(item)
	for item in inventaire.equipement.values():
		if item !=False:
			itemlist.add(item)


	######
	######	SPRITES
	######


	profilimg=ProfilIMG(132,100)
	otherlist.add(profilimg)
	#en couche la plus basse on met les slots (pour qu'ils soit recouverts par les items)
	all_sprites.add(otherlist)
	all_sprites.add(slotslist)

	all_sprites.add(itemlist)



	locked=False
	spritePosBeforeLock=0
	spriteLocked=-1
	inventaireOn=True
	# -------- Main Program Loop -----------
	while inventaireOn:
		#fermeture de la fenetre
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			# Detection d'utilisation du clavier pour faire spawner 3 monstres
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					item=Item(True,"head","helmet2","./img/items/helmet.png")
					itemlist.add(item)
					all_sprites.add(item)
					inventaire.add(item)
				if event.key == pygame.K_i:
					inventaireOn=False

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not locked:
				checkRightClick(inventaire)
				

		# Detection du clic gauche la souris et de sa position
		activeMouse = pygame.mouse.get_pressed()
		mx, my = pygame.mouse.get_pos()
		#si on clique
		if activeMouse[0] == True:
			#on regarde pour chaque item 
			for item in itemlist:
				#si on est dessus et qu'on ne bouge pas déja un 
				if item.hoover(mx,my) and not locked:
					#on le prend
					locked = True
					spriteLocked= item
					spritePosBeforeLock=item.pos()
				#si on en bouge un et que c'est cet item
				if locked and spriteLocked==item:
					#l'item suis notre souris
					item.rect.x = mx - item.rect.width//2
					item.rect.y = my - item.rect.height//2

		#si on ne clique pas
		else:
			#si on avait un item
			if locked : 
				#on verifie si c'est possible de poser l'item la ou il est. Si c'est possible on deplace l'item (ou les items si on inverse de place)
				checkmoveInInv(mx,my,spriteLocked,spritePosBeforeLock,slotslist,inventaire)
				locked=False
				spritePosBeforeLock=0
				spriteLocked=-1

		#on change le fond des slots d'inventaire si il on un objet équipé
		inventaire.updateSlotsImg()
		# Appelle la méthode update() de tous les Sprites
		all_sprites.update()
		#on met l'ecran en blanc
		screen.fill((255,255,255))

		drawInventory(screen)
		# Dessine tous les sprites (les blits sur screen)
		all_sprites.draw(screen)

		#si besoin on dessine l'overlay de l'item
		if activeMouse[0] == False:
			drawItemOverlay(screen,mx, my,itemlist,inventaire)

		pygame.display.update()
		fpsClock.tick(60)
