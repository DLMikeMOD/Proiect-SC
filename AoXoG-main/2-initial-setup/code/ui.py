import pygame

from settings import *


class UI:
    def __init__(self):
        #  fonts loader
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # user bars
        self.hp_bar = pygame.Rect(12, 12, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.mana_bar = pygame.Rect(12, 32, ENERGY_BAR_WIDTH, BAR_HEIGHT )

    def show_ui_bar(self, current, max_amm, bg_rec, color):
        #     make bg
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rec)

        # convert stats to pixel
        ratio = current / max_amm
        current_width = bg_rec.width * ratio
        current_rect = bg_rec.copy()
        current_rect.width = current_width

        #     make bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rec,5)

    def show_xp(self,xp):
        text_surface = self.font.render(str(int(xp)),False,TEXT_COLOR) # making sure the number is a number via integer conversion
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surface.get_rect(bottomright= (x,y))

        pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
        self.display_surface.blit(text_surface,text_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),5)

    def display(self, you):
        self.show_ui_bar(you.hp, you.stats['health'], self.hp_bar, HEALTH_COLOR)
        self.show_ui_bar(you.energy, you.stats['mana'], self.mana_bar, ENERGY_COLOR)

        self.show_xp(you.xp)
