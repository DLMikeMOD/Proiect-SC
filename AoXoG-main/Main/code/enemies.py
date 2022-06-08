import pygame
import self

from settings import *
from entities import *
from support import *
from you import You


class Enemy(Entity):
    def __init__(self, npc_name, position, groups, obstacles, damaj_you, kill_splash,add_xp):
        # general info
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # asset info
        self.import_npc(npc_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        # npc_move
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -11)
        self.obstacles = obstacles

        #     npc stats
        self.monster_name = npc_name
        monster_info = monster_list[self.monster_name]
        self.health = monster_info['health']
        self.xp = monster_info['xp']
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
        self.damaj_you = damaj_you
        self.kill_splash = kill_splash
        self.add_xp = add_xp

        # Invulnrable frame timer
        self.vincible = True
        self.damage_time = None
        self.invincibility_lenght = 300

    def import_npc(self, name):
        self.animations = {'idle': [], 'move': [], 'attac': []}
        npc_path = f"../assets/enemies/{name}/"
        for animation in self.animations.keys():
            self.animations[animation] = import_directory(npc_path + animation)

    def get_you_distance_direction(self, you):
        npc_vector = pygame.math.Vector2(self.rect.center)
        you_vector = pygame.math.Vector2(you.rect.center)
        distance = (you_vector - npc_vector).magnitude()  # magnitude converts vector to distance

        if distance > 0:
            direction = (you_vector - npc_vector).normalize()  # normalizez move towards player after calculation
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, you):
        distance = self.get_you_distance_direction(you)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attac':
                self.frame_index = 0
            self.status = 'attac'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def action(self, you):
        if self.status == 'attac':
            self.attack_time = pygame.time.get_ticks()
            self.damaj_you(self.attack_damage, self.attack_type)
        elif self.status == 'move':
            self.direction = self.get_you_distance_direction(you)[1]
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

        if not self.vincible:
            alfa = self.flick_value()
            self.image.set_alpha(alfa)
        else:
            self.image.set_alpha(255)  # 255 means full value

    def cd(self):
        time_now = pygame.time.get_ticks()
        if not self.can_attack:
            if time_now - self.attack_time >= self.attack_cd:
                self.can_attack = True

        if not self.vincible:
            if time_now - self.damage_time >= self.invincibility_lenght:
                self.vincible = True

    def damaj(self, you, type_of_attac):
        if self.vincible:
            self.direction = self.get_you_distance_direction(you)[1]
            if type_of_attac == 'weapon':
                self.health -= you.get_weapon_damaj()
            else:
            #     magic damaj to enemy
                self.health -= you.get_spell_damaj()

            self.damage_time = pygame.time.get_ticks()
            self.vincible = False

    def kill_check(self):
        if self.health <= 0:
            self.kill()
            self.kill_splash(self.rect.center,self.monster_name)
            self.add_xp(self.xp)

    def damaj_react(self):
        if not self.vincible:
            self.direction *= -self.resistance

    def update(self):
        self.damaj_react()
        self.move(self.speed)
        self.animante()
        self.cd()
        self.kill_check()

    def npc_update(self, you):
        self.get_status(you)
        self.action(you)
