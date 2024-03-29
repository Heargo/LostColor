import pygame, sys
from pygame.locals import *
#from functions import draw_text
from constants import *
from random import choice, choices, randint
import controls
from Items import *
from tools import draw_text




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
	def __init__(self, size, x_slots=700, y_slots=180):
		self.size = size
		self.equipement ={"head":False,"chest":False,"glove":False,"boot":False,"weapon":False,"weaponbis":False,"earrings":False,"belt":False}
		self.createEquipementSlot()
		self.items = [False]*size
		self.createSlots(x_slots,y_slots)


	def createSlots(self,x_slots,y_slots):
		lsSlots=[]
		for i in range(self.size):
			x=i%8 * 60 + x_slots
			y=i//8 * 60 + y_slots
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
				item.move((self.slots[i].rect.x+5,self.slots[i].rect.y+5))
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

	def numOfItems(self):
		res=0
		for i in self.items:
			if i !=False:
				res+=1
		return res
	
	def move_all_items(self):
		for i in range(len(self.items)):
			if self.items[i] != False:
				self.items[i].move((self.slots[i].rect.x+5,self.slots[i].rect.y+5))





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

def generateLoot(x,y,loots_list,all_sprites_list):
	item = createRandomItem()

	#on recupère l'image du l'item
	img = pygame.transform.scale(item.image,(32,32))
	#on récup le rect
	rect = img.get_rect()
	item.image = img
	item.rect = rect
	#on la place correctement
	item.move((x,y))

	#on le met dans la liste des loots
	loots_list.add(item)
	all_sprites_list.add(item)

def checkMoveInShop(mx, my, spriteLocked, spritePosBeforeLock, playerslotslist, merchantslotslist, player, merchant, playerItemTaken):
	"""Permet de verifier les déplacement des objet dans le shop"""
	hoverASlot = False
	for slot in playerslotslist:
		if playerItemTaken:
			if slot.hoover(mx, my) and player.inventaire.items[slot.id] == False:
				# on l'enleve de la ou il était
				player.inventaire.remove(spriteLocked)
				player.inventaire.items[slot.id] = spriteLocked
				spriteLocked.slot = slot.id
				spriteLocked.move((slot.rect.x, slot.rect.y))
				hoverASlot = True

			# si on est au dessus du slot et qu'il est plein
			elif slot.hoover(mx, my) and player.inventaire.items[slot.id] != False:
				switched = switch(spriteLocked, player.inventaire.items[slot.id], player.inventaire)
				if not switched:
					spriteLocked.move(spritePosBeforeLock)
				hoverASlot = True
		else:
			if slot.hoover(mx, my) and player.inventaire.items[slot.id] == False:
				if player.money >= spriteLocked.price:
					player.money = round(player.money-spriteLocked.price,2)
					merchant.money = round(merchant.money+spriteLocked.price,2)
					spriteLocked.price = round(spriteLocked.price * 0.75,1)
					# on l'enleve de la ou il était
					merchant.inventaire.remove(spriteLocked)
					player.inventaire.items[slot.id] = spriteLocked
					spriteLocked.slot = slot.id
					spriteLocked.move((slot.rect.x, slot.rect.y))
					hoverASlot = True
	for slot in merchantslotslist:
		if playerItemTaken:
			if slot.hoover(mx, my) and merchant.inventaire.items[slot.id] == False:
				if merchant.money >= spriteLocked.price:
					# Le joueur vends l'objet le prix de l'objet monte car le marchand le revends plus cher
					player.money = round(player.money+spriteLocked.price,2)
					merchant.money = round(merchant.money-spriteLocked.price,2)
					spriteLocked.price = round(spriteLocked.price * 2,2)
					# on l'enleve de la ou il était
					player.inventaire.remove(spriteLocked)
					merchant.inventaire.items[slot.id] = spriteLocked
					spriteLocked.slot = slot.id
					spriteLocked.move((slot.rect.x, slot.rect.y))

					hoverASlot = True
		else:
			if slot.hoover(mx, my) and merchant.inventaire.items[slot.id] == False:
				# on l'enleve de la ou il était
				merchant.inventaire.remove(spriteLocked)
				merchant.inventaire.items[slot.id] = spriteLocked
				spriteLocked.slot = slot.id
				spriteLocked.move((slot.rect.x, slot.rect.y))
				hoverASlot = True

			# si on est au dessus du slot et qu'il est plein
			elif slot.hoover(mx, my) and merchant.inventaire.items[slot.id] != False:
				switched = switch(spriteLocked, merchant.inventaire.items[slot.id], merchant.inventaire)
				if not switched:
					spriteLocked.move(spritePosBeforeLock)
				hoverASlot = True



	if not hoverASlot:
			spriteLocked.move(spritePosBeforeLock)





