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
	"pnj-dialogue":"Bonjour, bienvenue sur le tutoriel de LostColor! C'est ici que tu vas apprendre les principale commandes du jeu. Je suis ton instructeur! Tu peux interagir avec moi grâce à la touche espace. Pour te déplacer, utilise les  touches z (haut), q (gauche), s (bas) et d (droite). Cela te permettra d'esquiver les attaques adverses et de mieux te positionner pour attaquer tes ennemis. Attention, si ton clavier est en qwerty, passe-le en azerty. Essaye de te déplacer dans la salle en utilisant ces touches puis passe a la salle suivante.",
	
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
	"pnj-dialogue":"Tu as réussi à trouver votre chemin ? C'est un bon début. Passons au combat. Tu peux viser avec ta souris et tirer avec le clic gauche. Essaie donc sur cet ennemi! ",
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
	"pnj-dialogue":"Comme tu as pu le constater, des tâches de couleur sont apparues sur le sol. Lorsque tu es sur l'une d'elle, tes tirs prennent la même couleur que celle-ci. À quoi cela sert-il? J'y viens. Lorsque tu te trouves sur une tâche rouge, tu fais plus de dégâts à tous les monstres SAUF les monstres rouges que tu ne touches pas. De même pour les autres couleur excepté le blanc, qui représente les monstres de base. Essaie donc!",
	"step":{"action":"spawn","mobspeed":0,"number":5,"pos":[(400,100),(500,100),(600,100),(700,100),(800,100)],"color":[GRAY,GREEN,BLUE,RED,GRAY]}
},
{
	"difficulty":"peaceful",
	"showBackground":False,
	"showHealSkill":True,
	"lvl":1,
	"allowWhiteMobSpawn":False,
	"lootEnable":False,
	"pnj-name":"HuSiRo",
	"pnj-dialogue":"Un monstre viendra plus vite vers toi et te fera deux fois plus de dégâts si tu es sur une tâche de la même couleur que lui. Au bout d'un moment, tu auras besoin de te soigner pour ne pas mourir. Pour te soigner en combat, utilise la touche 'e' pour consommer de la nourriture de ton inventaire. Hors combat tu peux utiliser la nourriture depuis l'inventaire avec le clic droit. Pour ouvrir l'inventaire, utilise la touche 'i'. Enfin, tu peux voir la carte avec la touche 'tab'. Essaye donc ces fonctionnalitées pour t'y familiariser.",
	"step":{"action":"dmg-inv-map","keys":["e","i","tab"]}
}

]


NOMSITEMS = {
	"belt_commun" : ["Ceinture usagée", "Ceinture de voyage", "Vieille ceinture"],
	"belt_rare" : ["Ceinture d'aventurier", "Ceinture en peau de gobelin", "Ceinture ornée"],
	"belt_mythique" : ["Ceinture de paladin", "Ceinture en peau de troll"],
	"belt_légendaire" : ["Ceinture de héros", "Ceinture d'écailles de dragon", "Ceinture d'invincibilité"],
	"chest_commun" : ["Armure de peau", "Tenue de voyage"],
	"chest_rare" : ["Tenue d'aventurier", "Armure en peau de gobelin", "Armure tenace"],
	"chest_mythique" : ["Armure de paladin", "Armure en peau de troll", "Armure résistante"],
	"chest_légendaire" : ["Armure de héros", "Armure d'écailles de dragon", "Armure de protection ultime"],
	"boot_commun" : ["Bottes usagées", "Bottes de voyage", "Vieilles bottes"],
	"boot_rare" : ["Bottes d'aventurier", "Bottes en peau de gobelin", "Bottes de vélocité"],
	"boot_mythique" : ["Soleret de paladin", "Bottes en peau de troll", "Bottes de géant"],
	"boot_légendaire" : ["Soleret de héros", "Bottes d'écailles de dragon", "Bottes de Sept-Lieues"],
	"head_commun" : ["Casque usagé", "Chapeau de voyage", "Vieux casque"],
	"head_rare" : ["Casque d'aventurier", "Casque en peau de gobelin", "Casque solide"],
	"head_mythique" : ["Casque de paladin", "Casque en peau de troll", "Casque résistant"],
	"head_légendaire" : ["Casque de héros", "Casque d'écailles de dragon", "Casque de protection ultime"],
	"glove_commun" : ["Gants usagés", "Gants de voyage", "Vieux gants"],
	"glove_rare" : ["Gantelets d'aventurier", "Gants en peau de gobelin", "Gants de forgeron"],
	"glove_mythique" : ["Gantelets de paladin", "Gants en peau de troll"],
	"glove_légendaire" : ["Gantelets de héros", "Gants d'écailles de dragon"],
	"earrings_commun" : ["Boucles d'oreilles tordues"],
	"earrings_rare" : ["Boucles d'oereilles de qualité"],
	"earrings_mythique" : ["Boucles d'oreilles de magnificence"],
	"earrings_légendaire" : ["Boucles d'oreilles illustres"],
	"wand_commun" : ["Baguette d'apprenti", "Baguette de roturier", "Baguette abimée"],
	"wand_rare" : ["Baguette de mage", "Baguette magique"],
	"wand_mythique" : ["Baguette de maître", "Baguette de renom"],
	"wand_légendaire" : ["Baguette d'archimage", "Baguette d'immortel"],
	"staff_rare" : ["Bâton de magicien"]
	
}

