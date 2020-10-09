import pygame
from player import Player
import const
pygame.init()



screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
FPS = 60

running=True
player = Player("Test", 0,0)

def showEntity(E):
	"""Show showEntity E """
	#update player position using direction speed movement (dirX or dirY)
	E.setX(E.getDirX()+E.getX())
	E.setY(E.getDirY()+E.getY())
	#show player on screen
	playerImg = screen.blit(pygame.image.load(E.getAvatar()),(E.getX(),E.getY()))

def noMovingKeyDown(event_list): #a voir pour faire un truc smooth
	res = True
	for event in event_list:
		if event.type == pygame.KEYDOWN:
			#movements
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
				res=False
	return res

while running:
	dt = clock.tick(FPS) / 1000
	screen.fill((0,0,0))
	#player.moveRight(0.1)
	event_list=pygame.event.get()
	for event in event_list:
		#close game
		if event.type == pygame.QUIT:
			running = False
		#key pressed
		if event.type == pygame.KEYDOWN:
			#movements
			carac= event.dict['unicode'] # On récupère la touche tapée grâce à sa référence unicode et on va la comparer aux différents caractères possibles
			if carac== 'q': #left
				player.moveLeft(const.speedX*dt) 
			elif carac== 'd': #right
				player.moveRight(const.speedX*dt) 
			elif carac== 'z': #top
				player.moveTop(const.speedY*dt) 
			elif carac== 's': #bottom
				player.moveBottom(const.speedY*dt) 

		#key relased 
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_w or event.key == pygame.K_s: 
				player.stopY()
			elif event.key == pygame.K_a or event.key == pygame.K_d:
				player.stopX()


	
	showEntity(player)
	pygame.display.update()