def checkmoveInInv(mx,my,spriteLocked,spritePosBeforeLock,slotslist,itemlist,all_sprites,inventaire):
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

		if slot.id !="bin":
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
		elif slot.hoover(mx,my) and slot.id =="bin":
			inventaire.remove(spriteLocked)
			itemlist.remove(spriteLocked)
			all_sprites.remove(spriteLocked)

	if not hoverASlot:
			spriteLocked.move(spritePosBeforeLock)

def checkRightClick(inventaire,player,itemlist,all_sprites):
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
		elif item != False and item.hoover(mx,my) and "heal" in item.stats.keys() and player.HP < player.HP_MAX:
			inventaire.remove(item)
			itemlist.remove(item)
			all_sprites.remove(item)
			#on soigne le joueur
			player.HP += item.stats["heal"]
			if player.HP > player.HP_MAX:
				player.HP = player.HP_MAX

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

def drawStats(screen,player):
	player.updateStats()
	#stats
	i=0
	stats= player.getStatsDico()
	for stat in stats:
		yPOS=450+(i*30)
		draw_text(screen,stat, 'fonts/No_Color.ttf', 15, BLACK, 80, yPOS, False)
		nbBlocks=int(5*stats[stat]/STATS_MAX_COMMUN[stat])
		if nbBlocks==0:
			nbBlocks=1
		if nbBlocks>5:
			nbBlocks=5
		#on recupère le grade de la stat
		color =(100,64,31)
		gradeStat="commun"
		for grade in STATS_GRADE_DATA[stat].keys():
			if stats[stat] >=STATS_GRADE_DATA[stat][grade]:
				color = COLOR_OF_GRADE[grade]
				gradeStat=grade

		if stats[stat] <STATS_MAX_COMMUN[stat]:
			for j in range(nbBlocks):
				pygame.draw.rect(screen,color,(80+(j*55),yPOS+20,50,5))
		else:
			for j in range(GRADES.index(gradeStat)+1):
				pygame.draw.rect(screen,COLOR_OF_GRADE[GRADES[j]],(80+(j*55),yPOS+20,50,5))
		i+=1


def invetoryScreen(screen,fpsClock,inventaire,player):
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
	binSlot = Slot("bin",1100,100,image="./img/slots/bin.png")
	slotslist.add(binSlot)
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
	#en couche la plus basse on met la poubelle puis les slots (pour qu'ils soit recouverts par les items)
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
			# Detection d'utilisation du clavier 
			if event.type == pygame.KEYDOWN:
				#pour ajouter un item aléatoire (debug)
				# if event.key == pygame.K_q and inventaire.numOfItems() < inventaire.size:
				# 	item=createRandomItem()
				# 	itemlist.add(item)
				# 	all_sprites.add(item)
				# 	inventaire.add(item)

				if event.key == controls.C_INVENTAIRE or event.key == pygame.K_ESCAPE:
					inventaireOn=False

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not locked:
				checkRightClick(inventaire,player,itemlist,all_sprites)
				

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
				checkmoveInInv(mx,my,spriteLocked,spritePosBeforeLock,slotslist,itemlist,all_sprites,inventaire)
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
		drawStats(screen,player)
		# Dessine tous les sprites (les blits sur screen)
		all_sprites.draw(screen)

		#si besoin on dessine l'overlay de l'item
		if activeMouse[0] == False:
			drawItemOverlay(screen,mx, my,itemlist,inventaire)

		pygame.display.update()
		fpsClock.tick(60)
