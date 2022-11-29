import sys
import pygame
from time import *
from settings import *
from random import randint
from button import Button
from plane import Plane
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

# set background
background = pygame.image.load('images/background.png')
background = pygame.transform.rotozoom(background, 0, .5)
screen = pygame.display.set_mode((window_width, window_height))

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)

def draw_background():
        # fill in background
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
def play():
    # settings
    clock = pygame.time.Clock()
    fps = 60
    game_over = False
    font = pygame.font.SysFont('comicsans', 24)
    score = 0
    obstacles_passed = False

    # create/add first plane
    plane = Plane(50, int(window_height / 2), screen)
    #create cloud group and frequency
    cloud_group = pygame.sprite.Group()
    cloud_frequency = 1000  # miliseconds
    last_cloud = pygame.time.get_ticks()
    #create house group and frequency
    house_group = pygame.sprite.Group()
    house_frequency = 1000  # miliseconds
    last_house = pygame.time.get_ticks()

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # draw background
        draw_background()
        # check for collision
        cloud_collision = pygame.sprite.spritecollide(plane, cloud_group, True)
        house_collision = pygame.sprite.spritecollide(plane, house_group, True)
        if cloud_collision or house_collision:
            sys.exit()

        #draw clouds on screen
        cloud_group.draw(screen)
        cloud_group.update()
        #draw houses on screen
        house_group.draw(screen)
        house_group.update()
        # draw plane on screen
        plane.draw()
        plane.update()

        # count how many houses player has successfully passed
        if len(house_group) > 0:
            if plane.rect.left > house_group.sprites()[0].rect.left \
                and plane.rect.right < house_group.sprites()[0].rect.right \
                and obstacles_passed == False:
                obstacles_passed = True
            # track score (calculate score based on obstacles passed)
            if obstacles_passed == True:
                if plane.rect.left < house_group.sprites()[0].rect.left:
                    score += 1
                    obstacles_passed = False
        #print(score)

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
        # if game_over == True:
        # if button.draw() == True:
        # game_over = False

        #for event in pygame.event.get():


        #PLAY_TEXT = get_font(25).render("PLAY screen.", True, "White")
        #PLAY_RECT = PLAY_TEXT.get_rect(center=(250, 200))
        #screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(450, 450),
                           text_input="BACK", font=get_font(10), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if plane.rect.bottom >= 450:
                sys.exit()
            if plane.rect.top <= 10:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    plane.moving_up = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    plane.moving_up = False
        clock.tick(60)
        pygame.display.set_caption(f"Plane Game {clock.get_fps():.0f}")
        # add in a score
        img = font.render(f"Score: {score}", True, (15, 10, 10))
        screen.blit(img, (20, 20))



        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(25).render(" How to play:\n use up arrow key \n to keep plane up \n and avoid obstacles.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(250, 200))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(250, 300),
                              text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#main menu/opening screen
def main_menu():
    while True:
        screen.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(250, 100))
        button = pygame.image.load('images/button.png')
        button = pygame.transform.rotozoom(button, 0, .5)
        PLAY_BUTTON = Button(image= button, pos=(250, 200),
                             text_input="PLAY", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image= button, pos=(250, 250),
                                text_input="OPTIONS", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image= button, pos=(250, 300),
                             text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()




#game over screen
#end game w sound effect
#make game speed up over time


#Run game
while True:
    main_menu()

    #update screen
    pygame.display.flip()
