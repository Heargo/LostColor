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


TUTORIAL_DATA=[

{
	"difficulty":"peaceful",
	"showBackground":False,
	"showHealSkill":False,
	"lvl":1,
	"allowWhiteMobSpawn":False,
	"lootEnable":False,
	"pnj-name":"HuSiRo",
	"pnj-dialogue":"Bonjour, bienvenu(e) sur le Tutoriel de LostColor ! Je suis votre instructeur ici ! vous pouvez vous deplacer avec les  touches z q s d. Attention, si votre clavier est en qwerty, passez le en azerty. Essayez de vous deplacer dans la salle en utilisant ces touches puis passez a la salle suivante. Vous pouvez interragir avec moi avec [barre espace]",
	
	"step":{"action":"key","keys":["z","q","s","d"]}
},
{
	"difficulty":"peaceful",
	"showBackground":False,
	"showHealSkill":False,
	"lvl":1,
	"allowWhiteMobSpawn":False,
	"lootEnable":False,
	"pnj-name":"HuSiRo",
	"pnj-dialogue":"Vous avez pu trouver votre chemin ? Bien... Préparez vous à tuer un monstre. Vous pouvez visez avec le curseur de votre souris. utilisez le clique gauche pour tirer. ",
	"step":{"action":"spawn","mobspeed":0,"number":1,"pos":[(600,100)],"color":[GRAY]}
}
,
{
	"difficulty":"peaceful",
	"showBackground":True,
	"showHealSkill":False,
	"lvl":1,
	"allowWhiteMobSpawn":False,
	"lootEnable":False,
	"pnj-name":"HuSiRo",
	"pnj-dialogue":"Comme vous avez pu le constater, des taches de couleurs sont apparues sur le sol. Lorsque vous vous trouvez sur une couleur, vos tir prennent la même couleur. Quel interet me direz vous ? Lorsque vous êtes sur une tache rouges, vous faites plus de dégâts à tous les monstres SAUF que vous ne pouvez pas attaquer les monstres rouges. De même pour les autres couleurs sauf le blanc. Je vous laisse essayer...",
	"step":{"action":"spawn","mobspeed":0,"number":5,"pos":[(400,100),(500,100),(600,100),(700,100),(800,100)],"color":[GRAY,GREEN,BLUE,RED,GRAY]}
},
{
	"difficulty":"peaceful",
	"showBackground":False,
	"showHealSkill":False,
	"lvl":1,
	"allowWhiteMobSpawn":False,
	"lootEnable":False,
	"pnj-name":"HuSiRo",
	"pnj-dialogue":"Venons en maintenant aux dégats... Un monstre viendra plus vite vers vous et vous fera le double de dégats si vous vous tenez sur la même couleur que lui. Au bout d'un moment vous aurez besoin de vous soigner pour ne pas mourrir. Pour vous soigner en combat, il suffit d'utiliser la touche 'e'. Si vous avez de la nourriture dans votre inventaire elle sera automatiquement consommée. Hors combat vous pouvez utiliser la nourriture directement dans l'inventaire avec le clique droit. Pour ouvrir l'inventaire vous pouvez utiliser la touche 'i'. Enfin vous pouvez voir la carte avec la touche 'tab'. Essayez donc ces fonctionnalitées.",
	"step":{"action":"dmg-inv-map","keys":["e","i","tab"]}
}

]


