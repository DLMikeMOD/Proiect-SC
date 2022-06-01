import pygame, sys
from settings import *
from floor import Floor
from you import You
from support import *
from debug import debug


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible = YCameraGroup()
        self.obstacles = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    # birthplace of the map
    def create_map(self):
        # edges = {
        #     'bounds': import_csv_layout('../assets/map_objects/map_FloorAssets.csv')
        # }
        # for style, layout in edges.items():
            for row_index, row in enumerate(WORLD_MAP): #change this to "edges" and uncomment for new map bounds
                for col_index, col in enumerate(row):
                    # if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        # if style == 'bounds':
                        if col == 'x':
                            Floor((x, y), [self.visible, self.obstacles], 'invisible')
                        if col == 'p':
                            self.you = You((x,y), [self.visible], self.obstacles)
        #         if col == 'x':
        #             Floor((x, y), [self.visible_sprites, self.obstacles])
        #         if col == 'i':
        #             IceWall((x,y), [self.visible_sprites, self.obstacles])
        #         if col == 'c':
        #             Campfire((x, y), [self.visible_sprites, self.obstacles])
        #         if col == 'p':
        #             self.you = You((x, y), [self.visible_sprites], self.obstacles)
        # self.you = You((1989, 1449), [self.visible], self.obstacles)
        # debug(self.you.obstacles)

    def run(self):
        # update and draw the game
        self.visible.custom_d(self.you)
        self.visible.update()
        debug(self.you.direction)


# hero center
class YCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        self.centering = pygame.math.Vector2()

        # floor lvl
        self.ground_texture = pygame.image.load('../assets/textures/tiles/ground-base.png').convert()
        self.ground_texture_draw = self.ground_texture.get_rect(topleft=(0, 0))

    def custom_d(self, you):
        # player coords
        self.centering.x = you.rect.centerx - self.half_w
        self.centering.y = you.rect.centery - self.half_h

        # birthing floor
        ground_offset = self.ground_texture_draw.topleft - self.centering
        self.display_surface.blit(self.ground_texture, ground_offset)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            center_display = sprite.rect.topleft - self.centering
            self.display_surface.blit(sprite.image, center_display)
