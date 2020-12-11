from menu import *
from constants import *
from Bullet import *
from Ennemis import *
from Bonus import *
from player import *
from Room import *
import random
from math import sqrt
from proceduralGeneration import *
from inventaire import invetoryScreen, Item
from Dialog_Box import *
from time import time

def initPartie(tutorial=False):
    """Initialise une partie"""
    global player,current_room,floor, allRoomsCoordinates


    if not tutorial:
        # Création du joueur
        player.initStats()
        player.inventaire.items=[False]*player.inventaire.size
        player.updateStats()
    
    player.rect.centerx = 2 * SCREEN_WIDTH // 3
    player.rect.centery = 2 * SCREEN_HEIGHT // 3

    # Création des salles
    if not tutorial:
        floor,allRoomsCoordinates = createPrimaryPath(10, player)
        allRoomsCoordinates=ExtendPath(floor,allRoomsCoordinates,player)
    else:
        floor,allRoomsCoordinates = createTutorialWithError(player)

    # Salle courante (ou est le joueur est)
    current_room = floor[player.current_room_id]
    #on reset les sprites
    loots_list = pygame.sprite.Group()
    # Ajout des sprite dans l'ordre d'affichage dans le Group all_sprites_list
    all_sprites_list.empty()
    current_room.enemy_list.empty()
    all_sprites_list.add(loots_list)
    all_sprites_list.add(current_room.enemy_list)
    all_sprites_list.add(current_room.pnj_list)
    all_sprites_list.add(bullet_list)
    all_sprites_list.add(player)



def initSprites():
    global all_sprites_list,enemy_list,bullet_list,loots_list,player,current_room_no,current_room,floor, allRoomsCoordinates
    # --- Listes de Sprites
    # Ceci est la liste de tous les sprites. Tous les ennemis et le joueur aussi.
    # Un groupe de sprite LayeredUpdates possede en plus un ordre (pour l'affichage)
    all_sprites_list = pygame.sprite.LayeredUpdates()


    # Liste des balles
    bullet_list = pygame.sprite.Group()

    
    # --- Creation des Sprites
    # Création du joueur
    player = Player("Test", 0, 0)

    player.rect.centerx = 2 * SCREEN_WIDTH // 3
    player.rect.centery = 2 * SCREEN_HEIGHT // 3

    # Création des salles
    floor,allRoomsCoordinates = createPrimaryPath(10, player)
    allRoomsCoordinates=ExtendPath(floor,allRoomsCoordinates,player)

    # Salle courante (ou est le joueur est)
    current_room = floor[player.current_room_id]
    #liste des loots
    loots_list = pygame.sprite.Group()
    # Ajout des sprite dans l'ordre d'affichage dans le Group all_sprites_list
    all_sprites_list.add(loots_list)
    all_sprites_list.add(current_room.enemy_list)
    all_sprites_list.add(current_room.pnj_list)
    all_sprites_list.add(bullet_list)
    all_sprites_list.add(player)



def draw_text(screen,text, font_name, size, color, x, y, center):
    """"""
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.centerx = x
        text_rect.centery = y
    else:
        text_rect.x = x
        text_rect.y = y

    screen.blit(text_surface, text_rect)

