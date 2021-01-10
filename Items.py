import pygame, sys
from pygame.locals import *
from constants import *
from random import choice, choices, randint
from tools import draw_text, to_gold, random_key

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
		self.originalImage=self.image
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
		self.image = self.originalImage
		print(self.image,self.originalImage)
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
		

def createRandomItem(typeItem="default",gradeItem="default",categorie="default",itemname="default"):
	WEAPONS=[Item(equipable=True,slotequipable="weapon",name="baguette",shortName="wand",image="./img/items/wand_commun.png",grade="commun",price=2,stats={"dmg":5,"tps":4,},description="Une baguette magique...")
		]
	WEAPONSBIS=[Item(equipable=True,slotequipable="weaponbis",name="orbe",shortName="orbe",image="./img/items/wand_commun.png",grade="commun",price=2,stats={"speed":0.1,"shot_speed":4},description="Une orbe magique...")
	]
	#"weaponbis":WEAPONSBIS,
	DICOEQUIPEMENT={
			"weapon":WEAPONS,
			"head": [Item(equipable=True,slotequipable="head",name="casque",shortName="casque",image="./img/items/head_commun.png",grade="commun",price=1,stats={"hp":10},description="Un casque...")],
			"chest":[Item(equipable=True,slotequipable="chest",name="Plastron",shortName="Plastron",image="./img/items/chest_commun.png",grade="commun",price=1,stats={"hp":30},description="Un plastron...")],
			"glove":[Item(equipable=True,slotequipable="glove",name="Gants",shortName="Gants",image="./img/items/glove_commun.png",grade="commun",price=1,stats={"hp":10,"tps":1},description="Une paire de gants...")],
			"boot":[Item(equipable=True,slotequipable="boot",name="Bottes",shortName="Bottes",image="./img/items/boot_commun.png",grade="commun",price=1,stats={"hp":10,"speed":0.5},description="Des bottes...")],
			"earrings":[Item(equipable=True,slotequipable="earrings",name="Boucles d'oreille",shortName="earrings",image="./img/items/earrings_commun.png",grade="commun",price=1.5,stats={"dmg":5},description="Un casque...")],
			"belt":[Item(equipable=True,slotequipable="belt",name="Ceinture",shortName="Ceinture",image="./img/items/belt_commun.png",grade="commun",price=1,stats={"shot_speed":2},description="Un casque...")]
			}
	#on choisi si l'item sera un item equipable ou pas
	if typeItem =="default":
		equipable=choices([True,False], weights=[10,90])[0]
		if equipable:
			slotequipable=choice(["head","chest","glove","boot","weapon","earrings","belt"])
	else:
		if typeItem in DICOEQUIPEMENT:
			equipable=True
			slotequipable=typeItem
		else:
			equipable=False

	#si il est equipable
	if equipable:
		basicStats={"hp":100,"dmg":12,"speed":6,"tps":2,"shot_speed":8}
		#on prend un item de référence
		item = choice(DICOEQUIPEMENT[slotequipable])

		#on choisi un grade
		if gradeItem=="default":
			grade = choices(["commun","rare","mythique","légendaire"], weights = GRADES_WEIGHTS)[0]
		else:
			grade = gradeItem
		item.grade=grade

		#en fonction du grade on modifie les stats
		gradeFactor = {"commun":1,"rare":1.5,"mythique":2,"légendaire":3}
		for k in item.stats.keys():
			item.stats[k] = gradeFactor[grade] * item.stats[k]

		#en fonction du grade on modifie le prix
		gradeFactor ={"commun":1,"rare":8,"mythique":16,"légendaire":32}
		item.price = gradeFactor[grade] * item.price
		for k in item.stats:
			item.price+=2

		#en fonction du grade on change l'image
		if item.slotequipable not in ["weapon","weaponbis"]:
			item.image = pygame.image.load("./img/items/"+item.slotequipable+"_"+grade+".png")
			item.originalImage=item.image
			key=item.slotequipable+"_"+grade
		else:
			item.image = pygame.image.load("./img/items/"+item.shortName+"_"+grade+".png")
			item.originalImage=item.image
			key = item.shortName+"_"+grade

		item.name = NOMSITEMS[key][randint(0,len(NOMSITEMS[key])-1)]
		item.description = DESCRIPTIONSITEMS[key][randint(0,len(DESCRIPTIONSITEMS[key])-1)]

	#si il n'est pas equipable
	else:
		if categorie=="default":
			categorie=choice(["food","misc","plants"])
		if itemname == "default":
			itemname=choice(dicNameImg[categorie])
		#on set le prix
		prix=randint(5,15)/100
		#on set les stats si possible
		if categorie=="food":
			stats={"heal":5}
			prix*=3
		else:
			stats={}

		item = Item(equipable=False,slotequipable=-1,name=itemname,shortName=itemname,image="./img/"+categorie+"/"+itemname+".png",grade="commun",price=prix,stats=stats,description="Un item pouvant s'avérer utile. Vous pouvez le vendre à un marchant.")

		if categorie=="plants":
			#on recupère l'image du l'item
			item.image = pygame.transform.scale(item.image,(64,64))
			#on la resize
			item.rect = item.image.get_rect()
			#on met a jour le nom et la description
			item.name = NOMSPLANTES[itemname][0]
			item.shortName = "Plante"
			item.description = DESCRIPTIONSPLANTES[itemname][0]
			#item.description = DESCRIPTIONSITEMS[itemname][randint(0,len(DESCRIPTIONSITEMS[key])-1)]
		elif categorie =="misc":
			item.name = NOMSDIVERS[itemname][0]
			item.shortName = NOMSDIVERS[itemname][0]
			item.description = DESCRIPTIONSDIVERS[itemname][0]
		elif categorie =="food":
			item.name = NOMSFOOD[itemname][randint(0,len(NOMSFOOD[itemname])-1)]
			item.shortName = NOMSFOOD[itemname][0]
			item.description = DESCRIPTIONSFOOD[itemname][0]


	return item

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
		pygame.draw.rect(screen,COLOR_OF_GRADE[itemHoover.grade],border)
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

		draw_text(screen,itemHoover.name, 'fonts/No_Color.ttf', 10, BLACK, mx+(factTextStat*200), my+80+decalY, False)
		draw_text(screen,"prix : "+to_gold(itemHoover.price), 'fonts/No_Color.ttf', 10, BLACK, mx+(factTextStat*200), my+100+decalY, False)

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
			draw_text(screen,txt, 'fonts/No_Color.ttf', 12, color, mx+(factTextStat*200), my+130+(i*15)+decalY, False)
			i+=1

		#la description
		lenLigne=22
		nblignes=int(len(itemHoover.description)/(lenLigne+1))
		startletter=0
		for j in range(nblignes+2):
			if j <nblignes:
				if itemHoover.description[startletter+lenLigne]!=" ":
					draw_text(screen,itemHoover.description[startletter:startletter+lenLigne]+"-", 'fonts/No_Color.ttf', 12, BLACK, mx+(factTextStat*200), my+130+(i+2*15)+decalY+(j*15), False)
				else:
					draw_text(screen,itemHoover.description[startletter:startletter+lenLigne], 'fonts/No_Color.ttf', 12, BLACK, mx+(factTextStat*200), my+130+(i+2*15)+decalY+(j*15), False)
			else:
				draw_text(screen,itemHoover.description[startletter:startletter+lenLigne], 'fonts/No_Color.ttf', 12, BLACK, mx+(factTextStat*200), my+130+(i+2*15)+decalY+(j*15), False)
			startletter+=lenLigne
