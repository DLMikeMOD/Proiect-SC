import pygame
from settings import *


# needs a position and an argument
class Floor(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'large_objects':
            # make offset
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1]- TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft=pos)

        self.hitbox = self.rect.inflate(0, -10)


# #old floor tile
# class Floor(pygame.sprite.Sprite):
#     def __init__(self, pos, groups):
#         super().__init__(groups)
#         self.image = pygame.image.load('../assets/test/Rock.png')
#         self.rect = self.image.get_rect(topleft=pos)
#         self.hitbox = self.rect.inflate(0, -7)

# #
# class IceWall(pygame.sprite.Sprite):
#     def __init__(self, pos, groups):
#         super().__init__(groups)
#         self.image = pygame.image.load('../assets/test/IceRock.png').convert_alpha()
#         self.rect = self.image.get_rect(bottomleft=pos)
#         self.hitbox = self.rect.inflate(0, -10)
#
#
# class Campfire(pygame.sprite.Sprite):
#     def __init__(self, pos, groups):
#         super().__init__(groups)
#         self.image = pygame.image.load('../assets/test/campfire_48x48.gif').convert_alpha()
#         self.rect = self.image.get_rect(bottomleft=pos)
#         self.hitbox = self.rect.inflate(0, -5)