def draw_HUD(screen):
    """Head up display : affichage d'information pour le joueur"""

    # Affichage PV
    draw_text(screen, "PV : " + str(player.HP) + "/" + str(player.HP_MAX), 'fonts/RPGSystem.ttf', 20, BLACK, 25, SCREEN_HEIGHT//2+20, False)

    # Affichage DMG
    draw_text(screen, "DMG : " + str(player.DMG), 'fonts/RPGSystem.ttf', 20, BLACK, 25, SCREEN_HEIGHT // 2, False)

    # Affichage TPS
    draw_text(screen, "TPS : " + str(player.tps), 'fonts/RPGSystem.ttf', 20, BLACK, 25, SCREEN_HEIGHT // 2 - 20, False)

    # Affichage SPEED
    draw_text(screen, "SPEED : " + str(player.speed), 'fonts/RPGSystem.ttf', 20, BLACK, 25, SCREEN_HEIGHT // 2 - 40, False)

    # Affichage SPEED
    draw_text(screen, "SHOT SPEED : " + str(player.shot_speed), 'fonts/RPGSystem.ttf', 20, BLACK, 25, SCREEN_HEIGHT // 2 - 60, False)


def setNewPolygones():
    res=[]
    for p in polygones_list:
        randomX= randint(0,SCREEN_WIDTH)
        randomY = randint(0,SCREEN_HEIGHT)
        newp=[]
        for point in p:
            newp+=[((randomX+point[0])/2,(randomY+point[1])/2)]
        res+=[[newp,random.choice(COLORS)]]

    return res

def drawPolygones(screen,poly_list):
    for p in poly_list:
        pygame.draw.polygon(screen, p[1], p[0],0)


def main_menu(screen,fpsClock):
    running = True
    click = False
    #créer les boutons
    b1 = Bouton(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, 'Jouer', RED)
    b2 = Bouton(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 'Tutoriel', GREEN)
    b3 = Bouton(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, 'Credit', BLUE)
    b4 = Bouton(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200, 'Quitter', GRAY)

    while running:
        #fermeture de la fenetre
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #clic de la souris
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        #on recupère les coordonnées de la souris
        mx, my = pygame.mouse.get_pos()

        #Si l'utilisateur clique sur un bouton, on lance la fonction adaptée
        if b1.hoover(mx, my):
            if click:
                game(screen,fpsClock)
        if b2.hoover(mx, my):
            if click:
                initPartie(True)
                game(screen,fpsClock,True)
        if b3.hoover(mx, my):
            if click:
                pass # credits()
        if b4.hoover(mx, my):
            if click:
                pygame.quit()
                sys.exit()

        #affichage 
        screen.fill((255, 255, 255))
        #affiche le nom du jeu
        draw_text(screen,'Lost color', 'fonts/No_Color.ttf', 60, BLACK, SCREEN_WIDTH // 2, 100, True)
        #affiche les boutons
        b1.draw(screen, mx, my)
        b2.draw(screen, mx, my)
        b3.draw(screen, mx, my)
        b4.draw(screen, mx, my)
        #on passe click a false pour pas que le jeu considère que l'utilisateur clique sans arrêt.
        click = False

        pygame.display.update()
        fpsClock.tick(FPS)



def game(screen,fpsClock,tutorial=False):
    global current_room
    playing = True
    mapOn=False
    white_mob_spawn_delay = 0
    loots_list=current_room.loots
    actions={"i":False,"tab":False,"z":False,"q":False,"s":False,"d":False,"f":False,"e":False,"kill":False}
    firstDialogueBoxDone=False
    if tutorial:
        tutorialCompleted=False
    else:
        tutorialCompleted=True   
   
    while playing:
        click=False
        current_room.visited=True
        # --- Gestion des Event
        for event in pygame.event.get():

            # close game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #click sur le bouton lors de la mort du joueur
            if event.type == MOUSEBUTTONDOWN and player.HP <=0:
                    if event.button == 1:
                        click = True
            # Detection d'utilisation du clavier pour faire spawner 3 monstres
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for pnj in current_room.pnj_list:
                        if pygame.sprite.collide_rect(pnj, player):
                            dialog_loop(tutorial,False,pnj, screen, fpsClock)
                if event.key == pygame.K_KP8:
                   current_room.spawnMonsters("exact_number", player, 3)
                   all_sprites_list.add(current_room.enemy_list)
                if event.key == pygame.K_KP9:
                   print(all_sprites_list)
                if event.key == pygame.K_KP1:
                    bonus_test = Bonus("dmg", player)
                    all_sprites_list.add(bonus_test)
                if event.key == pygame.K_KP2:
                    bonus_test = Bonus("tps", player)
                    all_sprites_list.add(bonus_test)
                if event.key == pygame.K_KP3:
                    bonus_test = Bonus("shot_speed", player)
                    all_sprites_list.add(bonus_test)
                if event.key == pygame.K_KP4:
                    bonus_test = Bonus("heal", player)
                    all_sprites_list.add(bonus_test)
                if event.key == pygame.K_KP5:
                    bonus_test = Bonus("hp_max", player)
                    all_sprites_list.add(bonus_test)
                if event.key == pygame.K_KP6:
                    bonus_test = Bonus("speed", player)
                    all_sprites_list.add(bonus_test)
                if event.key == K_ESCAPE:
                    playing = False
                if event.key == K_TAB and len(current_room.enemy_list) == 0:
                    mapOn=True
                    if tutorial:
                        actions["tab"]=True
                if event.key == K_i and len(current_room.enemy_list) == 0:
                    if tutorial:
                        actions["i"]=True
                    invetoryScreen(screen,fpsClock,player.inventaire,player)
                    player.updateStats()
                if event.key == K_f:
                    checkRecupLoot(all_sprites_list,loots_list,player)
                if event.key == K_e:
                    healSkill(player)
                    if tutorial:
                        actions["e"]=True


        if not mapOn and player.HP >0:
            # Detection d'utilisation du clavier pour déplacer le joueur:
            activeKey = pygame.key.get_pressed()

            if activeKey[K_a]:  # left
                player.move("LEFT", current_room.wall_list)
                if tutorial:
                    actions["q"]=True
            if activeKey[K_d]:  # right
                player.move("RIGHT", current_room.wall_list)
                if tutorial:
                    actions["d"]=True
            if activeKey[K_w]:  # top
                player.move("UP", current_room.wall_list)
                if tutorial:
                    actions["z"]=True
            if activeKey[K_s]:  # bottom
                player.move("DOWN", current_room.wall_list)
                if tutorial:
                    actions["s"]=True

            # on change la couleur du joueur en fonction de la position
            if not tutorial:
                setColorPlayerFromPosition(current_room.taches, player)
            else:
                if TUTORIAL_DATA[current_room.id]["showBackground"]:
                    setColorPlayerFromPosition(current_room.taches, player)
            




            # Si la salle contient des monstres de couleurs et que le delai d'aparition est bon on fait aparaitre
            # un monstre blanc
            if not tutorial :
                if white_mob_spawn_delay >= 120:
                    manageWhiteMobs(current_room.enemy_list, current_room, player)
                    all_sprites_list.add(current_room.enemy_list)
                    white_mob_spawn_delay = 0
            elif TUTORIAL_DATA[current_room.id]["allowWhiteMobSpawn"]:
                if white_mob_spawn_delay >= 120:
                    manageWhiteMobs(current_room.enemy_list, current_room, player)
                    all_sprites_list.add(current_room.enemy_list)
                    white_mob_spawn_delay = 0

            # on met a jour les stats des monstres en fonction de la couleur du joueur
            if not tutorial:
                updateMobsStats(current_room.enemy_list, player.colorbuff)


            # Detection de la souris et du cooldown pour tirer
            activeMouse = pygame.mouse.get_pressed()
            if activeMouse[0] == True:
                if player.cooldown >= player.cooldown_max:
                    # position de la souris
                    pos = pygame.mouse.get_pos()

                    mouse_x = pos[0]
                    mouse_y = pos[1]

                    # Créé la balle
                    bullet = Bullet(player, mouse_x, mouse_y, player.colorbuff)

                    # et l'ajoute a la liste des balles
                    bullet_list.add(bullet)
                    all_sprites_list.add(bullet)
                    # Remise à 0 du temps de rechargement de tire
                    player.cooldown = 0

            # --- Logique du jeu
            # Bonus a la fin des salles
            if len(current_room.enemy_list) == 0 and (not current_room.bonus.taken)  and current_room.difficulty!="peaceful":
                all_sprites_list.add(current_room.bonus)

            # Gestions du changement de salle
            if player.rect.x < -player.rect.width:  # Le joueur va à gauche
                player.current_room_id = current_room.doors_id["left"]
                loots_list = current_room.loots
                all_sprites_list.empty()  # Détruit les sprite de la salle avant de changer de salle
                all_sprites_list.add(player)  # Remet le joueur dans all_sprites_list our l'afficher dans la prochaine salle
                current_room = floor[player.current_room_id]
                player.rect.x = SCREEN_WIDTH - player.rect.width - wall_size
                loots_list = current_room.loots 
                all_sprites_list.add(loots_list)
                all_sprites_list.add(current_room.enemy_list)
                print(current_room.difficulty,current_room.lvl)


            if player.rect.x > SCREEN_WIDTH:  # Le joueur va à droite
                player.current_room_id = current_room.doors_id["right"]
                all_sprites_list.empty()  # Détruit les sprite de la salle avant de changer de salle
                all_sprites_list.add(player)  # Remet le joueur dans all_sprites_list our l'afficher dans la prochaine salle
                current_room = floor[player.current_room_id]
                player.rect.x = player.rect.width + wall_size
                loots_list = current_room.loots 
                all_sprites_list.add(loots_list)
                all_sprites_list.add(current_room.enemy_list)
                print(current_room.difficulty,current_room.lvl)

            if player.rect.y < -player.rect.height:  # Le joueur va en haut
                player.current_room_id = current_room.doors_id["top"]
                all_sprites_list.empty()  # Détruit les sprite de la salle avant de changer de salle
                all_sprites_list.add(player)  # Remet le joueur dans all_sprites_list our l'afficher dans la prochaine salle
                current_room = floor[player.current_room_id]
                player.rect.y = SCREEN_HEIGHT - player.rect.height - wall_size
                loots_list = current_room.loots 
                all_sprites_list.add(loots_list)
                all_sprites_list.add(current_room.enemy_list)
                print(current_room.difficulty,current_room.lvl)

            if player.rect.y > SCREEN_HEIGHT:  # Le joueur va en bas
                player.current_room_id = current_room.doors_id["bottom"]
                all_sprites_list.empty()  # Détruit les sprite de la salle avant de changer de salle
                all_sprites_list.add(player)  # Remet le joueur dans all_sprites_list our l'afficher dans la prochaine salle
                current_room = floor[player.current_room_id]
                player.rect.y = player.rect.height + wall_size
                loots_list = current_room.loots 
                all_sprites_list.add(loots_list)
                all_sprites_list.add(current_room.enemy_list)
                print(current_room.difficulty,current_room.lvl)

            # Gestions des balles
            for bullet in bullet_list:

                # Si une balle touche un monstre
                enemy_hit_list = pygame.sprite.spritecollide(bullet, current_room.enemy_list, False)

                # Pour chaque monstre touché, on supprime la balle et on fait perdre de la vie au monstre en fonction de la couleur de la balle
                for mob in enemy_hit_list:
                    dmgDone=False
                    
                    # Lorsqu'un ennemie se fait toucher il perd les dégats du joueur si il n'est pas de la m
                    if bullet.color==GRAY:
                        mob.HP -= player.DMG*0.5
                        dmgDone=True
                    elif bullet.color!=mob.colorbuff:
                        mob.HP -= player.DMG*1.5
                        dmgDone=True

                    if dmgDone:
                        bullet_list.remove(bullet)
                        all_sprites_list.remove(bullet)
                        if tutorial:
                            actions["kill"] = mob.checkdead(loots_list,all_sprites_list,TUTORIAL_DATA[current_room.id]["lootEnable"])
                        else:
                            mob.checkdead(loots_list,all_sprites_list,True)

                # On supprime la balle de la liste des sprites si elle sort de l'écran
                if bullet.rect.y < -10:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)

            # Colision entre joueur et monstre
            for mob in current_room.enemy_list:
                if pygame.sprite.collide_rect(mob, player) and not player.get_hit:
                    player.get_hit = True
                    player.HP -= mob.DMG

            # Incrementation du delai d'aparition des monstre blanc
            white_mob_spawn_delay += 1

            #si on est dans le tuto, on vérifie l'avancement de l'étape
            if tutorial and not tutorialCompleted:
                actions,tutorialCompleted = checkTutorialStepCompletion(current_room,actions,tutorialCompleted)

            # Appelle la méthode update() de tous les Sprites
            all_sprites_list.update()

            # Méthode update de la salle courante pour la gestion des portes
            current_room.update(tutorialCompleted)
        
            # --- Dessiner la frame
            # Clear the screen
            screen.fill(WHITE)

            

            # Dessine les taches de couleur
            if not tutorial:
                drawAllTaches(screen, current_room.taches)
            else:
                if TUTORIAL_DATA[current_room.id]["showBackground"]:
                    drawAllTaches(screen, current_room.taches) 
            # Dessine tous les sprites (les blits sur screen)
            all_sprites_list.draw(screen)
            #dessine le bouton de skill de heal 
            if not tutorial:
                dessineHealBouton(screen,player)
            else:
                if TUTORIAL_DATA[current_room.id]["showHealSkill"]:
                    dessineHealBouton(screen,player)

            #on met l'affichage de fin de tuto
            if tutorial:
                if tutorialCompleted:
                    draw_text(screen,"Vous avez terminé le tutoriel ! echap pour quitter", 'fonts/No_Color.ttf', 37, BLACK, 650, 100, True)

            # Dessine les murs et portes de la salle courante
            current_room.wall_list.draw(screen)
            current_room.door_list.draw(screen)
            # Dessine les PNJs de la salle courante
            current_room.pnj_list.draw(screen)


            # Affichage HUD
            draw_HUD(screen)

        #si il y a la map
        if mapOn and player.HP >0:
            activeKey = pygame.key.get_pressed()
            if not activeKey[K_TAB]:
                mapOn=False
            # Clear the screen
            screen.fill(WHITE)
            drawMap(screen,floor,allRoomsCoordinates,current_room.id)

        #si le jouer est mort
        if player.HP <=0:
            #créer le bouton de restart
            replay_bouton = Bouton(SCREEN_WIDTH // 2, 400, 'RESTART', RED)               
            #on recupère les coordonnées de la souris
            mx, my = pygame.mouse.get_pos()

            #Si l'utilisateur clique sur le bouton, on retourne au menu
            if replay_bouton.hoover(mx, my):
                if click:
                    all_sprites_list.empty()  # Détruit les sprite de la salle avant de changer de salle
                    all_sprites_list.add(player)  # Remet le joueur dans all_sprites_list our l'afficher dans la prochaine salle
                    initPartie()
                    playing=False

            #affichage
            screen.fill(WHITE)
            
            draw_text(screen,'GAME OVER...', 'fonts/No_Color.ttf', 60, BLACK, SCREEN_WIDTH // 2, 200, True)
            replay_bouton.draw(screen, mx, my)
            

            
        #print(actions)
        #bidouille pour afficher instant la bote de dialogue
        if tutorial and current_room.id ==0 and not firstDialogueBoxDone :
            for pnj in current_room.pnj_list:
                dialog_loop(tutorial,True,pnj, screen, fpsClock)
                firstDialogueBoxDone=True

        # Met à jour la fenetre de jeu
        pygame.display.update()

        # --- Limite le jeu à 60 images par seconde
        fpsClock.tick(FPS)


def dessineHealBouton(screen,player):
    image = pygame.image.load("./img/slots/heal.png")
    screen.blit(image,(1150,600))
    now=time()
    timeLeft=player.healCD-(now-player.healed)
    if timeLeft > 0:
        pygame.draw.circle(screen, (55,55,55), (1182, 632), 36, 0)
        draw_text(screen,str(int(timeLeft)), 'fonts/No_Color.ttf', 40, BLACK, 1180, 630, True)
        draw_text(screen,str(int(timeLeft)), 'fonts/No_Color.ttf', 37, WHITE, 1180, 630, True)



def updateMobsStats(mobs_lists,color):
    for mob in mobs_lists:
        if mob.colorbuff == color and not mob.isboosted:
            mob.DMG*=2
            mob.speed+=3
            mob.isboosted=True
            #on recupère l'image du monstre
            mob.image = pygame.transform.scale(mob.image,(40,40))
            #on la resize
            mob.rect = mob.image.get_rect()
        elif mob.colorbuff != color and mob.isboosted:
            mob.DMG/=2
            mob.speed-=3
            mob.isboosted=False
            #on recupère l'image du monstre
            mob.image =mob.originalImage
            #on la resize
            mob.rect = mob.image.get_rect()

def manageWhiteMobs(mobs_lists, current_room, player):
    is_colored_mob=False

    for mob in mobs_lists:
        if mob.colorbuff != GRAY:
            is_colored_mob=True

    if is_colored_mob:
        current_room.spawnMonsters("exact_number", player, 1, GRAY)

def healSkill(player):
    now=time()
    timeLeft=player.healCD-(now-player.healed)
    if timeLeft <0:
        healed=False
        for item in player.inventaire.items:
            if item != False and not healed and "heal" in item.stats.keys() and player.HP < player.HP_MAX:
                #on enlève l'item de l'inventaire
                player.inventaire.remove(item)
                #on soigne le joueur
                player.HP += item.stats["heal"]
                if player.HP > player.HP_MAX:
                    player.HP = player.HP_MAX
                player.healed = time()
                healed=True

        
def estDansPolygone(x,y,polygone):
    bool = True
    n = len(polygone)
    a = polygone[n-1][0] - x
    b = polygone[n-1][1] - y
    c = polygone[0][0] - polygone[n-1][0]
    d = polygone[0][1] - polygone[n-1][1]
    z = a*d - b*c
    if z < 0:
        s = -1
    elif z > 0:
        s = 1
    else :
        s = 0
    if s!=0:
        for i in (0, n-2):
            a = polygone[i][0] - x
            b = polygone[i][1] - y
            c = polygone[i+1][0] - polygone[i][0]
            d= polygone[i+1][1] - polygone[i][1]
            z = a*d - b*c
            if z == 0:
                break
            if z * s < 0:
                bool = False
                break
    return bool


def estDansCercle(Cercle, M):
    a = Cercle[0][0] - M[0]
    b = Cercle[0][1] - M[1]
    c=sqrt(a**2 + b**2)
    if c <= Cercle[1]:
        bool = True
    else:
        bool = False
    return bool

def estDansEnsembleCercles(ensemble,M):
    n = len(ensemble)
    bool = False
    for i in range(n):
        if estDansCercle(ensemble[i], M):
            bool = True
            break
    return bool

def setColorPlayerFromPosition(taches,player):
    fin=False
    color=GRAY
    i=0
    while not fin and i <len(taches):

        tache=taches[i][0]

        if estDansEnsembleCercles(tache,player.pos()):
            colore=True
            color=taches[i][1]
        i+=1
    player.colorbuff = color


def checkRecupLoot(all_sprites_list,loots_list,player):
    for item in loots_list:
        if pygame.sprite.collide_rect(item, player):
            spaceAvailable=False
            for itemInv in player.inventaire.items:
                if itemInv==False:
                    spaceAvailable=True
            if spaceAvailable:
                loots_list.remove(item)
                all_sprites_list.remove(item)
                item.resetImage()
                player.inventaire.add(item)

def dialog_loop(tutorial,first,pnj, screen, fpsClock):
    dialog_end = False
    boite_de_dialogue = pnj.dialog_box
    dialog_box_group = pygame.sprite.Group()
    dialog_box_group.add(boite_de_dialogue)

    while not dialog_end:
        # close game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    boite_de_dialogue.boite_suiv()
                    if len(dialog_box_group) == 0:
                        boite_de_dialogue.reset_boite()
                        dialog_end = True
                        if tutorial:
                            initTutorialStep(current_room,player)

        dialog_box_group.draw(screen)

        pygame.display.update()
        fpsClock.tick(FPS)

def initTutorialStep(current_room,player):
    roomDATA= TUTORIAL_DATA[current_room.id]
    if roomDATA["step"]["action"]=="spawn":
        current_room.spawnMonsters("exact_number", player, roomDATA["step"]["number"], GRAY)
        i=0
        for mob in current_room.enemy_list:
            mob.setColor(roomDATA["step"]["color"][i]) 
            mob.speed = roomDATA["step"]["mobspeed"]
            mob.rect.x = roomDATA["step"]["pos"][i][0]
            mob.rect.y = roomDATA["step"]["pos"][i][1]
            mob.floating_point_x =roomDATA["step"]["pos"][i][0]
            mob.floating_point_y=roomDATA["step"]["pos"][i][1]
            i+=1

        all_sprites_list.add(current_room.enemy_list)
    if TUTORIAL_DATA[current_room.id]["step"]["action"]=="dmg-inv-map":
        player.HP-=10
        player.inventaire.add(Item(equipable=False,slotequipable=-1,name="Gateau aux cerises",shortName="Gateau",image="./img/food/cake.png",grade="commun",price=0.01,stats={"heal":10},description="Tutorial item"))

def checkTutorialStepCompletion(current_room,actions,tutorialCompletedF1):
    res= actions
    if TUTORIAL_DATA[current_room.id]["step"]["action"]=="spawn" and len(current_room.enemy_list)==0 and actions["kill"]:
        current_room.open_doors()
        res= {"i":False,"tab":False,"z":False,"q":False,"s":False,"d":False,"f":False,"e":False,"kill":False}
    if TUTORIAL_DATA[current_room.id]["step"]["action"]=="key":
        ok=True
        for key in TUTORIAL_DATA[current_room.id]["step"]["keys"]:
            if not actions[key]:
                ok=False
        if ok:
            current_room.open_doors()
            res= {"i":False,"tab":False,"z":False,"q":False,"s":False,"d":False,"f":False,"e":False,"kill":False}
    if TUTORIAL_DATA[current_room.id]["step"]["action"]=="dmg-inv-map":
        ok=True
        for key in TUTORIAL_DATA[current_room.id]["step"]["keys"]:
            if not actions[key]:
                ok=False
        if ok:
            current_room.open_doors()
            tutorialCompletedF1=True
            res= {"i":False,"tab":False,"z":False,"q":False,"s":False,"d":False,"f":False,"e":False,"kill":False}     

    return res, tutorialCompletedF1