import pygame
from constants import *
from pygame.locals import *

class Dialog_Box(pygame.sprite.Sprite):
    def __init__(self, text, author_name, x=50, y=3*(SCREEN_HEIGHT//4)):
        super().__init__()

        self.text = text
        self.author_name = author_name
        lines_tab = self.get_lines_tab(120)
        self.dialog_tab = self.get_dialog_tab(lines_tab)

        self.boite_no = 0

        self.image = self.genere_image()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def get_lines_tab(self, nb_lettres):
        lines_tab = []
        line = ""
        for i in range(len(self.text)):
            line += self.text[i]
            if (i + 1) % nb_lettres == 0:
                lines_tab.append(line)
                line = ""

        lines_tab.append(line)

        return lines_tab

    def get_dialog_tab(self, lines_tab):
        dialog_tab = []
        boite = []
        for i in range(len(lines_tab)):
            boite.append(lines_tab[i])
            if (i + 1) % 4 == 0:
                dialog_tab.append(boite)
                boite = []
        if len(lines_tab) % 4 != 0:
            dialog_tab.append(boite)
        return dialog_tab

    def genere_image(self):

        background = pygame.Surface((SCREEN_WIDTH - 100, SCREEN_HEIGHT // 4 - 50))
        background.fill(GRAY)
        background_rect = background.get_rect()

        BORDER = 10
        forground = pygame.Surface((background_rect.width - BORDER, background_rect.height - BORDER))
        forground.fill(BLACK)
        forground_rect = forground.get_rect()
        forground_rect.center = background_rect.center
        background.blit(forground, forground_rect)

        self.ecrit_boite(background, background_rect, self.dialog_tab[self.boite_no], self.author_name)
        return background



    def ecrit_boite(self, surface, surface_rect, boite, author_name):
        font = pygame.font.Font('fonts/RPGSystem.ttf', 25)
        text_image = font.render(author_name+" :", True, WHITE)
        text_rect = text_image.get_rect()
        text_rect.x = surface_rect.x + 10
        text_rect.y = surface_rect.y + 5

        surface.blit(text_image, text_rect)
        surface.blit(text_image, text_rect)

        for i in range(len(boite)):
            line = boite[i]
            font = pygame.font.Font('fonts/RPGSystem.ttf', 25)

            text_image = font.render(line, True, WHITE)
            text_rect = text_image.get_rect()
            text_rect.x = surface_rect.x + 10
            text_rect.y = surface_rect.y + 2 + ((i+1) * 25)

            surface.blit(text_image, text_rect)
            surface.blit(text_image, text_rect)

    def boite_suiv(self):
        self.boite_no += 1
        if self.boite_no > len(self.dialog_tab) - 1:
            self.kill()
        else:
            self.image = self.genere_image()

    def reset_boite(self):
        self.boite_no = 0
        self.image = self.genere_image()

    def draw(self, surface):
        surface.blit(self.image, self.rect)