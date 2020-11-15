from Room import *
from random import choices


def createPrimaryPath(n, player):
	allRooms={}
	for i in range(n):
		if i == 0: # Pour la première salle (Tuto)
			currentroom = Room(player, i, difficulty="ultra_easy")
		else:
			random_difficulty = choices(DIFFICULTIES, weights = [20, 1, 4, 50, 20, 5])[0]
			currentroom = Room(player, i, difficulty=random_difficulty)

		#on ouvre sa porte en fonction de la salle précédente
		if i > 0:
			previousRoom=allRooms[i-1]
			currentroom.openDoorFromPreviousRoom(previousRoom)
			currentroom.walls_creation()
			currentroom.doors_creation()

		#on ouvre une nouvelle porte si ce n'est pas la dernière salle
		if i < n-1:
			alea=random.choice(currentroom.doorsPossibleToOpen())
			currentroom.doors_id[alea]=i+1
			currentroom.walls_creation()
			currentroom.doors_creation()

		allRooms[i]=currentroom

	return allRooms
