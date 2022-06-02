import pygame
from settings import *
from main_level import *
from support import import_folder


class You(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacles, create_attacking, destroy_attack):
        super().__init__(groups)
        self.image = pygame.image.load('../assets/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)

        # asset setupod for movement of you
        self.load_you_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # move
        self.direction = pygame.math.Vector2()
        self.speed = 7
        self.attacking = False
        self.attacking_cd = 400
        self.attacking_time = None

        self.obstacles = obstacles

        # weaponization
        self.create_attack = create_attacking
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_list.keys())[self.weapon_index]
        # print(self.weapon)
        self.weapon_switch = True
        self.weapon_switch_time = None
        self.switch_cd = 200

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
            self.animations[animation] = import_folder(animation_fpath)

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
                print('magic')

            if keys[pygame.K_q] and self.weapon_switch:
                self.weapon_switch = False
                self.weapon_switch_time = pygame.time.get_ticks()

                if self.weapon_index < len(list(weapon_list.keys())) - 1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0

                self.weapon = list(weapon_list.keys())[self.weapon_index]

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

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collide('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collide('vertical')
        self.rect.center = self.hitbox.center

        self.rect.center += self.direction * speed

    # collision functionality
    def collide(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacles:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacles:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # up
                        self.hitbox.top = sprite.hitbox.bottom

    # this runs forever
    def cooldown(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attacking_time >= self.attacking_cd:
                self.attacking = False
                self.destroy_attack()

        if not self.weapon_switch:
            if current_time - self.weapon_switch_time >= self.switch_cd:
                self.weapon_switch = True
                # self.destroy_attack()

    def animate(self):
        animation = self.animations[self.status]

        # lopp prin index de ceel 12 statusuri
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        #  seteaza iamginea
        self.image = animation[int(self.frame_index)]  # mut be converted
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        self.input()
        self.cooldown()
        self.get_sts()
        self.animate()
        self.move(self.speed)
        # self.visible.draw(self.display_surface)
        # self.visible_sprites.update()