import pygame, sys
from pygame.locals import *
from Ennemis import *
from player import Player

pygame.init()
#Definition des FPS
FPS = 60
fpsClock = pygame.time.Clock()

# Initialisation de couleur et constantes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255, 0)
BLUE = (0, 0, 255)
 
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# --- Fonction
def spawnNMonsters(N):
    """Cette fonction fait appraitre le nombre en entrée énnemis"""
    for i in range(0, N):
        monstre = Monstre1(random.randint(0, SCREEN_WIDTH),
              random.randint(0, SCREEN_HEIGHT//3),
              player)
        enemy_list.add(monstre)
        all_sprites_list.add(monstre)

# --- Création de la fenetre
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('LostColor')

# --- Listes de Sprites
# Ceci est la liste de tous les sprites. Tous les ennemis et le joueur aussi.
# Un groupe de sprite LayeredUpdates possede en plus un ordre (pour l'affichage)
all_sprites_list = pygame.sprite.LayeredUpdates()

# Liste de tous les ennemis
enemy_list = pygame.sprite.Group() 

# --- Creation des Sprites
#Création du joueur
player = Player("Test", 0,0,6)


player.rect.centerx = 2*SCREEN_WIDTH//3
player.rect.centery = 2*SCREEN_HEIGHT//3

#Création d'un monstre
m1 = Monstre1(random.randint(0, SCREEN_WIDTH),
              random.randint(0, SCREEN_HEIGHT//3),
              player)

# Ajout du monstre sprite dans le Group enemy_list
enemy_list.add(m1)

# Ajout des sprite dans l'ordre d'affichange dans le Group all_sprites_list
all_sprites_list.add(m1)
all_sprites_list.add(player)

# -------- Main Program Loop -----------
running=True

while running:

	# --- Gestion des Event
	for event in pygame.event.get():

        #close game
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP5: #bottom
				spawnNMonsters(3)
        
	#Detection d'utilisation du clavier pour déplacer le joueur:
	activeKey=pygame.key.get_pressed()
	
	if activeKey[K_a]:#left
		player.move("LEFT") 
	if activeKey[K_d]: #right
		player.move("RIGHT")  
	if activeKey[K_w]: #top
		player.move("UP") 
	if activeKey[K_s]: #bottom
		player.move("DOWN")


	#Detection d'utilisation du clavier pour faire spawner 3 monstres
	

	# --- Logique du jeu
	
	# Appelle la méthode update() de tous les Sprites
	all_sprites_list.update()

    # --- Dessiner la frame
    # Clear the screen

	screen.fill(WHITE)
        
    # Dessine tous les sprites (les blits sur screen)
	all_sprites_list.draw(screen)

    # Met à jour la fenetre de jeu
	pygame.display.update()
        
    # --- Limite le jeu à 60 images par seconde
	fpsClock.tick(FPS)


pygame.quit()
sys.exit()


