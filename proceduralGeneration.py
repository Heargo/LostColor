import pygame, sys
import random
from constants import *
from Room import *
from Pnj import Instructor
def createPrimaryPathWithError(n,player):
	allRooms={}
	allRoomsCoordinates={}
	for i in range(n):
		#on init la salle
		if i == 0: # Pour la première salle
			currentroom = Room(player, i, difficulty="ultra_easy",lvl=1)
			#currentroom = Room(player, i, difficulty="boss") # Pour fair des tests sur le boss ds la 1ere salle
		elif i == n-1:  # On fait apparaitre le boss a la dernière salle
			currentroom = Room(player, i, difficulty="boss")
		else:
			random_difficulty = random.choices(DIFFICULTIES, weights = DIFFICULTIESWEIGHTS)[0]
			currentroom = Room(player, i, difficulty=random_difficulty,lvl=i)
		coordo=[0,0]
		#on ouvre sa porte en fonction de la salle précédente
		if i >0:
			previousRoom=allRooms[i-1]
			currentroom.openDoorFromPreviousRoom(previousRoom)
			coordo=calcCoordinates(previousRoom,currentroom.id,allRoomsCoordinates)
		

		allRoomsCoordinates[i]=coordo
		
		#on ouvre une nouvelle porte si ce n'est pas la dernière salle et si 
		if i < n-1:
			#on choisi une porte à ouvrir aléatoirement dans celles qui sont possibles
			if i==0:
				alea=random.choice(currentroom.doorsPossibleToOpen())
			else:
				doorsPossible=doorsPossibleToOpenWithCoords(currentroom,i+1,allRoomsCoordinates)
				#si il y a aucune porte possible, une erreur fait crash l'algo
				alea=random.choice(doorsPossible)
			currentroom.doors_id[alea]=i+1
		allRooms[i]=currentroom
	return allRooms,allRoomsCoordinates


def createTutorialWithError(player):
	#get info from TUTORIAL_DATA
	allRooms={}
	allRoomsCoordinates={}
	n=len(TUTORIAL_DATA)
	for i in range(n):
		roomDATA =TUTORIAL_DATA[i]
		#on init la salle
		currentroom = Room(player, i, difficulty=roomDATA["difficulty"],lvl=roomDATA["lvl"])
		coordo=[0,0]

		#on edit le pnj si besoin
		if currentroom.difficulty=="peaceful":
			currentroom.enemy_list.empty()
			currentroom.pnj_list.empty() #on vide la liste de pnj pour repartir a 0
			#print(roomDATA)
			pnj = Instructor(roomDATA["pnj-name"]) #créer le pnj
			pnj.say(roomDATA["pnj-dialogue"]) #on met a jour son dialogue
			currentroom.pnj_list.add(pnj)

		#on ouvre sa porte en fonction de la salle précédente
		if i >0:
			previousRoom=allRooms[i-1]
			currentroom.openDoorFromPreviousRoom(previousRoom)
			coordo=calcCoordinates(previousRoom,currentroom.id,allRoomsCoordinates)
		allRoomsCoordinates[i]=coordo
		
		#on ouvre une nouvelle porte si ce n'est pas la dernière salle
		if i < n-1:
			#on choisi une porte à ouvrir aléatoirement dans celles qui sont possibles
			if i==0:
				alea=random.choice(currentroom.doorsPossibleToOpen())
			else:
				doorsPossible=doorsPossibleToOpenWithCoords(currentroom,i+1,allRoomsCoordinates)
				#si il y a aucune porte possible, une erreur fait crash l'algo
				alea=random.choice(doorsPossible)
			currentroom.doors_id[alea]=i+1
		allRooms[i]=currentroom

	for salle in allRooms.values():
		#on créer les murs et les portes
		salle.walls_creation()
		salle.doors_creation()

	return allRooms,allRoomsCoordinates

def createTutorial(player):
	generer=False
	while not generer:
		try:
			allRooms,allRoomsCoordinates = createTutorialWithError(player)
			generer=True
		except:
			print("On ressaye de généré")
	return allRooms,allRoomsCoordinates

def createPrimaryPath(n,player):
	generer=False
	while not generer:
		try:
			allRooms,allRoomsCoordinates = createPrimaryPathWithError(n,player)
			generer=True
		except:
			print("On ressaye de généré")
	return allRooms,allRoomsCoordinates


def calcCoordinates(previousRoom,currentroomID,allRoomsCoordinates):
	#on trouve depuis on on vient
	for k in previousRoom.doors_id:
			if previousRoom.doors_id[k]==currentroomID:
				fromdoor=k
	relationDoors={"top":1,"bottom":-1,"left":-1,"right":1}
	#on calcul les coordonée de currentroom
	if fromdoor in ["top","bottom"]:
		x=allRoomsCoordinates[previousRoom.id][0]
		y=allRoomsCoordinates[previousRoom.id][1]+relationDoors[fromdoor]
	else:
		x=allRoomsCoordinates[previousRoom.id][0]+relationDoors[fromdoor]
		y=allRoomsCoordinates[previousRoom.id][1]

	return [x,y]


