from menu import *
from constants import *
from Bullet import *
from Ennemis import *
from player import *

def initSprites():
    global all_sprites_list,enemy_list,bullet_list,player
    # --- Listes de Sprites
    # Ceci est la liste de tous les sprites. Tous les ennemis et le joueur aussi.
    # Un groupe de sprite LayeredUpdates possede en plus un ordre (pour l'affichage)
    all_sprites_list = pygame.sprite.LayeredUpdates()

    # Liste de tous les ennemis
    enemy_list = pygame.sprite.Group()

    # Liste des balles
    bullet_list = pygame.sprite.Group()

    # --- Creation des Sprites
    # Création du joueur
    player = Player("Test", 0, 0, 6)

    player.rect.centerx = 2 * SCREEN_WIDTH // 3
    player.rect.centery = 2 * SCREEN_HEIGHT // 3

    # Création d'un monstre
    m1 = Monstre1(random.randint(0, SCREEN_WIDTH),
                  random.randint(0, SCREEN_HEIGHT // 3),
                  player)

    # Ajout du monstre sprite dans le Group enemy_list
    enemy_list.add(m1)

    # Ajout des sprite dans l'ordre d'affichange dans le Group all_sprites_list
    all_sprites_list.add(m1)
    all_sprites_list.add(bullet_list)
    all_sprites_list.add(player)


def spawnNMonsters(N):
    """Cette fonction fait appraitre N enemies"""
    for i in range(0, N):
        monstre = Monstre1(random.randint(0, SCREEN_WIDTH),
                           random.randint(0, SCREEN_HEIGHT // 3),
                           player)
        enemy_list.add(monstre)
        all_sprites_list.add(monstre)



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
    draw_text(screen, "PV : " + str(player.HP) + "/" + str(player.HP_MAX), 'fonts/RPGSystem.ttf', 20, BLACK, 10, SCREEN_HEIGHT//2+20, False)

    # Affichage DMG
    draw_text(screen, "DMG : " + str(player.DMG), 'fonts/RPGSystem.ttf', 20, BLACK, 10,SCREEN_HEIGHT // 2, False)

    # Affichage TPS
    draw_text(screen, "TPS : " + str(player.tps), 'fonts/RPGSystem.ttf', 20, BLACK, 10,SCREEN_HEIGHT // 2-20, False)

    # Affichage SPEED
    draw_text(screen, "SPEED : " + str(player.speed), 'fonts/RPGSystem.ttf', 20, BLACK, 10,SCREEN_HEIGHT // 2-40, False)


def main_menu(screen,fpsClock):
    running = True
    click = False
    #créer les boutons
    b1 = Bouton(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, 'Jouer', RED)
    b2 = Bouton(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 'Options', GREEN)
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
                pass # options()
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



def game(screen,fpsClock):
    playing = True
    while playing:

        # --- Gestion des Event
        for event in pygame.event.get():

            # close game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Detection d'utilisation du clavier pour faire spawner 3 monstres
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP5:  # bottom
                    spawnNMonsters(3)
                if event.key == K_ESCAPE:
                    playing = False
                if event.key == K_1:
                    player.colorbuff=GRAY
                if event.key == K_2:
                    player.colorbuff=RED

        # Detection d'utilisation du clavier pour déplacer le joueur:

        activeKey = pygame.key.get_pressed()

        if activeKey[K_a]:  # left
            player.move("LEFT")
        if activeKey[K_d]:  # right
            player.move("RIGHT")
        if activeKey[K_w]:  # top
            player.move("UP")
        if activeKey[K_s]:  # bottom
            player.move("DOWN")
        # shoot
        activeMouse = pygame.mouse.get_pressed()
        # print(activeMouse)
        if activeMouse[0] == True:
            if player.cooldown >= player.cooldown_max:
                # position de la souris
                pos = pygame.mouse.get_pos()

                mouse_x = pos[0]
                mouse_y = pos[1]

                # Créé la balle
                bullet = Bullet(player.rect.centerx, player.rect.centery, mouse_x, mouse_y,player.colorbuff)

                # et l'ajoute a la liste des balles
                bullet_list.add(bullet)
                all_sprites_list.add(bullet)
                # Remise à 0 du temps de rechargement de tire
                player.cooldown = 0

        # --- Logique du jeu
        for bullet in bullet_list:

            # Si une balle touche un monstre
            enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, False)

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

            # On supprime la balle de la liste des sprites si elle sort de l'écran
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

        # Colision entre joueur et monstre
        for mob in enemy_list:
            if pygame.sprite.collide_rect(mob, player) and not player.get_hit:
                player.get_hit = True
                player.HP -= mob.DMG



        # Appelle la méthode update() de tous les Sprites
        all_sprites_list.update()

        # --- Dessiner la frame
        # Clear the screen

        screen.fill(WHITE)

        # Dessine tous les sprites (les blits sur screen)
        all_sprites_list.draw(screen)

        # Affichage HUD
        draw_HUD(screen)

        # Met à jour la fenetre de jeu
        pygame.display.update()

        # --- Limite le jeu à 60 images par seconde
        fpsClock.tick(FPS)