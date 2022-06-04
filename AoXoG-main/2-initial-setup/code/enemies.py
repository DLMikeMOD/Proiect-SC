import pygame
from settings import *
from entities import *
from support import *

class Enemy(Entity):
    def __init__(self, npc_name, position, groups, obstacles):
        # general info
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # asset info
        self.import_npc(npc_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        # npc_move
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0,-11)
        self.obstacles = obstacles

    #     npc stats
        self.monster_name = npc_name
        monster_info = monster_list[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['def']
        self.attack_radius = monster_info['hitbox']
        self.notice_radius = monster_info['aggro_range']
        self.attack_type = monster_info['attack_type']

    #     hero actions
        self.can_attack = True
        self.attack_time = None
        self.attack_cd = 420

    def import_npc(self, name):
        self.animations = {'idle':[], 'move':[], 'attac':[]}
        npc_path = f"../assets/enemies/{name}/"
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(npc_path + animation)

    def get_you_distance_direction(self,you):
        npc_vector = pygame.math.Vector2(self.rect.center)
        you_vector = pygame.math.Vector2(you.rect.center)
        distance = (you_vector - npc_vector).magnitude() #magnitude converts vector to distance

        if distance >0:
            direction = (you_vector - npc_vector).normalize() # normalizez move towards player after calculation
        else:
            direction=pygame.math.Vector2()

        return (distance,direction)

    def get_status(self, you):
        distance = self.get_you_distance_direction(you)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attac':
                self.frame_index = 0
            self.status = 'attac'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status= 'idle'

    def action(self,you):
        if self.status == 'attac':
            self.attack_time = pygame.time.get_ticks()
            print('attac')
        elif self.status == 'move':
            self.direction =self.get_you_distance_direction(you)[1]
        else:
            self.direction = pygame.math.Vector2()

    # aniamtion for npc
    def animante(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attac':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def cd(self):
        if not self.can_attack:
            time_now = pygame.time.get_ticks()
            if time_now - self.attack_time >= self.attack_cd:
                self.can_attack = True

    def update(self):
        self.move(self.speed)
        self.animante()
        self.cd()

    def npc_update(self,you):
        self.get_status(you)
        self.action(you)