FPS = 60
#Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127, 127)
BROWN = (58, 29, 0)
RED2 = (225, 40, 30)
GREEN2 = (40, 215, 50)
BLUE2 = (40, 30, 215)


#couleurs des taches et des monstres
COLORS=[RED,GREEN,BLUE]

#taille de l'écran
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


#constants stats joueur
PLAYER_HP = 100
PLAYER_DMG = 12
PLAYER_TPS = 2
PLAYER_SHOOT_SPEED = 8
PLAYER_SPEED = 6
HEAL_COOLDOWN = 5

MONSTER_LEVEL_MAX=100

# Taille des portes et murs du jeu
wall_size = 20
door_length = 100

# Type de bonus :
BONUS_TYPE = ("dmg", "tps", "heal", "hp_max", "shot_speed", "speed")

# Liste des difficultés
DIFFICULTIES = ["peaceful", "ultra_easy", "easy", "medium", "hard", "ultra_hard"]
DIFFICULTIESWEIGHTS=[10,8,6,4,1,1]

#relation couleur/grade
COLOR_OF_GRADE={"commun":(176, 176, 176),"rare":(123, 212, 220),"mythique":(136, 77, 155),"légendaire":(230, 185, 45)}
GRADES=["commun","rare","mythique","légendaire"]
STATS_MAX_COMMUN={"dmg":50, "tps":6, "hp":500, "shot_speed":10, "speed":6.5}
STATS_MAX={"dmg":100, "tps":60, "hp":1000, "shot_speed":20, "speed":8}
STATS_GRADE_DATA={"dmg":{"commun":50,"rare":65,"mythique":80,"légendaire":STATS_MAX["dmg"]},
				  "tps":{"commun":7,"rare":20,"mythique":40,"légendaire":STATS_MAX["tps"]},
				  "hp":{"commun":500,"rare":600,"mythique":800,"légendaire":STATS_MAX["hp"]},
				  "shot_speed":{"commun":10,"rare":13,"mythique":16,"légendaire":STATS_MAX["shot_speed"]},
				  "speed":{"commun":6.5,"rare":6.9,"mythique":7.5,"légendaire":STATS_MAX["speed"]}
				  }
# Liste des pnjs
PNJS = ["instructor", "merchant"]