NOMSITEMS = {
	"belt_commun" : ["Ceinture usagée", "Ceinture de voyage"],
	"belt_rare" : ["Ceinture d'aventurier", "Ceinture en peau de gobelin"],
	"belt_mythique" : ["Ceinture de paladin", "Ceinture en peau de troll"],
	"belt_légendaire" : ["Ceinture de héros", "Ceinture d'écailles de dragon"],
	"chest_commun" : ["Armure de peau", "Tenue de voyage"],
	"chest_rare" : ["Tenue d'aventurier", "Armure en peau de gobelin"],
	"chest_mythique" : ["Armure de paladin", "Armure en peau de troll"],
	"chest_légendaire" : ["Armure de héros", "Armure d'écailles de dragon"],
	"boot_commun" : ["Bottes usagées", "Bottes de voyage"],
	"boot_rare" : ["Bottes d'aventurier", "Bottes en peau de gobelin"],
	"boot_mythique" : ["Soleret de paladin", "Bottes en peau de troll"],
	"boot_légendaire" : ["Soleret de héros", "Bottes d'écailles de dragon"],
	"head_commun" : ["Casque usagé", "Chapeau de voyage"],
	"head_rare" : ["Casque d'aventurier", "Casque en peau de gobelin"],
	"head_mythique" : ["Casque de paladin", "Casque en peau de troll"],
	"head_légendaire" : ["Casque de héros", "Casque d'écailles de dragon"],
	"glove_commun" : ["Gants usagés", "Gants de voyage"],
	"glove_rare" : ["Gantelets d'aventurier", "Gants en peau de gobelin"],
	"glove_mythique" : ["Gantelets de paladin", "Gants en peau de troll"],
	"glove_légendaire" : ["Gantelets de héros", "Gants d'écailles de dragon"],
	"earrings_commun" : ["Boucles d'oreilles tordues"],
	"earrings_rare" : ["Boucles d'oereilles de qualité"],
	"earrings_mythique" : ["Boucles d'oreilles de magnificence"],
	"earrings_légendaire" : ["Boucles d'oreilles illustres"],
	"wand_commun" : ["Baguette d'apprenti", "Baguette de roturier"],
	"wand_rare" : ["Baguette de mage", "Baguette magique"],
	"wand_mythique" : ["Baguette de maître", "Baguette de renom"],
	"wand_légendaire" : ["Baguette d'archimage"],
	"staff_rare" : ["Bâton de magicien"]
	
}

DESCRIPTIONS = {
	"belt_commun" : ["Une ceinture simple", "Une ceinture abimée par le temps"],
	"belt_rare" : ["Une ceinture solide", "Porter cette ceinture vous fait vous sentir un peu plus fort"],
	"belt_mythique" : ["Porter cette ceinture vous remplit de détermination"],
	"belt_légendaire" : ["La simple vue de cette ceinture vous remplit de courage", "Cette ceinture fait jaillir en vous une force inconnue"],
	"chest_commun" : ["Une tenue simple", "Une tenue abimée par le temps"],
	"chest_rare" : ["Une armure solide", "Porter cette armure vous fait vous sentir un peu plus fort"],
	"chest_mythique" : ["Porter cette armure vous remplit de détermination"],
	"chest_légendaire" : ["La simple vue de cette armure vous remplit de courage", "Cette armure fait jaillir en vous une force inconnue"],
	"boot_commun" : ["De simples bottes", "Des bottes abimées par le temps"],
	"boot_rare" : ["Des bottes robustes", "Porter ces bottes vous fait vous sentir un peu plus fort"],
	"boot_mythique" : ["Porter ces bottes vous remplit de détermination"],
	"boot_légendaire" : ["La simple vue de ces bottes vous remplit de courage", "Ces bottes font jaillir en vous une force inconnue"],
	"head_commun" : ["Un casque simple", "Un casque abimé par le temps"],
	"head_rare" : ["Un casque solide", "Porter ce casque vous fait vous sentir un peu plus fort"],
	"head_mythique" : ["casque de paladin", "casque en peau de troll"],
	"head_légendaire" : ["La simple vue de ce casque vous remplit de courage", "Ce casque fait jaillir en vous une force inconnue"],
	"glove_commun" : ["Des gants simples", "Des gants abimés par le temps"],
	"glove_rare" : ["Des gants robustes", "Porter ces gants vous fait vous sentir un peu plus fort"],
	"glove_mythique" : ["Porter ces gants vous remplit de détermination"],
	"glove_légendaire" : ["La simple vue de ces gants vous remplit de courage", "Ces gants font jaillir en vous une force inconnue"],
	"earrings_commun" : ["De la joaillerie de bas étage"],
	"earrings_rare" : ["Une perle de joaillier"],
	"earrings_mythique" : ["Ces boucles d'oreilles semblent être tirées d'un rêve"],
	"earrings_légendaire" : ["Ces fabuleuses boucles d'oreilles sont réputées pour leur beauté"],
	"wand_commun" : ["Un simple bout de bois"],
	"wand_rare" : ["Vous sentez de la magie pure émanant de cette baguette"],
	"wand_mythique" : ["Vous savez que la baguette que vous tenez s'est fait un nom dans l'histoire de la magie"],
	"wand_légendaire" : ["Cette baguette a déjà accompli de nombreux exploits"],
	"staff_rare" : ["Vous sentez de la magie pure émanant de ce bâton orné"]

		       
}
	
		  
		       
	
	
	
	
	
	
