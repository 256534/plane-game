import pygame
from pygame.sprite import Sprite
from random import choice
class Sky(Sprite):
    def __init__(self):
        self.cloud_1_image = pygame.image.load('images/cloud1.png')
        self.rect1 = self.cloud_1_image.get_rect()
        self.cloud_3_image = pygame.image.load('images/cloud2.png')
        self.rect2 = self.cloud_3_image.get_rect()
        self.cloud_5_image = pygame.image.load('images/cloud3.png')
        self.rect3 = self.cloud_5_image.get_rect()
        self.cloud_7_image = pygame.image.load('images/cloud4.png')
        self.rect4 = self.cloud_7_image.get_rect()
        self.sun_image = pygame.image.load('images/sun.png')
        self.rect5 = self.sun_image.get_rect()
    def draw(self):

        sky_obstacles = [self.cloud_1_image, self.cloud_3_image, self.cloud_5_image, self.cloud_7_image, self.sun_image]
        #self.screen.blit(self.sky_obstacles.random, self.rect)