import random

class Room():
	"""docstring for room"""
	def __init__(self, id, top=-1, bottom=-1, left=-1, right=-1, difficulty="none"):
		self.id = id
		self.doors={"top":top,"bottom":bottom,"left":left,"right":right}
		self.difficulty=difficulty


	def doorsPossibleToOpen(self):
		lsDoors=[]
		for k in self.doors.keys():
			if self.doors[k]==-1:
				lsDoors+=[k]
		return lsDoors


	def openDoorFromPreviousRoom(self,previousRoom):
		res="none"
		for k in previousRoom.doors:
			if previousRoom.doors[k]==self.id:
				res=k
		relationDoors={"top":"bottom","bottom":"top","left":"right","right":"left"}
		self.doors[relationDoors[res]]=previousRoom.id




def createPrimaryPath(n):
	allRooms={}
	allRoomsCoordinates={}
	for i in range(n):
		#on init la salle
		currentroom=Room(i)
		coordo=[0,0]
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
				alea=random.choice(doorsPossible)
			currentroom.doors[alea]=i+1
		allRooms[i]=currentroom
	return allRooms,allRoomsCoordinates


def calcCoordinates(previousRoom,currentroomID,allRoomsCoordinates):
	#on trouve depuis on on vient
	for k in previousRoom.doors:
			if previousRoom.doors[k]==currentroomID:
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
	for door in currentroom.doors:
		#si la porte n'existe pas 
		if currentroom.doors[door]==-1:
			working=True
			#on créer une porte vers l'emplacement de la futur salle
			currentroom.doors[door]=futurRoomID
			#on calcul les coordonée de la futur salle
			coordoFuturRoom=calcCoordinates(currentroom,futurRoomID,allRoomsCoordinates)
			#on regarde si les coordonnées de la futur salle ne sont pas déjà les coordonnées d'une autre salle
			for k in allRoomsCoordinates.keys():
				coordo=allRoomsCoordinates[k]
				#si il y a deja une salle a ces coordonnées
				if coordo==coordoFuturRoom:
					working=False
					#on supprime la porte
			currentroom.doors[door]=-1
			#si les coordonnées sont libres alors on ajoute la possibilité de porte a la liste des possibilités
			if working:
				res+=[door]
	return res

def ExtendPath(primaryPath,allRoomsCoordinates):
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
				salle.doors[door]=idUsable
				extends[idUsable]=Room(idUsable)
				extends[idUsable].openDoorFromPreviousRoom(salle)
				idUsable+=1

	primaryPath.update(extends)

#tests
path,allRoomsCoordinates=createPrimaryPath(8)
ExtendPath(path,allRoomsCoordinates)
#affichage des données
# for salle in path.values():
# 	print(salle.id)
# 	print(salle.doors)
