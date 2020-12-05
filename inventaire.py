import pygame, sys
from pygame.locals import *
#from functions import draw_text
from constants import *
from random import choice, choices, randint

class Item(pygame.sprite.Sprite):
	"""docstring for Item"""
	def __init__(self,equipable,slotequipable,name,shortName="none",image="./img/items/item.png",grade="commun",price=0.1,stats={},description="none"):
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
		self.imagePath=image
		self.rect = self.image.get_rect()
		self.rect.x = self.x 
		self.rect.y = self.y

		#caractéristiques
		self.grade = grade
		self.price = price
		self.stats = stats
		self.description = description

	def hoover(self, mx, my):
		if self.rect.collidepoint(mx, my):
			is_hoover = True
		else:
			is_hoover = False
		return is_hoover

	def resetImage(self):
		self.image = pygame.image.load(self.imagePath)
		#on rezise a 64*64 pixel
		self.image = pygame.transform.scale(self.image,(64,64))
		self.rect = self.image.get_rect()

	def pos(self):
		return (self.rect.x,self.rect.y)

	def move(self,pos):
		self.rect.x = pos[0]
		self.rect.y = pos[1]


	def info(self):
		infos=("Nom : {0}\nLevel : {1}\nGrade : {9}\nprix : {2}\nstackable : {3}\nStatistiques : {4}\nDurabilité : {5}/{6}\ndescription : {7}\neffet : {8}")
		return infos
		





