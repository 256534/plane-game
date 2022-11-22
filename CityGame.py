import sys
import pygame
from time import *
from plane import Plane
from ground import Ground
from clouds import Sky
from random import randint

#create game instance
pygame.init()
pygame.display.set_caption("Plane Game")

#game settings
clock = pygame.time.Clock()
fps = 60

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
#ground_group = pygame.sprite.Group()
ground = Ground(screen)
#ground_group.add(ground)

#sky_group = pygame.sprite.Group()
sky = Sky(screen)
#sky_group.add(sky)
cloud_frequency = 1000 #miliseconds
last_cloud = pygame.time.get_ticks()

house_frequency = 1000 #miliseconds
last_house = pygame.time.get_ticks()

font = pygame.font.SysFont(None, 24)
score = 1024

#Run game
while True:
    for event in pygame.event.get():
        if plane.rect.bottom > 500:
            sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()
        # make plane move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                plane.moving_up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                plane.moving_up = False


    # add clock
    clock.tick(60)
    pygame.display.set_caption(f"Plane Game {clock.get_fps():.0f}")
    # track score (calculate score based on time)
    # add in a score
    score = 0
    img = font.render(f"Score: {score}", True, (255, 0, 0))
    screen.blit(img, (20, 20))
    score += 1

    # draw background
    draw_background()

    #draw plane on screen
    plane.draw()
    plane.update()
    ground.draw()
    ground.update()
    sky.draw()
    sky.update()

    # make obstacles recycle
    time_now = pygame.time.get_ticks()
    if time_now - last_cloud > cloud_frequency:
        sky = Sky(screen)

        last_cloud = time_now
    if time_now - last_house > house_frequency:
        ground = Ground(screen)

        last_house = time_now

    #update screen
    pygame.display.flip()



#end game w sound effect


#make game speed up over time
#add opening screen
#add multiplayer
