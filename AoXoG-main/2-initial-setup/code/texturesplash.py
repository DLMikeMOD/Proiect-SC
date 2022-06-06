import pygame
import self

from support import import_directory
from random import choice
from settings import *


class YouAnimation:
    def __init__(self):
        self.splash_frames = {
            # magic
            'flame': import_directory('../assets/splash-animation/flame/frames'),
            'aura': import_directory('../assets/splash-animation/aura'),
            'heal': import_directory('../assets/splash-animation/heal/frames'),
            'ice-spike': import_directory('../assets/splash-animation/ice_spell/frames'),

            # attacks
            'claw': import_directory('../assets/splash-animation/claw'),
            'slash': import_directory('../assets/splash-animation/slash'),
            'sparkle': import_directory('../assets/splash-animation/sparkle'),
            'leaf_attack': import_directory('../assets/splash-animation/leaf_attack'),
            'thunder': import_directory('../assets/splash-animation/thunder'),
            'seed_bullet': import_directory('../assets/splash-animation/seed_bullet'),

            # monster deaths
            'squid': import_directory('../assets/splash-animation/smoke_orange'),
            'raccoon': import_directory('../assets/splash-animation/raccoon'),
            'spirit': import_directory('../assets/splash-animation/nova'),
            'bamboo': import_directory('../assets/splash-animation/bamboo'),
            'cyclops': (import_directory('../assets/splash-animation/cyclops')),

            # leafs
            'leaf': (
                import_directory('../assets/splash-animation/leaf1'),
                import_directory('../assets/splash-animation/leaf2'),
                import_directory('../assets/splash-animation/leaf3'),
                import_directory('../assets/splash-animation/leaf4'),
                import_directory('../assets/splash-animation/leaf5'),
                import_directory('../assets/splash-animation/leaf6'),
                self.splash_reflect(import_directory('../assets/splash-animation/leaf1')),
                self.splash_reflect(import_directory('../assets/splash-animation/leaf2')),
                self.splash_reflect(import_directory('../assets/splash-animation/leaf3')),
                self.splash_reflect(import_directory('../assets/splash-animation/leaf4')),
                self.splash_reflect(import_directory('../assets/splash-animation/leaf5')),
                self.splash_reflect(import_directory('../assets/splash-animation/leaf6'))
            ),

            # 'campfire': import_directory('../assets/splash-animation/campfire'), # to be used in beta 2.0
        }

    def splash_reflect(self, splash_frames):
        new_splash = []

        for splash in splash_frames:
            mirror_splash = pygame.transform.flip(splash, True, False)
            new_splash.append(mirror_splash)
        return new_splash

    def create_grass_splash(self, loc, groups):
        splash_animation = choice(self.splash_frames['leaf'])
        SplashEffects(loc, splash_animation, groups)

    def create_genericsplash(self,splash_type, loc, groups):
        splash_animation = self.splash_frames[splash_type]
        SplashEffects(loc, splash_animation, groups)


class SplashEffects(pygame.sprite.Sprite):
    def __init__(self, loc, splash_animation, groups):
        super().__init__(groups)
        self.sprite_type = 'spells'
        self.frame_index = 0
        self.splash_speed = 0.15
        self.splash_frames = splash_animation
        self.image = self.splash_frames[self.frame_index]
        self.rect = self.image.get_rect(center=loc)

    def animate(self):
        self.frame_index += self.splash_speed
        if self.frame_index >= len(self.splash_frames):
            self.kill()
        else:
            self.image = self.splash_frames[int(self.frame_index)]

    def update(self):
        self.animate()
