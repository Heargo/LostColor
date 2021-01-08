from menu import *
import pygame, sys
from pygame.locals import *
from constants import *
from random import choice, choices, randint
import controls
from inventaire import createRandomItem
from player import *
from Items import drawItemOverlay, createRandomItem
from tools import draw_text


# Création du joueur
player = Player("Test", 0, 0)
player.initStats()
player.inventaire.items=[False]*player.inventaire.size
player.updateStats()
for i in range(20):
	item=createRandomItem()
	player.inventaire.add(item)

#les crafts/recette
ITEMS_RECIPES=[]
for i in range(0,len(RECIPES) ):
	#print(RECIPES[i]["img"])
	ITEMS_RECIPES.append(
		{"item":createRandomItem(typeItem=RECIPES[i]["slot"],gradeItem=RECIPES[i]["grade"]),
		"id":i,
		"craft":RECIPES[i]["craft"]
		}
		)

slots=[]
def craftsOfPage(page):
	#print("--PAGE",page)
	NewCrafts=[]
	listeCraftSprite=[]
	for i in range(( (page-1)*5 ),min( (page-1)*5+5 , len(ITEMS_RECIPES) ) ):
		NewCrafts.append(ITEMS_RECIPES[i])
		listeCraftSprite.append(ITEMS_RECIPES[i]["item"])
	return NewCrafts, listeCraftSprite


def nbIngredientInInv(ingredient,inventaire):
	nb=0
	for item in inventaire.items:
		if item !=False:
			if item.name==ingredient:
				nb+=1

	return nb

def nbIngDispo(craft,inv):
	maxi=0
	get=0
	for ing in craft:
		maxi+=craft[ing]
		if ing in dicNameImg["plants"]:
			name = NOMSPLANTES[ing][0]
		else:
			name = NOMSDIVERS[ing][0]
		get+=nbIngredientInInv(name,inv)
	return get,maxi



def drawCraftOverlay(screen,page,inventaire):
	global listeCraftSprite, slots
	#on dessine les background
	largeur =505
	hauteur = 100
	spaceBetween = 15
	crafts, listeCraftSprite = craftsOfPage(page)
	slots=[]
	for i in range(5):
		x = 700
		y = (i*hauteur+i*spaceBetween)
		item = listeCraftSprite[i]
		craft = crafts[i]["craft"]
		colorGrade = COLOR_OF_GRADE[item.grade]
		###FOND
		#inventaire fond
		s = pygame.Rect(690,40+y,largeur,hauteur)
		pygame.draw.rect(screen,(164,131,80),s)
		#inventaire bords
		pygame.draw.rect(screen,(100,64,31),s,5)

		##APPERCU
		img = pygame.transform.scale(item.image,(64,64))
		#on la resize
		rect = img.get_rect()
		#on la place en haut à gauche du cadre
		pos= (700, 60+y)
		rect = rect.move(pos)
		item.move(pos)
		screen.blit(img, rect)

		#NOM
		if len(item.name) > 20:
			txt=item.shortName
		else:
			txt=item.name
		draw_text(screen,txt, 'fonts/No_Color.ttf', 20, BLACK, 780,60+y, False)
		#grade
		draw_text(screen,item.grade, 'fonts/No_Color.ttf', 15, colorGrade, 780,90+y, False)

		#ingrédients dispo
		dispo,needed = nbIngDispo(craft,inventaire)
		draw_text(screen,str(dispo)+" / "+str(needed), 'fonts/No_Color.ttf', 30, BLACK, 1050,70+y, False)

		slots.append([s,crafts[i]])





def drawResultOverlay(screen,actif,inventaire):
	#profil fond
	pygame.draw.rect(screen,(164,131,80),(50,40,505,560))
	#profil bords
	pygame.draw.rect(screen,(100,64,31),(50,40,505,560),5)

	item = actif["item"]
	colorGrade = COLOR_OF_GRADE[item.grade]
	craft = actif["craft"]

	##APPERCU
	img = pygame.transform.scale(item.image,(64,64))
	#on la resize
	rect = img.get_rect()
	#on la place en haut à gauche du cadre
	pos= (100, 60)
	rect = rect.move(pos)
	screen.blit(img, rect)


	#NOM
	if len(item.name) > 20:
		txt=item.shortName
	else:
		txt=item.name
	draw_text(screen,txt, 'fonts/No_Color.ttf', 30, BLACK, 350,80, True)
	#grade
	draw_text(screen,item.grade, 'fonts/No_Color.ttf', 20, colorGrade, 350,110, True)

	#ingrédients dispo
	i=0
	for ingredient in craft:
		name = ingredient
		quantity = craft[ingredient]

		#visuel
		if ingredient in dicNameImg["misc"]:
			cat = "misc/"
			name = NOMSDIVERS[ingredient][0]
		else:
			cat = "plants/"
			name = NOMSPLANTES[ingredient][0]
		img =  pygame.image.load("./img/"+cat+ingredient+".png")
		img = pygame.transform.scale(img,(32,32))
		rect = img.get_rect()
		#on la place
		pos= (100, 300+i*40)
		rect = rect.move(pos)
		screen.blit(img, rect)


		#text
		draw_text(screen,name+"  "+str(nbIngredientInInv(name,inventaire))+"/"+str(quantity) , 'fonts/No_Color.ttf', 15, BLACK, 140,310+i*40, False)



		i+=1
	







pygame.init()
# Definition des FPS
fpsClock = pygame.time.Clock()
# --- Création de la fenetre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('LostColor')

#liste des boutons
boutonList=pygame.sprite.Group()
#liste des slots de craft
craftSlotsList = pygame.sprite.Group()
#liste de tout les sprites
all_sprites=pygame.sprite.LayeredUpdates()

all_sprites.add(boutonList)
all_sprites.add(craftSlotsList)


craftScreenOn=True
page =1
actif=-1
# -------- Main Program Loop -----------
while craftScreenOn:
	#fermeture de la fenetre
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == controls.C_CRAFT or event.key == pygame.K_ESCAPE:
				craftScreenOn=False
			

	# Detection du clic gauche la souris et de sa position
	activeMouse = pygame.mouse.get_pressed()
	mx, my = pygame.mouse.get_pos()
	#si on clique
	if activeMouse[0] == True:
		#on regarde pour chaque bouton 
		for s in slots:
			#si on est dessus 
			if s[0].collidepoint(mx,my):
				print("j'ai cliqué sur un slot",s[1]["item"].name)
				actif = s[1]["id"]


	# Appelle la méthode update() de tous les Sprites
	all_sprites.update()
	#on met l'ecran en blanc
	screen.fill((255,255,255))

	#on dessine la liste des crafts de la page
	drawCraftOverlay(screen,page,player.inventaire)

	#resultat du craft actif
	if actif >=0:
		drawResultOverlay(screen,ITEMS_RECIPES[actif],player.inventaire)

	#si besoin on dessine l'overlay de l'item
	if activeMouse[0] == False:
		drawItemOverlay(screen,mx, my,listeCraftSprite,player.inventaire)

	# Dessine tous les sprites (les blits sur screen)
	all_sprites.draw(screen)



	pygame.display.update()
	fpsClock.tick(60)