DESCRIPTIONSITEMS = {
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
	"head_mythique" : ["Porter ce casque vous remplit de détermination"],
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

NOMSFOOD = {
	"beer" : ["Bière", "Cervoise de qualité"],
	"cake" : ["Gâteau", "Tarte"],
	"fish" : ["Poisson", "Poisson pêché"],
	"meal" : ["Repas", "Casse-croûte"],
	"meat" : ["Viande", "Morceau de viande rouge"],
	"noodles" : ["Nouilles", "Plat de nouilles", "Plat de pâtes"],
	"onigiri" : ["Riz", "Boulette de riz"],
	"pizza" : ["Pizza", "Morceau de pizza"],
	"steak" : ["Steak", "Côtelette d'agneau"],
	"strawberry" : ["Fraise" "Fruit rouge"],
	"tomato" : ["Tomate", "Tomate de potager"],
	"whiskey" : ["Whiskey", "Alcool de qualité"]
	
}

DESCRIPTIONSFOOD = {
	"beer" : ["Une curieuse boisson importée par les nains"],
	"cake" : ["Un gâteau appétissant"],
	"fish" : ["Frais de ce matin"],
	"meal" : ["Parfaitement équilibré pour une aventure!"],
	"meat" : ["Le regarder vous fait saliver"],
	"noodles" : ["Son odeur vous fait chavirer"],
	"onigiri" : ["Une simple boulette de riz"],
	"pizza" : ["Le fromage en coule encore"],
	"steak" : ["Un fumet ravissant"],
	"strawberry" : ["Une denrée rare dans ces régions"],
	"tomato" : ["Pour respecter les 5 fruits et légumes par jour"],
	"whiskey" : ["Celui-ci a été conservé pendant 30 ans"]
		    
}

NOMSPLANTES = {
	"2" : ["Blé"],
	"3" : ["Houx"],
	"6" : ["Paille"],
	"7" : ["Baie violette"],
	"8" : ["Baie pâle"],
	"9" : ["Baie orange"],
	"10" : ["Noix"],
	"12": ["Carotte"],
	"16" : ["Trèfle commun"],
	"19" : ["Baie rouge"],
	"20" : ["Champignons noirâtres"],
	"21" : ["Samare d'érable"],
	"23": ["Champignons blancs"],
	"32" : ["Grappe de baies bleuâtres"],
	"33" : ["Haricot"],
	"35" : ["Graines"],
	"40" : ["Branche tordue"],
	"44" : ["Champignons grisâtres"],
	"46" : ["Chataîgne"],
	"47" : ["Champignons luisants"],

}

DESCRIPTIONSPLANTES = {
	"2" : ["De simples céréales"],
	"3" : ["Une feuille de houx"],
	"6" : ["Une touffe de paille"],
	"7" : ["Une baie qui ne vous inspire guère confiance"],
	"8" : ["Des baies utilisées comme somnifère"],
	"9" : ["Une baie comestibles et succulentes"],
	"10" : ["Leur poudre peut servir à concocter des solutions"],
	"12" : ["Un légume basique"],
	"16" : ["Certains spécimens très rares portent chance"],
	"19" : ["Des baies toxiques"],
	"20" : ["Des champignons non comestibles mais qui possèdent de sombres propriétés..."],
	"21" : ["Une graine qui tournicote lors de sa chute"],
	"23" : ["Ces champignons ont l'air succulents"],
	"32" : ["Ces baies dégagent une odeur pestilentielle"],
	"33" : ["Un haricot rempli de petits pois"],
	"35" : ["Des graines de haricots"],
	"40" : ["La forme étrange de cette branche vous fait penser qu'elle a été ensorcelée"],
	"44" : ["De succulents champignons"],
	"46" : ["Une chataîgne encore intacte"],
	"47" : ["Des champignons d'aspect peu commun aux propriétés magiques"]

}
	
	

NOMSDIVERS = {
	"ambre" : ["Ambre"],
	"diamond" : ["Diamant"],
	"emerauld" : ["Émeraude"],
	"leather" : ["Cuir"],
	"metal" : ["Métal"],
	"plank" : ["Planche"],
	"rubis" : ["Rubis"],
	"stone" : ["Pierre"],
	"wood" : ["Bois"]

}

DESCRIPTIONSDIVERS = { 
	"ambre" : ["Une gemme opaque de couleur jaune-marron"],
	"diamond" : ["Une pierre précieuse, brillante et extrêmement dure"],
	"emerauld" : ["Une gemme minérale de couleur verte"],
	"leather" : ["Une simple peau d'animal tannée"],
	"metal" : ["Un pur lingot de métal"],
	"plank" : ["Une fine planche de bois"],
	"rubis" : ["Un pierre couleur sang"],
	"stone" : ["De la pierre brute"],
	"wood" : ["Des rondins de bois"]
	
}

DIALOGUESMARCHAND = {
	"présentation" : ["Bonjour", "Beau temps pour faire des affaires non?", "Je vous ai manqué?", "Cela fait bien longtemps... au moins trente secondes!", "Êtes-vous prêts à marchander?"],
	"acheter" : ["J'ai quelques nouveautés dont vous me direz des nouvelles.", "J'ai refait mes stocks derièrement, regardez donc.", "Qu'est-ce qui vous intéresserait cette fois-ci?", "Jetez un coup d'oeil", "Peut-être trouverez-vous votre bohneur cette fois-ci", "Vous aurez bien besoin d'un petit remontant?"],
	"vendre" : ["Que m'apportez-vous cette fois-ci?", "Montrez-moi ce que vous voulez vendre.", "Un peu de commerce ne fait jamais de mal", "Dites toujours", "Oh ho! Quels nouveaux joyaux m'apportez-vous?", "Ça tombe bien, j'avais envie de faire des emplettes aujourd'hui."],
	"quitter" : ["À une prochaine fois! Enfin, je l'espère...", "Faites bien attention à vous.", "Les environs sont dangereux ces temps-ci, soyez prudent", "Puissent nos chemins de nouveau se croiser!", "Bonne chance."]
	
}

		  
		       
	
	
	
	
	
	
