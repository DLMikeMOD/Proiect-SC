import pygame
from you import *


class Weapon(pygame.sprite.Sprite):
    def __init__(self, you, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        aim = you.status.split('_')[0] # very usefull split
        print(aim)

        # asset
        weapon_fpath = f"../assets/weapons/{you.weapon}/{aim}.png"
        self.image = pygame.image.load(weapon_fpath).convert_alpha()
        # self.image = pygame.Surface((42, 42))


        # direction aim
        if aim == 'right':
            self.rect = self.image.get_rect(midleft=you.rect.midright + pygame.math.Vector2(0,16))
        elif aim == 'left':
            self.rect = self.image.get_rect(midright=you.rect.midleft + pygame.math.Vector2(0,16))
        elif aim == 'down':
            self.rect = self.image.get_rect(midtop=you.rect.midbottom + pygame.math.Vector2(0, 0))
        else:
            self.rect = self.image.get_rect(midbottom=you.rect.midtop + pygame.math.Vector2(0, 0))
