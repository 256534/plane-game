import pygame
from pygame.sprite import Sprite
from time import *
from math import cos
class Plane(Sprite):
    def __init__(self, x, y, screen):
        self.image = pygame.image.load('images/GreenPlane.png')
        self.image = pygame.transform.rotozoom(self.image, 0, .5)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.screen = screen
        self.vel = 0
        self.moving_up = False


    def update(self):
        self.vel += 0.5
        # create gravity
        if self.vel > 9:
            self.vel = 9
        if self.rect.bottom < 500:
            self.rect.y += int(self.vel)

        #moving
        if self.moving_up:
            self.vel = -5

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def crash(self):
        #new image for crash
        self.image = pygame.image.load('images/explosion.png')
        self.image = pygame.transform.rotozoom(self.image, 0, .15)
