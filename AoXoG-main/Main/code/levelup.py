import pygame
from settings import *


class Upgrade:
    def __init__(self, you):

        # general settigns
        self.display_surface = pygame.display.get_surface()
        self.you = you
        self.attr_nr = len(you.stats)
        self.attr_name = list(you.stats.keys())
        self.max_values = list(you.max_stats.values())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # slider width and height creation
        self.width = self.display_surface.get_size()[0] // 6
        self.height = self.display_surface.get_size()[1] * 0.8
        self.make_slider()

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
                self.slider_list[self.select_index].trigger(self.you)

    def select_cd(self):
        if not self.movable:
            current_time = pygame.time.get_ticks()
            if current_time - self.select_time >= 300:
                self.movable = True

    def make_slider(self):
        self.slider_list = []

        for slider, index in enumerate(range(self.attr_nr)):
            # horizontal position
            full_width = self.display_surface.get_size()[0]
            increase = full_width // self.attr_nr
            left = (slider * increase) + (increase - self.width) // 2

            # vertical position
            top = self.display_surface.get_size()[1] * 0.1

            # create the slider
            slider = Slider(left, top, self.width, self.height, index, self.font)
            self.slider_list.append(slider)

    def display(self):
        self.input()
        self.select_cd()

        for index, slider in enumerate(self.slider_list):
            # get attributes
            name = self.attr_name[index]
            val = self.you.get_val_by_index(index)
            max_val = self.max_values[index]
            cost = self.you.get_cost_by_index(index)
            slider.display(self.display_surface, self.select_index, name, val, max_val, cost)


class Slider:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l, t, w, h)
        self.index = index
        self.font = font

    def show_names(self, surface, name, cost, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # text
        text_surface = self.font.render(name, False, color)
        text_rect = text_surface.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 20))
        # cost
        cost_surface = self.font.render(f'{int(cost)}', False,
                                        color)  # possiblity for cost to become floating point number, and converitng to f string and integer solves all possible implications
        cost_rect = cost_surface.get_rect(midbottom=self.rect.midbottom - pygame.math.Vector2(0, 20))
        # create
        surface.blit(text_surface, text_rect)
        surface.blit(cost_surface, cost_rect)

    def show_bar(self, surface, value, max_val, selected):

        # slider setup
        top = self.rect.midtop + pygame.math.Vector2(0, 60)
        bottom = self.rect.midbottom - pygame.math.Vector2(0, 60)
        color = BAR_COLOR_SELECTED if selected else BAR_COLOR

        # slider params
        full_height = bottom[1] - top[1]
        relative_nr = (value / max_val) * full_height
        val_rect = pygame.Rect(top[0] - 15, bottom[1] - relative_nr, 30, 10)

        # draw slider
        pygame.draw.line(surface, color, top, bottom, 10)
        pygame.draw.rect(surface,color,val_rect)

    def trigger(self,you):
        lvlup_attributes = list(you.stats.keys())[self.index]

        if you.xp >= you.upgrade_price[lvlup_attributes] and you.stats[lvlup_attributes] < you.max_stats[lvlup_attributes]:
            you.xp -= you.upgrade_price[lvlup_attributes]
            you.stats[lvlup_attributes] *= 1.2
            you.upgrade_price[lvlup_attributes] *= 1.4

        if you.stats[lvlup_attributes] > you.max_stats[lvlup_attributes]:
            you.stats[lvlup_attributes] = you.max_stats[lvlup_attributes]

    def display(self, surface, select_nr, name, value, max_val, cost):
        if self.index == select_nr:
            pygame.draw.rect(surface, UPGRADE_BG_COLOR_SELECTED, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)

        self.show_names(surface, name, cost, self.index == select_nr)
        self.show_bar(surface, value, max_val, self.index == select_nr)
