
from settings import *
from floor import Floor
from you import You
from support import *
from debug import debug
from random import choice
from weapons import Weapon
from ui import UI
from entities import Entity
from enemies import Enemy


class Level:
    def __init__(self):

        # get the display surface
        # self.current_attack = None
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible = YCameraGroup()
        self.obstacles = pygame.sprite.Group()

        # sprite setup
        self.create_map()

        # UI default
        self.ui = UI()

        #     attack assets
        self.current_attack = None

    # birthplace of the map and objects
    def create_map(self):
        edges = {
            'bounds': import_csv_layout('../assets/map_objects/map_FloorAssets.csv'),
            'grass': import_csv_layout('../assets/map_objects/map_Grass.csv'),
            'large_objects': import_csv_layout('../assets/map_objects/map_LargeObjects.csv'),
            'entities': import_csv_layout('../assets/map_objects/map_Entities.csv'),
            # 'details': import_csv_layout('../assets/map_objects/map_Details.csv'),
        }

        video_assets = {
            'grass': import_folder("../assets/grass"),
            'big_obj': import_folder("../assets/objects")
        }
        # print(video_assets)

        for style, layout in edges.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'bounds':
                            Floor((x, y), [self.obstacles], 'invisible_wall')
                        if style == 'grass':
                            rand_grass_img = choice(video_assets['grass'])
                            Floor((x, y), [self.visible, self.obstacles], 'grass', rand_grass_img)
                        if style == 'large_objects':
                            obj_surface = video_assets['big_obj'][int(col)]
                            Floor((x, y), [self.visible, self.obstacles], 'large_objects', obj_surface)

                        if style == 'entities':
                            if col == '394':
                                self.you = You((2255, 2700),  # could also work with (x,y)
                                               [self.visible],
                                               self.obstacles,
                                               self.create_attacking,
                                               self.destroy_attack,
                                               self.create_spell)

                            else:
                                if col == '390':
                                    npc_name = 'bamboo'
                                elif col == '391':
                                    npc_name = 'spirit'
                                elif col == '392':
                                    npc_name = 'raccoon'
                                # elif col == '394':
                                #     npc_name = 'cyclops'
                                else:
                                    npc_name = 'cyclops'
                                Enemy(npc_name, (x, y), [self.visible],self.obstacles)

        # debug(self.you.obstacles)

    def create_attacking(self):
        self.current_attack = Weapon(self.you, [self.visible])

    def create_spell(self, style, str, cost):
        print(style)
        print(str)
        print(cost)

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        # update and draw the game
        self.visible.custom_draw(self.you)
        self.visible.update()
        self.ui.display(self.you)
        self.visible.npc_update(self.you)
        # debug(self.you.status)


# hero center
class YCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        self.centering = pygame.math.Vector2()

        # floor lvl
        self.ground_texture = pygame.image.load(
            '../assets/textures/tiles/ground-base.png'
        ).convert()
        self.ground_texture_draw = self.ground_texture.get_rect(topleft=(0, 0))

    def custom_draw(self, you):
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

    def npc_update(self,you):
        npc_sprites =[sprite for sprite in self.sprites()if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for npc in npc_sprites:
            npc.npc_update(you)
