import sys
import pygame
from time import sleep
from plane import Plane
from ground import Ground
from random import randint

#create game instance
pygame.init()
pygame.display.set_caption("Plane Game")

#game settings
clock = pygame.time.Clock()
fps = 60

#size of game
window_width = 400
window_height = 400

#set background
background = pygame.image.load('images/background.png')
background = pygame.transform.rotozoom(background, 0, .5)
screen = pygame.display.set_mode((window_width, window_height))


def draw_background():
    #fill in background
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

#add first plane
plane = Plane(50, int(window_height / 2), screen)

#create obstacles
ground = Ground(screen)
#def draw_obstacles():

font = pygame.font.SysFont(None, 24)
score = 1024
#Run game
while True:
    for event in pygame.event.get():
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
    img = font.render(f"Score: {score}", True, (255, 0, 0))
    screen.blit(img, (20, 20))
    score += 1
    # draw background
    draw_background()
    #draw plane on screen
    plane.draw()
    plane.update()
    ground.draw()
    #update screen
    pygame.display.flip()



#make obstacles move
#end game w sound effect


#make game speed up over time
#add opening screen
#add multiplayer
