import pygame
from settings import *


class Upgrade:
    def __init__(self, you):

        # general settigns
        self.display_surface = pygame.display.get_surface()
        self.you = you
        self.attr_nr = len(you.stats)
        self.attr_name = list(you.stats.keys())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # selection system
        self.select_index = 0
        self.select_time = None
        self.movable = True

    def input(self):
        keys = pygame.key.get_pressed()

        if self.movable:
            if keys[pygame.K_RIGHT] and self.select_index < self.attr_nr - 1:
                self.select_index += 1
                self.movable = False
                self.select_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.select_index >= 1:
                self.select_index -= 1
                self.movable = False
                self.select_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.movable = False
                self.select_time = pygame.time.get_ticks()
                print(self.select_index)

    def select_cd(self):
        if not self.movable:
            current_time = pygame.time.get_ticks()
            if current_time - self.select_time >= 300:
                self.movable = True

    def display(self):
        self.input()
        self.select_cd()
