import pygame, sys
from pygame.locals import *
from inventaire import Slot, checkMoveInShop, drawItemOverlay
from constants import *
from tools import draw_text
from menu import *


def shopScreen(screen, fpsClock, player, merchant):
    # liste des slots
    playerslotslist = pygame.sprite.Group()
    merchantslotslist = pygame.sprite.Group()
    # liste des items
    playeritemlist = pygame.sprite.Group()
    merchantitemlist = pygame.sprite.Group()

    # liste de tout les sprites
    all_sprites = pygame.sprite.LayeredUpdates()

    ######
    ######	INVENTAIRE
    ######

    # On change les coordonée des slots et items du joueur
    player.inventaire.createSlots(60,180)
    player.inventaire.move_all_items()
    # on ajoute les slots a la liste des slots du joueur
    for slot in player.inventaire.slots:
        playerslotslist.add(slot)
    # On change les coordonée des slots et items du marchand
    merchant.inventaire.createSlots(SCREEN_WIDTH-50-505+10, 180)
    merchant.inventaire.move_all_items()
    # on ajoute les slots a la liste des slots du marchand
    for slot in merchant.inventaire.slots:
        merchantslotslist.add(slot)

    # de meme avec les items du joueur
    for item in player.inventaire.items:
        if item != False:
            playeritemlist.add(item)
    # de meme avec les items du marchand
    for item in merchant.inventaire.items:
        if item != False:
            merchantitemlist.add(item)

    # en couche la plus basse on met les slots puis les items (pour qu'ils soit recouverts par les items)
    all_sprites.add(playerslotslist)
    all_sprites.add(merchantslotslist)

    all_sprites.add(playeritemlist)
    all_sprites.add(merchantitemlist)

    shop_on = True
    click = False
    playerItemTaken = False
    locked = False
    spritePosBeforeLock = 0
    spriteLocked = -1
    quit_button = Bouton(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 'Retour', (164, 131, 80), True, 120, 35, font_size=25)
    while shop_on:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player.inventaire.createSlots(700,180)
                    player.inventaire.move_all_items()
                    shop_on = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Detection du clic gauche la souris et de sa position
        activeMouse = pygame.mouse.get_pressed()
        mx, my = pygame.mouse.get_pos()
        if quit_button.hoover(mx, my) and click:
            player.inventaire.createSlots(700,180)
            player.inventaire.move_all_items()
            shop_on = False

        # si on clique
        if activeMouse[0] == True:
            # on regarde pour chaque item du joueur
            for item in player.inventaire.items:
                if item != False:
                    # si on est dessus et qu'on ne bouge pas déja un
                    if item.hoover(mx, my) and not locked:
                        # on le prend
                        locked = True
                        spriteLocked = item
                        spritePosBeforeLock = item.pos()
                        playerItemTaken = True
                    # si on en bouge un et que c'est cet item
                    if locked and spriteLocked == item:
                        # l'item suis notre souris
                        item.rect.x = mx - item.rect.width // 2
                        item.rect.y = my - item.rect.height // 2
            # on regarde pour chaque item du marchand
            for item in merchant.inventaire.items:
                if item != False:
                    # si on est dessus et qu'on ne bouge pas déja un
                    if item.hoover(mx, my) and not locked:
                        # on le prend
                        locked = True
                        spriteLocked = item
                        spritePosBeforeLock = item.pos()
                        playerItemTaken = False
                    # si on en bouge un et que c'est cet item
                    if locked and spriteLocked == item:
                        # l'item suis notre souris
                        item.rect.x = mx - item.rect.width // 2
                        item.rect.y = my - item.rect.height // 2
        # si on ne clique pas
        else:
            # si on avait un item
            if locked:
                # on verifie si c'est possible de poser l'item la ou il est. Si c'est possible on deplace l'item (ou les items si on inverse de place)
                checkMoveInShop(mx, my, spriteLocked, spritePosBeforeLock, playerslotslist, merchantslotslist, player, merchant, playerItemTaken)
                locked = False
                spritePosBeforeLock = 0
                spriteLocked = -1



        # Appelle la méthode update() de tous les Sprites
        all_sprites.update()

        screen.fill(WHITE)


        drawShop(screen, player, merchant)
        quit_button.draw(screen, mx, my)

        # Dessine tous les sprites (les blits sur screen)
        all_sprites.draw(screen)

        # si besoin on dessine l'overlay de l'item
        if activeMouse[0] == False:
            drawItemOverlay(screen, mx, my, playeritemlist, player.inventaire)
            drawItemOverlay(screen, mx, my, merchantitemlist, merchant.inventaire)

        click = False
        pygame.display.update()
        fpsClock.tick(FPS)


def drawShop(screen, player, merchant):
    # on dessine les background
    # fond inventaire player
    pygame.draw.rect(screen, (164, 131, 80), (50, 40, 505, 635))
    # bords inventaire player
    pygame.draw.rect(screen, (100, 64, 31), (50, 40, 505, 635), 5)
    # fond inventaire marchand
    pygame.draw.rect(screen, (164, 131, 80), (SCREEN_WIDTH-50-505, 40, 505, 635))
    # bords inventaire marchand
    pygame.draw.rect(screen, (100, 64, 31), (SCREEN_WIDTH-50-505, 40, 505, 635), 5)

    # bord bouton retour


    # puis les texts
    draw_text(screen, 'Inventaire du marchand', 'fonts/No_Color.ttf', 30, BLACK, (SCREEN_WIDTH-50-505)+505//2, 80, True)
    draw_text(screen, 'Votre inventaire', 'fonts/No_Color.ttf', 30, BLACK, 302, 80, True)
    draw_text(screen, "Votre argent : " + str(player.money)+" CC", "fonts/SuperLegendBoy-4w8Y.ttf", 20, BLACK, 302, 120, True)
    draw_text(screen, "Argent du marchand : " + str(merchant.money) + " CC", "fonts/SuperLegendBoy-4w8Y.ttf", 20, BLACK, (SCREEN_WIDTH-50-505)+505//2,120, True)
