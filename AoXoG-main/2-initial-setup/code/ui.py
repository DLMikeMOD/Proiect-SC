import pygame

from settings import *


class UI:
    def __init__(self):
        #  fonts loader
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # user bars
        self.hp_bar = pygame.Rect(12, 12, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.mana_bar = pygame.Rect(12, 32, ENERGY_BAR_WIDTH, BAR_HEIGHT)

    #     convert dict of weapons
        self.weapon_icons = []
        for weapon in weapon_list.values():
            path = weapon['icon']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_icons.append(weapon)

    #     convert spell dictionary
        self.magic_assets =[]
        for magic in magic_list.values():
            magic = pygame.image.load(magic['icon']).convert_alpha()
            self.magic_assets.append(magic)


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

    def select_box(self,left,bottom, did_switch):
        bg_rec = pygame.Rect(left,bottom,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rec)
        if did_switch:
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rec,5)
        else:
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rec,5)
        return bg_rec

    # showing the weapon icon
    def weapon_icon(self,weapon_index,did_switch):
        bg_rec = self.select_box(10, 770, did_switch)
        weapon_asset = self.weapon_icons[weapon_index]
        weapon_rect = weapon_asset.get_rect(center = bg_rec.center)

        self.display_surface.blit(weapon_asset,weapon_rect)

    def magic_icon(self,magic_index,did_switch):
        bg_rec = self.select_box(79,770, did_switch)
        magic_surface = self.magic_assets[magic_index]
        magic_rect = magic_surface.get_rect(center=bg_rec.center)

        self.display_surface.blit(magic_surface,magic_rect)


    def display(self, you):
        self.show_ui_bar(you.hp, you.stats['health'], self.hp_bar, HEALTH_COLOR)
        self.show_ui_bar(you.energy, you.stats['mana'], self.mana_bar, ENERGY_COLOR)

        self.show_xp(you.xp)

        self.weapon_icon(you.weapon_index,not you.weapon_switch) # weapon show
        self.magic_icon(you.magic_index,not you.magic_switch)