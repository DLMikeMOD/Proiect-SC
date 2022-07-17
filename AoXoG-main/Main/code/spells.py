import pygame
from settings import *
from random import randint


class YouMagic:
    def __init__(self, you_animation):
        self.you_animation = you_animation
        self.sounds = {
            'heal': pygame.mixer.Sound("../assets/audio/heal.wav"),
            'flame': pygame.mixer.Sound("../assets/audio/Fire.wav")
            }

    # heal is much simpler because animation only happens on self.you (player)
    def heal(self, you, power, cost, groups):
        if you.energy >= cost:
            self.sounds['heal'].play()
            you.hp += power
            you.energy -= cost
            if you.hp >= you.stats['health']:
                you.hp = you.stats['health']

            self.you_animation.create_genericsplash('aura', you.rect.center, groups)
            self.you_animation.create_genericsplash('heal', you.rect.center + pygame.math.Vector2(0, -33), groups)

    # offense spells need a direction and a target

    def flame(self, you, cost, groups):
        if you.energy >= cost:
            you.energy -= cost
            self.sounds['flame'].play()


            # get direction for aiming the spell that contains projectiles
            if you.status.split('_')[0] == 'left':
                aim_spell = pygame.math.Vector2(-1, 0)
            elif you.status.split('_')[0] == 'right':
                aim_spell = pygame.math.Vector2(1, 0)
            elif you.status.split('_')[0] == 'up':
                aim_spell = pygame.math.Vector2(0, -1)
            else:
                aim_spell = pygame.math.Vector2(0, 1)

            # needs to start at index 1 not 0 so offset will be correct on spell cast for all projectiles
            for i in range(1, 6):
                if aim_spell.x:  # hor
                    offset_x = (aim_spell.x * i) * TILESIZE
                    x = you.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = you.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.you_animation.create_genericsplash('flame', (x, y), groups)
                else:  # verti
                    offset_y = (aim_spell.y * i) * TILESIZE
                    x = you.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = you.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.you_animation.create_genericsplash('flame', (x, y), groups)

    def ice_spike(self, you, cost, groups):
        if you.energy >= cost:
            you.energy -= cost

            # get direction for aiming the spell that contains projectiles
            if you.status.split('_')[0] == 'left':
                aim_spell = pygame.math.Vector2(-1, 0)
            elif you.status.split('_')[0] == 'right':
                aim_spell = pygame.math.Vector2(1, 0)
            elif you.status.split('_')[0] == 'up':
                aim_spell = pygame.math.Vector2(0, -1)
            else:
                aim_spell = pygame.math.Vector2(0, 1)

            # needs to start at index 1 not 0 so offset will be correct on spell cast for all projectiles
            for i in range(1, 6):
                if aim_spell.x:  # hor
                    offset_x = (aim_spell.x * i) * TILESIZE
                    x = you.rect.centerx + offset_x
                    y = you.rect.centery
                    self.you_animation.create_genericsplash('ice-spike', (x, y), groups)
                else:  # verti
                    offset_y = (aim_spell.y * i) * TILESIZE
                    x = you.rect.centerx
                    y = you.rect.centery + offset_y
                    self.you_animation.create_genericsplash('ice-spike', (x, y), groups)
