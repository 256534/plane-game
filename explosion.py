import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/explosion.png')
        self.rect = self.image.get_rect()
        self.rect.center = center
    def update(self):
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
