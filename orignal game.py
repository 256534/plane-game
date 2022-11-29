import sys
import pygame
from time import *
from plane import Plane
from random import randint
from button import Button
from mainmenu import MainMenu
#create game instance
pygame.init()
pygame.display.set_caption("Plane Game")

#game settings
clock = pygame.time.Clock()
fps = 60
game_over = False
font = pygame.font.SysFont('comicsans', 24)
score = 0
obstacles_passed = False

#size of game
window_width = 500
window_height = 500

#set background
background = pygame.image.load('images/background.png')
background = pygame.transform.rotozoom(background, 0, .5)
screen = pygame.display.set_mode((window_width, window_height))

def draw_background():
    #fill in background
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))


#create/add first plane
plane = Plane(50, int(window_height / 2), screen)


#create/draw obstacles
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

    def update(self):
        self.rect.x -= 2
        if self.rect.right < 100:
            self.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)
cloud_group = pygame.sprite.Group()
cloud_frequency = 1000 #miliseconds
last_cloud = pygame.time.get_ticks()

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
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
        self.rect.midbottom = [x, y]
    def update(self):
        #scrolling
        self.rect.x -= 2
        if self.rect.right < 100:
            self.kill()
    def draw(self):
        self.screen.blit(self.image, self.rect)
house_group = pygame.sprite.Group()
house_frequency = 1000 #miliseconds
last_house = pygame.time.get_ticks()



#game over screen
#button = Button(window_width // 2- 50, window_height // 2 - 100)

#Run game
while True:
    #main_menu()
    # draw background
    draw_background()
    # check for collision
    cloud_collision = pygame.sprite.spritecollide(plane, cloud_group, True)
    house_collision = pygame.sprite.spritecollide(plane, house_group, True)
    if cloud_collision or house_collision:
        sys.exit()

    # draw plane on screen
    cloud_group.draw(screen)
    cloud_group.update()
    house_group.draw(screen)
    house_group.update()
    plane.draw()
    plane.update()

    #count how many houses player has successfully passed
    if len(house_group) > 0:
        if plane.rect.left > house_group.sprites()[0].rect.left\
            and plane.rect.right < house_group.sprites()[0].rect.right\
            and obstacles_passed == False:
            obstacles_passed = True
        if obstacles_passed == True:
            if plane.rect.left < house_group.sprites()[0].rect.left:
                score += 1
                obstacles_passed = False
    print(score)

    cloud_height = randint(1, 15)

    # make obstacles recycle
    if game_over == False:
        time_now = pygame.time.get_ticks()
        if time_now - last_cloud > cloud_frequency:
            skies = Sky(400, int(window_height / cloud_height))
            cloud_group.add(skies)
            last_cloud = time_now

        if time_now - last_house > house_frequency:
            grounds = Ground(400, 500)
            house_group.add(grounds)
            last_house = time_now
    #if game_over == True:
        #if button.draw() == True:
           # game_over = False

    for event in pygame.event.get():
        if plane.rect.bottom >= 450:
            sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()
        # make plane move
        #if event.type == pygame.KEYDOWN and moving == False:
           # moving = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                plane.moving_up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                plane.moving_up = False

    # add clock
    clock.tick(60)
    pygame.display.set_caption(f"Plane Game {clock.get_fps():.0f}")
    # track score (calculate score based on obstacles passed)
    img = font.render(f"Score: {score}", True, (255, 10, 10))
    screen.blit(img, (20, 20))

    #update screen
    pygame.display.flip()



#end game w sound effect


#make game speed up over time
#add opening screen

