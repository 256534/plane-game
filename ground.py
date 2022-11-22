import pygame
from pygame.sprite import Sprite

class Ground(Sprite):
    def __init__(self, screen):
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img = pygame.image.load(f'images/house{num}.png')
            img = pygame.transform.rotozoom(img, 0, .25)
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    def update(self):
        #scrolling
        self.counter += 1
    def draw(self):
        self.screen.blit(self.image, self.rect)
