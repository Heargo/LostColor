import pygame
import sys
from pygame import *

class Bouton():

    def __init__(self, x, y, text, color, center=True, width=300, height=75, font='fonts/No_Color.ttf',font_size=40):
        self.text = text
        self.color = color

        self.image = pygame.Surface((width, height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()

        font = pygame.font.Font(font, font_size)
        self.text_surface = font.render(text, True, (0,0,0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.centerx = self.rect.centerx
        self.text_rect.centery = self.rect.centery
        self.image.blit(self.text_surface, self.text_rect)

        if center:
            self.rect.centerx = x
            self.rect.centery = y
        else:
            self.rect.x = x
            self.rect.y = y

        self.filtre = pygame.Surface((self.rect.width, self.rect.height), SRCALPHA)
        self.filtre_rect = self.filtre.get_rect()
        self.filtre.fill((255,255,255,100))
        self.filter_on = False

    def hoover(self, mx, my):
        if self.rect.collidepoint(mx, my):
            is_hoover = True
        else:
            is_hoover = False
        return is_hoover

    def draw(self, surface, mx, my):
        is_hoover = self.hoover(mx, my)

        if is_hoover and self.filter_on == False:
            self.image.blit(self.filtre,self.filtre_rect)
            self.filter_on = True
        elif is_hoover == False and self.filter_on == True:
            self.image.fill(self.color)
            self.image.blit(self.text_surface, self.text_rect)
            self.filter_on = False

        surface.blit(self.image, self.rect)



