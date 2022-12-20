import sys
import pygame
#size of game
window_width = 500
window_height = 500

screen = pygame.display.set_mode((window_width, window_height))
class Game():
    def __init__(self):
        # set background
        self.background = pygame.image.load('images/background.png')
        self.background = pygame.transform.rotozoom(self.background, 0, .5)
        self.screen = pygame.display.set_mode((500, 500))
    def draw_background(self):
        # fill in background
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))

 # create/draw obstacles
class Sky(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
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
        self.rect.midtop = [x, y]

    def update(self, speed = 2):
        self.rect.x -= speed
        #speed -= 2
        if self.rect.right < 100:
            self.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)



class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'images/house{num}.png')
            img = pygame.transform.rotozoom(img, 0, .25)
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.midbottom = [x, y]

    def update(self, speed = 2):
            # scrolling
        self.rect.x -= speed
        if self.rect.right < 100:
            self.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)

