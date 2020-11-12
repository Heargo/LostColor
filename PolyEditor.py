import pygame, sys
from pygame.locals import *
import random
from math import sqrt
from constants import *
from proceduralGeneration import createPrimaryPath, ExtendPath, drawMap
# import matplotlib.pyplot as plt
# import PIL.ImageDraw as ImageDraw
# import PIL.Image as Image



########################################
###############ALGO V1##################
########################################

def minDistPoints(points):
	#on initialise mini avec la distance des deux premiers points du polygone
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

def drawPolygones(screen,poly_list):
    for p in poly_list:
        pygame.draw.polygon(screen, p[1], p[0],0)

########################################
###############ALGO 2 ##################
########################################
 
def randomPoints(n,size):
	"""renvoie une liste de points tiré aléatoirement dans un rectangle de taile size"""
	lsPoints=[]
	h=size[1]
	w=size[0]
	for i in range(n):
		x=random.randint(0,w)
		y=random.randint(0,h)
		lsPoints+=[(x,y)]
	return lsPoints

def distPlusProche(p,pts):
	"""Renvoie la distance entre le point p et le point le plus proche parmis les points"""
	points=pts[::]

	#on enleve p de la liste des points en cas de répétition
	if p in points:
		points.remove(p)
	#on initialise mini avec la distance au premier point de la liste des points
	mini=sqrt((p[0]-points[0][0])**2+(p[1]-points[0][1])**2)
	#on compare chaque point avec p pour trouver la plus petite distance
	for p2 in points:
		dist=sqrt((p2[0]-p[0])**2+(p2[1]-p[1])**2)
		if dist<mini:
			mini=dist

	return round(mini)


def randomHomogenePoints(n):
	"""renvoie une liste de points qui sont répartis homogénement (a plus de 300px les uns des autres) mais aléatoirement """
	res=[]
	lsbase=[]
	for i in range(n):
		randomX= random.randint(0,SCREEN_WIDTH)
		randomY = random.randint(0,SCREEN_HEIGHT)
		print(lsbase)
		if len(lsbase)>1:
			while distPlusProche((randomX,randomY),lsbase) < 300:
				randomX= random.randint(0,SCREEN_WIDTH)
				randomY = random.randint(0,SCREEN_HEIGHT)

		lsbase+=[(randomX,randomY)]
	return lsbase

def drawTache(tache):
	#draw circles
	for cercle in tache[0]:
		centre=cercle[0]
		rayon=cercle[1]
		pygame.draw.circle(screen, tache[1], centre, rayon)




def createTache(taille):
	n= random.randint(taille[0],taille[1])
	lsCenters=randomPoints(n,(200,200))
	lsCircles=[]
	tot=(0,0)
	for c in lsCenters:
		rayon=distPlusProche(c,lsCenters)
		tot=(tot[0]+c[0],tot[1]+c[1])
		lsCircles+=[[c,rayon]]
	color=random.choice([RED,GREEN,BLUE])
	return [lsCircles,color]

def createNTaches(n,taille):
	lsTaches=[]
	#on créer les taches
	for i in range(n):
		lsTaches+=[createTache(taille)]
	#on créer une disposition aléatoire sur la map
	points=randomHomogenePoints(n)
	#on applique cette position a chaque tache
	for i in range(len(lsTaches)):
		tache=lsTaches[i][0]
		pos=points[i]
		for cercle in tache:
			cercle[0] =(cercle[0][0]+pos[0],cercle[0][1]+pos[1])
		lsTaches[i][0]=tache	

	return lsTaches

def drawAllTaches(taches):
	for tache in taches:
		drawTache(tache)



##################################################################################################

def resizePoly(poly,facteur):
	res=[]
	for p in poly:
		x=int(p[0]*facteur)
		y=int(p[1]*facteur)
		res+=[(x,y)]
	return res






pygame.init()
# Definition des FPS
fpsClock = pygame.time.Clock()

# --- Création de la fenetre
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Editeur de taches LostColor')

#polyaresize=[(439, 557), (585, 569), (911, 560), (1003, 383), (929, 211), (733, 123), (507, 125), (699, 350)]


poly=[]#resizePoly(polyaresize,0.5)
lsCenters=[]
lsCircles=[]
previous=[]
bary=()
taches=[]
running = True
notPressedBefore=True

n=40
path,allRoomsCoordinates=createPrimaryPath(n)
#affichage des données
# for salle in path.values():
# 	print(salle.id)
# 	print(salle.doors)
allRoomsCoordinates=ExtendPath(path,allRoomsCoordinates)
#print(allRoomsCoordinates)
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
	
	#touche pressée
	if event.type == pygame.KEYDOWN and notPressedBefore:
		if event.key == pygame.K_RETURN:
			if len(poly)!=0:
				print("--{ Polygone }--")
				print(poly)
				print("----------------")
			if len(lsCircles)!=0:
				print("--{ Tache }--")
				print(lsCircles)
				print("---------------")
			notPressedBefore=False

		if event.key == pygame.K_w:
			print("CTRL+Z")
			poly=poly[:len(poly)-2]
			notPressedBefore=False

		if event.key == pygame.K_r:
			print("RESET")
			poly=[]
			lsCenters=[]
			lsCircles=[]
			bary=()
			taches=[]
			notPressedBefore=False

		if event.key == pygame.K_q:
			print("RANDOM POLY")
			#on commence avec un polygone
			p=polygone(3)
			#on l'étend
			poly=extend(p,1)
			notPressedBefore=False

		if event.key == pygame.K_p:
			print("ALL TACHES")
			#on creer toutes les taches
			n=random.randint(3,10)
			taches=createNTaches(n,(6,20))
			notPressedBefore=False
				

		if event.key == pygame.K_o:
			print("------------------{ Cercles }------------------")
			nbpoints=10
			lsCenters=randomPoints(nbpoints,(200,200))
			lsCircles=[]
			tot=(0,0)
			for c in lsCenters:
				rayon=distPlusProche(c,lsCenters)
				tot=(tot[0]+c[0],tot[1]+c[1])
				lsCircles+=[(c,rayon)]
			bary=(tot[0]//len(lsCenters),tot[1]//len(lsCenters))
			notPressedBefore=False

	#touche relachée
	if event.type == pygame.KEYUP:
		if event.key in [pygame.K_RETURN,pygame.K_w,pygame.K_q,pygame.K_o,pygame.K_r]:
			notPressedBefore=True
			

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

	#draw circles
	for c in lsCenters:
		cCentree=(c[0]+400,c[1]+200)
		rayon=distPlusProche(c,lsCenters)
		pygame.draw.circle(screen, (255,0,0), cCentree, rayon)

	if len(bary)!=0:
		baryCentree=(bary[0]+400,bary[1]+200)
		pygame.draw.circle(screen, (0,0,255), baryCentree, 3)

	if len(taches)>0:
		drawAllTaches(taches)

	if len(poly)>1:
		#draw lignes
		for i in range(0,len(poly)):
			pygame.draw.line(screen, (0,0,255), poly[i-1], poly[i], 2)


	drawMap(screen,path,allRoomsCoordinates,n)

	pygame.display.update()
	fpsClock.tick(60)

pygame.quit()
sys.exit()