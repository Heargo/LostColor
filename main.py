import pygame
from pygame.locals import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((1280,720))

running=True
player = Player("Test", 0,0,3)
playerImg = screen.blit(player.image,(player.x,player.y))
# limiter le taux de rafraichissement
clock = pygame.time.Clock()
while running:
	for event in pygame.event.get():
		#close game
		if event.type == pygame.QUIT:
			running = False

	activeKey=pygame.key.get_pressed()
	#movements
	if activeKey[K_a]:#left
		player.move("LEFT") 
	if activeKey[K_d]: #right
		player.move("RIGHT")  
	if activeKey[K_w]: #top
		player.move("UP") 
	if activeKey[K_s]: #bottom
		player.move("DOWN") 


	screen.fill((0,0,0))
	playerImg = screen.blit(player.image,player.rect)
	pygame.display.update()