def doorsPossibleToOpenWithCoords(currentroom,futurRoomID,allRoomsCoordinates):
	res=[]
	for door in currentroom.doors_id:
		#si la porte n'existe pas 
		if currentroom.doors_id[door]==-1:
			working=True
			#on créer une porte vers l'emplacement de la futur salle
			currentroom.doors_id[door]=futurRoomID
			#on calcul les coordonée de la futur salle
			coordoFuturRoom=calcCoordinates(currentroom,futurRoomID,allRoomsCoordinates)
			#on regarde si les coordonnées de la futur salle ne sont pas déjà les coordonnées d'une autre salle
			for k in allRoomsCoordinates.keys():
				coordo=allRoomsCoordinates[k]
				#si il y a deja une salle a ces coordonnées
				if coordo==coordoFuturRoom:
					working=False
			#on supprime la porte
			currentroom.doors_id[door]=-1
			#si les coordonnées sont libres alors on ajoute la possibilité de porte a la liste des possibilités
			if working:
				res+=[door]
	return res

def ExtendPath(primaryPath,allRoomsCoordinates,player):
	"""Etend le primaryPath avec de nouvelles salles"""
	bossRoomID=len(primaryPath)-1
	idUsable=len(primaryPath)
	extends={}
	for salle in primaryPath.values():
		#on recup les coordonées
		coordo=allRoomsCoordinates[salle.id]
		#on regarde quelles sont les portes fermées
		lsDoorposssibleToOpen=doorsPossibleToOpenWithCoords(salle,idUsable,allRoomsCoordinates)
		#on en choisi 0,1 ou 2 à ouvrir si ce n'est la salle du boss
		if salle.id !=bossRoomID:
			nbdoorsChoosed=random.randint(0,2)
			random.shuffle(lsDoorposssibleToOpen)
			doorsChoosed=lsDoorposssibleToOpen[0:nbdoorsChoosed]
			#on créer une salle après chaque porte choisi
			for door in doorsChoosed:
				salle.doors_id[door]=idUsable
				#on créer la salle
				random_difficulty = random.choices(DIFFICULTIES, weights = DIFFICULTIESWEIGHTS)[0]
				currentroom = Room(player, idUsable, difficulty=random_difficulty,lvl=salle.lvl+1)
				extends[idUsable]=currentroom
				allRoomsCoordinates[idUsable]=calcCoordinates(salle,idUsable,allRoomsCoordinates)
				extends[idUsable].openDoorFromPreviousRoom(salle)
				idUsable+=1

	primaryPath.update(extends)
	for salle in primaryPath.values():
		#on créer les murs et les portes
		salle.walls_creation()
		salle.doors_creation()

	return allRoomsCoordinates

def drawMap(screen,mapdico,allRoomsCoordinates,salleID):
	center=[0,0]
	#point en haut a gauche
	minX=allRoomsCoordinates[0][0]
	maxY=allRoomsCoordinates[0][1]
	#point en bas a droite
	maxX=allRoomsCoordinates[0][0]
	minY=allRoomsCoordinates[0][1]
	for x,y in allRoomsCoordinates.values():
		if x < minX:
			minX=x
		if y >  maxY:
			maxY=y
		if x > maxX:
			maxX=x
		if y < minY:
			minY=y
	
	center[0]=(maxX+minX)//2
	center[1]=-(maxY+minY)//2

	transx=16-center[0]
	transy=8-center[1]

	for roomid in mapdico.keys():
		room=mapdico[roomid]
		if room.visited:
			#draw salle
			x=(allRoomsCoordinates[roomid][0]+transx)*40 # 500 et 300 centre le 0 0 au milieu environ
			y=(-allRoomsCoordinates[roomid][1]+transy)*40
			color=GRAY
			if room.difficulty=="peaceful":
				color=BLUE
			if roomid==salleID:#salle du joueur
				color=GREEN

			pygame.draw.rect(screen, color, (x,y,20,20))
			#draw line 
			#on trouve on on vas
			relationDoors={"top":1,"bottom":-1,"left":-1,"right":1}
			for porte in room.doors_id:
					if room.doors_id[porte]!=-1:
						#on calcul les coordonée de currentroom
						if porte=="top":
							origine=(x+9,y)
							fin=(x+9,y-20)
						elif porte=="bottom":
							origine=(x+9,y+20)
							fin=(x+9,y+40)
						elif porte=="left":
							origine=(x,y+9)
							fin=(x-20,y+9)
						else: #right
							origine=(x+20,y+9)
							fin=(x+40,y+9)
						pygame.draw.line(screen, GRAY, origine, fin, 2)

	

#tests
# path,allRoomsCoordinates=createPrimaryPath(8,player)
# allRoomsCoordinates=ExtendPath(path,allRoomsCoordinates,player)
# affichage des données
# for salle in path.values():
# 	print(salle.id)
# 	print(salle.doors)