def to_gold(price,lang="fr",emojis="none"):
	"""converted a float with 4 decimal max into gold, silver and bronze
	1.4586 = 1 gold 45 silver and 86 bronze"""
	gold = int(price//1)
	silver = int(100*(price%1))
	copper = round(((100*(price%1))%1)*100)
	#print(gold,"gold",silver,"silver and",copper,"copper")
	if lang=="fr":
		res = str(gold)+" or "+str(silver)+" argent "+str(copper)+" cuivre "
	elif lang=="eng":
		res = str(gold)+" gold "+str(silver)+" silver "+str(copper)+" copper "
	elif lang=="discord":
		res = f"{gold} {emojis[0]}  {silver} {emojis[1]}  {copper} {emojis[2]}"
	return res

def random_key(dico):
	"""pick a random key of a dictionary"""
	liste=[]
	for k in dico.keys():
		liste+=[k]
	return random.choice(liste)

def createRandomItem():
	WEAPONS=[Item(equipable=True,slotequipable="weapon",name="baguette",shortName="wand",image="./img/items/wand_commun.png",grade="commun",price=0.1,stats={"dmg":1,"tps":1,},description="Une baguette magique...")
		]
	WEAPONSBIS=[Item(equipable=True,slotequipable="weaponbis",name="orbe",shortName="orbe",image="./img/items/wand_commun.png",grade="commun",price=0.1,stats={"speed":1,"shot_speed":1},description="Une orbe magique...")
	]
	#"weaponbis":WEAPONSBIS,
	DICOEQUIPEMENT={
			"weapon":WEAPONS,
			"head": [Item(equipable=True,slotequipable="head",name="casque",shortName="casque",image="./img/items/head_commun.png",grade="commun",price=0.1,stats={"hp":1},description="Un casque...")],
			"chest":[Item(equipable=True,slotequipable="chest",name="Plastron",shortName="Plastron",image="./img/items/chest_commun.png",grade="commun",price=0.1,stats={"hp":1},description="Un plastron...")],
			"glove":[Item(equipable=True,slotequipable="glove",name="Gants",shortName="Gants",image="./img/items/glove_commun.png",grade="commun",price=0.1,stats={"hp":1,"tps":1},description="Une paire de gants...")],
			"boot":[Item(equipable=True,slotequipable="boot",name="Bottes",shortName="Bottes",image="./img/items/boot_commun.png",grade="commun",price=0.1,stats={"hp":1,"speed":1},description="Des bottes...")],
			"earrings":[Item(equipable=True,slotequipable="earrings",name="Boucles d'oreille",shortName="earrings",image="./img/items/earrings_commun.png",grade="commun",price=0.1,stats={"dmg":1},description="Un casque...")],
			"belt":[Item(equipable=True,slotequipable="belt",name="Ceinture",shortName="Ceinture",image="./img/items/belt_commun.png",grade="commun",price=0.1,stats={"shot_speed":1},description="Un casque...")]
			}
	#on choisi si l'item sera un item equipable ou pas
	equipable=choices([True,False], weights=[10,90])[0]
	if equipable:
		slotequipable=choice(["head","chest","glove","boot","weapon","earrings","belt"])

	#si il est equipable
	if equipable:
		basicStats={"hp":100,"dmg":12,"speed":6,"tps":2,"shot_speed":8}
		#on prend un item de référence
		item = choice(DICOEQUIPEMENT[slotequipable])

		#on choisi un grade
		grade = choices(["commun","rare","mythique","légendaire"], weights = [50,45,4,1])[0]
		item.grade=grade
		#en fonction du grade on modifie les stats
		gradeFactor = {"commun":1,"rare":1.5,"mythique":2,"légendaire":3}
		for k in item.stats.keys():
			item.stats[k] = gradeFactor[grade] * item.stats[k]
		#en fonction du grade on modifie le prix
		gradeFactor ={"commun":1,"rare":8,"mythique":16,"légendaire":32}
		for k in item.stats:
			item.price = gradeFactor[grade] * item.price
		#en fonction du grade on change l'image
		if item.slotequipable not in ["weapon","weaponbis"]:
			item.image = pygame.image.load("./img/items/"+item.slotequipable+"_"+grade+".png")
		else:
			item.image = pygame.image.load("./img/items/"+item.shortName+"_"+grade+".png")
	#si il n'est pas equipable
	else:
		lsPlants=[]
		for i in range(1,49):
			lsPlants+=[str(i)]
		dicNameImg={
		"food":["beer","cake","fish","meal","meat","noodles","onigiri","pizza","steak","strawberry","tomato","whiskey"],
		"misc":["ambre","diamond","emerauld","leather","metal","plank","rubis","stone","wood"],
		"plants":lsPlants
		}
		categorie=choice(["food","misc","plants"])
		itemname=choice(dicNameImg[categorie])
		#on set le prix
		prix=randint(1,50)/100
		#on set les stats si possible
		if categorie=="food":
			stats={"heal":5}
		else:
			stats={}

		item = Item(equipable=False,slotequipable=-1,name=itemname,shortName=itemname,image="./img/"+categorie+"/"+itemname+".png",grade="commun",price=prix,stats=stats,description="Un item pouvant s'avérer utile. Vous pouvez le vendre à un marchant.")

		if categorie=="plants":
			#on recupère l'image du l'item
			item.image = pygame.transform.scale(item.image,(64,64))
			#on la resize
			item.rect = item.image.get_rect()


	return item



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

print("test")

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


def drawItemOverlay(screen,mx, my,itemlist,inventaire):
	
	hoverAnItem=False
	for item in itemlist:
		if item.hoover(mx, my):
			itemHoover=item
			hoverAnItem=True

	if hoverAnItem:
		width=200
		height=300

		if my > SCREEN_HEIGHT-250:
			decalY=-300
		else:
			decalY=0

		if itemHoover.slot in inventaire.equipement.keys():
			decalX=0
			decalXText = 360
			factTextStat = 0.10
			#on dessine le cadre
			border = pygame.Rect(mx,my+decalY,width+10,height+10)
			fond = (mx+5,my+5+decalY,width,height)
		else:
			decalX = -200
			decalXText = -200
			factTextStat = -0.9
			#on dessine le cadre
			border =(mx+decalX-5,my-5+decalY,width+10,height+10)
			fond = (mx+decalX,my+decalY,width,height)


		
		
		#on dessine le cadre
		pygame.draw.rect(screen,(100,64,31),border)
		pygame.draw.rect(screen,(164,131,80),fond)

		#on recupère l'image du l'item
		img = pygame.transform.scale(itemHoover.image,(50,50))
		#on la resize
		rect = img.get_rect()
		#on la place en haut à gauche du cadre
		rect = rect.move((mx+decalX+10, my+10+decalY))
		screen.blit(img, rect)

		#on dessine le nom (titre):
		if len(itemHoover.name) > 10:
			txt=itemHoover.shortName
		else:
			txt=itemHoover.name
		draw_text(screen,txt, 'fonts/No_Color.ttf', 20, BLACK, mx+(0.75*(decalXText//2)), my+30+decalY, True)

		#le grade
		draw_text(screen,itemHoover.grade, 'fonts/No_Color.ttf', 10, COLOR_OF_GRADE[itemHoover.grade], mx+(0.75*(decalXText//2)), my+50+decalY, True)

		#les stats
		i=0
		for stat in itemHoover.stats.keys():
			txt=stat+" : "+str(itemHoover.stats[stat])
			color=BLACK
			if itemHoover.slotequipable in inventaire.equipement.keys():
				if inventaire.equipement[itemHoover.slotequipable]!=False and inventaire.equipement[itemHoover.slotequipable].stats[stat] < itemHoover.stats[stat]:
					color = GREEN
				elif inventaire.equipement[itemHoover.slotequipable]!=False and inventaire.equipement[itemHoover.slotequipable].stats[stat] > itemHoover.stats[stat]:
					color = RED
			draw_text(screen,txt, 'fonts/No_Color.ttf', 12, color, mx+(factTextStat*200), my+100+(i*15)+decalY, False)
			i+=1

		#la description
		lenLigne=22
		nblignes=int(len(itemHoover.description)/(lenLigne+1))
		startletter=0
		for j in range(nblignes+2):
			if j <nblignes:
				if itemHoover.description[startletter+lenLigne]!=" ":
					draw_text(screen,itemHoover.description[startletter:startletter+lenLigne]+"-", 'fonts/No_Color.ttf', 12, BLACK, mx+(factTextStat*200), my+100+(i+2*15)+decalY+(j*15), False)
				else:
					draw_text(screen,itemHoover.description[startletter:startletter+lenLigne], 'fonts/No_Color.ttf', 12, BLACK, mx+(factTextStat*200), my+100+(i+2*15)+decalY+(j*15), False)
			else:
				draw_text(screen,itemHoover.description[startletter:startletter+lenLigne], 'fonts/No_Color.ttf', 12, BLACK, mx+(factTextStat*200), my+100+(i+2*15)+decalY+(j*15), False)
			startletter+=lenLigne
		



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
				if event.key == pygame.K_q and inventaire.numOfItems() < inventaire.size:
					item=createRandomItem()
					itemlist.add(item)
					all_sprites.add(item)
					inventaire.add(item)

				if event.key == pygame.K_i:
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
		# Dessine tous les sprites (les blits sur screen)
		all_sprites.draw(screen)

		#si besoin on dessine l'overlay de l'item
		if activeMouse[0] == False:
			drawItemOverlay(screen,mx, my,itemlist,inventaire)

		pygame.display.update()
		fpsClock.tick(60)
