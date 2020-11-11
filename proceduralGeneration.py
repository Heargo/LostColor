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
	for i in range(n):
		#on init la salle
		currentroom=Room(i)
		#on ouvre sa porte en fonction de la salle précédente
		if i >0:
			previousRoom=allRooms[i-1]
			currentroom.openDoorFromPreviousRoom(previousRoom)

		#on ouvre une nouvelle porte si ce n'est pas la dernière salle
		if i < n-1:
			alea=random.choice(currentroom.doorsPossibleToOpen())
			currentroom.doors[alea]=i+1

		allRooms[i]=currentroom

	return allRooms


primaryPath=createPrimaryPath(4)
for i in primaryPath:
	print(primaryPath[i].id)
	print(primaryPath[i].doors)
	print("-----------------")