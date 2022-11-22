import pygame
from pygame.sprite import Sprite
from random import choice
class Sky(Sprite):

    def __init__(self, screen):
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'images/cloud{num}.png')
            img = pygame.transform.rotozoom(img, 0, .25)
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.midtop = self.screen_rect.midtop

    def update(self):
        self.rect.x -= 2

    def draw(self):
        self.screen.blit(self.image, self.rect)