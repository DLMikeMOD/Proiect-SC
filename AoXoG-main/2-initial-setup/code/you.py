import pygame
from settings import *


class You(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacles):
        super().__init__(groups)
        self.image = pygame.image.load('../assets/test/big_hero.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacles = obstacles

    def input(self):
        keys = pygame.key.get_pressed()

        # up and down
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0 # without this it walks till it dies

        # left and right
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0 # without this it walks till it dies

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collide('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collide('vertical')
        self.rect.center = self.hitbox.center



        # self.rect.center += self.direction * speed

#collision functionality
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

    def update(self):
        self.input()
        self.move(self.speed)
        # self.visible_sprites.draw(self.display_surface)
        # self.visible_sprites.update()
