import pygame
from pygame.sprite import Sprite

class Plane(Sprite):
    def __init__(self, x, y, screen):
        self.image = pygame.image.load('images/GreenPlane.png')
        self.image = pygame.transform.rotozoom(self.image, 0, .5)
#plane_2_image = pygame.image.load('images/ RedPlane.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.screen = screen
        self.vel = 0
        self.moving_up = False
        #moving = False

    def update(self):
        #if moving == True:
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


