from menu import *
import pygame, sys
from pygame.locals import *
from constants import *
from random import choice, choices, randint
import controls
from inventaire import createRandomItem
from player import *




# Création du joueur
player = Player("Test", 0, 0)
player.initStats()
player.inventaire.items=[False]*player.inventaire.size
player.updateStats()
for i in range(2):
	item=createRandomItem()
	player.inventaire.add(item)
	print(item.name)








def drawCraftOverlay(screen,page):
	#on dessine les background
	largeur =505
	hauteur = 100
	spaceBetween = 15
	for i in range(5):
		###FOND
		#inventaire fond
		pygame.draw.rect(screen,(164,131,80),(690,40+(i*hauteur+i*spaceBetween),largeur,hauteur))
		#inventaire bords
		pygame.draw.rect(screen,(100,64,31),(690,40+(i*hauteur+i*spaceBetween),largeur,hauteur),5)
		
		##APPERCU

def drawResultOverlay(screen,actif):
	#profil fond
	pygame.draw.rect(screen,(164,131,80),(50,40,505,560))
	#profil bords
	pygame.draw.rect(screen,(100,64,31),(50,40,505,560),5)







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
actif=1
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
		for bouton in boutonList:
			#si on est dessus 
			if bouton.hoover(mx,my):
				print("j'ai cliqué sur un bouton")


	# Appelle la méthode update() de tous les Sprites
	all_sprites.update()
	#on met l'ecran en blanc
	screen.fill((255,255,255))

	#on dessine la liste des crafts de la page
	drawCraftOverlay(screen,page)

	#resultat du craft actif
	drawResultOverlay(screen,actif)
	# Dessine tous les sprites (les blits sur screen)
	all_sprites.draw(screen)



	pygame.display.update()
	fpsClock.tick(60)