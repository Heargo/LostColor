import pygame, sys
from pygame.locals import *
import random
from math import sqrt
# import matplotlib.pyplot as plt
# import PIL.ImageDraw as ImageDraw
# import PIL.Image as Image
########################################
###############ALGO V1##################
########################################

def minDistPoints(points):
	#on initialise mini avec la distance des eux premiers points du polygone
	mini=sqrt((points[0][0]-points[1][0])**2+(points[0][1]-points[1][1])**2)
	#on compare chaque point avec tout les autres pour trouver la plus petite distance
	for p in points:
		for p2 in points:
			if p!=p2:
				dist=sqrt((p2[0]-p[0])**2+(p2[1]-p[1])**2)
				if dist<mini:
					mini=dist

	return int(mini)

def randomPoint(p1,p2,rend):
	x1=p1[0]
	y1=p1[1]
	x2=p2[0]
	y2=p2[1]

	n=random.random()
	if x1 != x2:
		a=(y2-y1)/(x2-x1)
		x=(x2-x1)*n+x1
		y=a*(x-x1)+y1
	else:
		x=x1
		y=(y2-y1)*n+y1

	rx=random.randint(0,rend)
	ry=random.randint(0,rend)
	return (int(x+rx),int(y+ry))


def polygone(n):
	p=[]
	for i in range(0,n):
		x=random.randint(10,300)
		y=random.randint(10,300)
		#plt.scatter(x,y, s=50)
		p+=[(x,y)]

	return p


def lines(p):
	linesLS=[]
	for i in range(len(p)):
		start=p[i]
		if i==len(p)-1:
			end=p[0]
		else:
			end=p[i+1]

		linesLS+=[[start,end]]
	return linesLS

def extend(p,n):
	ext=[]
	lsLines=lines(p)
	s=40
	for i in range(n):
		for j in range(len(lsLines)):
			s=s-2
			if s <0:
				s=1
			line=lsLines[j]
			start=line[0]
			end=line[1]
			rend=minDistPoints(p)
			newp = randomPoint(start,end,rend)
			#plt.scatter(newp[0],newp[1], s=s)
			ext+=[start,newp]
		lsLines=lines(ext)

	return ext



pygame.init()
# Definition des FPS
fpsClock = pygame.time.Clock()

# --- Création de la fenetre
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Editeur de taches LostColor')
poly=[]
running = True
# -------- Main Program Loop -----------
while running:
	click=False
	#fermeture de la fenetre
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	#clic de la souris
	if event.type == MOUSEBUTTONDOWN:
		if event.button == 1:
			click=True
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RETURN  and len(poly)>0:
			print("------------------{ Polygone }------------------")
			print(poly)
			print("------------------------------------------------")
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_w:
			print("------------------{ CTRL+Z }------------------")
			poly=poly[:len(poly)-2]

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_r:
			print("------------------{ RESET }------------------")
			poly=[]

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_q:
			print("------------------{ RANDOM POLY }------------------")
			# #on commence avec un polygone
			p=polygone(3)
			#on l'étend
			poly=extend(p,1)

	if click:
		#on recupère les coordonnées de la souris
		mx, my = pygame.mouse.get_pos()
		if (mx,my) not in poly:
			#on ajoute le point au polygone
			poly+=[(mx,my)]


	

	#affichage 
	screen.fill((255, 255, 255))

	#draw points
	for p in poly:
		pygame.draw.circle(screen, (255,0,0), p, 2)

	if len(poly)>1:
		#draw lignes
		for i in range(0,len(poly)):
			pygame.draw.line(screen, (0,0,255), poly[i-1], poly[i], 2)

	pygame.display.update()
	fpsClock.tick(60)

pygame.quit()
sys.exit()