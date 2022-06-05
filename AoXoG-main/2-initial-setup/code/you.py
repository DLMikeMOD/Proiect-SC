import pygame
from settings import *
from main_level import *
from support import import_directory
from entities import Entity


class You(Entity):
    def __init__(self, pos, groups, obstacles, create_attack, destroy_attack, create_spell):
        super().__init__(groups)
        self.image = pygame.image.load('../assets/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)

        # asset setupod for movement of you
        self.load_you_assets()
        self.status = 'down'
        # self.frame_index = 0
        # self.animation_speed = 0.15

        # move
        # self.direction = pygame.math.Vector2()
        # self.speed = 7
        self.attacking = False
        self.attacking_cd = 600
        self.attacking_time = None
        self.obstacles = obstacles

        # weaponization
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_list.keys())[self.weapon_index]
        # print(self.weapon)
        self.weapon_switch = True
        self.weapon_switch_time = None
        self.switch_cd = 200

        #     spells config
        self.create_spell = create_spell
        self.magic_index = 0
        self.magic = list(magic_list.keys())[self.magic_index]
        self.magic_switch = True
        self.magic_switch_time = None

        # status and ui (every good story starts when you are hurt)
        self.stats = {'health': 142, 'mana': 69, 'attack': 10, 'magic': 9, 'speed': 6}
        self.hp = self.stats['health'] * 0.45
        self.energy = self.stats['mana'] * 0.21
        self.xp = 420
        self.speed = self.stats['speed']

        # damaj time
        self.vincible = True
        self.pain_time = None
        self.invincible_duration = 500

    def load_you_assets(self):
        hero_path = '../assets/player/'
        self.animations = {
            'right': [],
            'down': [],
            'left': [],
            'up': [],
            'right_idle': [],
            'down_idle': [],
            'left_idle': [],
            'up_idle': [],
            'right_attac': [],
            'down_attac': [],
            'left_attac': [],
            'up_attac': []
        }

        for animation in self.animations.keys():
            animation_fpath = hero_path + animation
            self.animations[animation] = import_directory(animation_fpath)

    def input(self):
        if not self.attacking:
            global keys  # without this it is fucked
            if not self.attacking:
                keys = pygame.key.get_pressed()

            # up and down
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0  # without this it walks till it diesa

            # left and right
            if keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0  # without this it walks till it dies

            # attac need to run only once
            if keys[pygame.K_RSHIFT]:
                self.attacking = True
                self.attacking_time = pygame.time.get_ticks()
                self.create_attack()

            if keys[pygame.K_RCTRL]:
                self.attacking = True
                self.attacking_time = pygame.time.get_ticks()
                style = list(magic_list.keys())[self.magic_index]
                strenght = list(magic_list.values())[self.magic_index]['power'] + self.stats['magic']
                cost = list(magic_list.values())[self.magic_index]['cost']
                self.create_spell(style, strenght, cost)

            # swicth weapon
            if keys[pygame.K_q] and self.weapon_switch:
                self.weapon_switch = False
                self.weapon_switch_time = pygame.time.get_ticks()

                if self.weapon_index < len(list(weapon_list.keys())) - 1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0

                self.weapon = list(weapon_list.keys())[self.weapon_index]

                # swicth spells
            if keys[pygame.K_e] and self.magic_switch:
                self.magic_switch = False
                self.magic_switch_time = pygame.time.get_ticks()

                if self.magic_index < len(list(magic_list.keys())) - 1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0

                    self.magic = list(magic_list.keys())[self.magic_index]

    def get_sts(self):

        # idle and attac
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attac' in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attac' in self.status:
                if 'idle' in self.status:
                    # overwrite idle
                    self.status = self.status.replace('_idle', '_attac')
                else:
                    self.status = self.status + '_attac'
        else:
            # not needed in this version
            if 'attac' in self.status:
                self.status = self.status.replace("_attac", '')

    # this runs forever
    def cooldown(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attacking_time >= self.attacking_cd + weapon_list[self.weapon]['cooldown']:
                self.attacking = False
                self.destroy_attack()

        if not self.weapon_switch:
            if current_time - self.weapon_switch_time >= self.switch_cd:
                self.weapon_switch = True
                # self.destroy_attack()

        if not self.magic_switch:
            if current_time - self.magic_switch_time >= self.switch_cd:
                self.magic_switch = True
                # self.destroy_attack()

        if not self.vincible:
            if current_time - self.pain_time >= self.invincible_duration:
                self.vincible = True

    def animate(self):
        animation = self.animations[self.status]

        # lopp prin index de ceel 12 statusuri
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        #  seteaza iamginea
        self.image = animation[int(self.frame_index)]  # mut be converted
        self.rect = self.image.get_rect(center=self.hitbox.center)

        # your flicker
        if not self.vincible:
            alfa = self.flick_value()
            self.image.set_alpha(alfa)
        else:
            self.image.set_alpha(255)

    def get_weapon_damaj(self):
        base_dmg = self.stats['attack']
        weapon_dmg = weapon_list[self.weapon]['damage']
        return base_dmg + weapon_dmg

    def update(self):
        self.input()
        self.cooldown()
        self.get_sts()
        self.animate()
        self.move(self.speed)
        # self.visible.draw(self.display_surface)
        # self.visible_sprites.update()
