import sys
from pygame import *
from time import *
from settings import *
from random import randint
from button import Button
from plane import Plane
from os import path
import json

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
    font = pygame.font.SysFont('comicsans', 24)
    obstacles_passed = False

    #save and reload game
    #reads score file to reload game
    try:                                       
        with open('score.txt', 'r') as file:   
            score = json.load(file)            
    except:                                    
        score = 0
    # create/add first plane
    plane = Plane(50, int(window_height / 2), screen)
    #create cloud group and frequency
    cloud_group = pygame.sprite.Group()
    cloud_frequency = 1000  # milliseconds
    last_cloud = pygame.time.get_ticks()

    #create house group and frequency
    house_group = pygame.sprite.Group()
    house_frequency = 1000  # milliseconds
    last_house = pygame.time.get_ticks()


    #runs through the actual game
    run = True
    while run:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # draws background
        draw_background()

        # initiates sound of crash/collision
        crash_sound = pygame.mixer.Sound('images/crashaudio.ogg')
        pygame.mixer.music.load('images/crashaudio.ogg')


        # checks for collision using sprites
        cloud_collision = pygame.sprite.spritecollide(plane, cloud_group, True)
        house_collision = pygame.sprite.spritecollide(plane, house_group, True)

        if cloud_collision or house_collision:
            #crash sound & explosion image
            plane.crash()
            pygame.mixer.Sound.play(crash_sound)
            pygame.mixer.music.stop()
            pygame.time.wait(1000)
            run = False


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
                    
        #check difficulty based on current score and make the obstacles move faster
        if score > 5:
            cloud_group.update(2.15)
            house_group.update(2.15)
            cloud_frequency = 1000
            house_frequency = 1000
        if score > 10:
            cloud_group.update(2.25)
            house_group.update(2.25)
            cloud_frequency = 900
            house_frequency = 900
        if score > 15:
            cloud_group.update(2.75)
            house_group.update(2.75)
            cloud_frequency = 700
            house_frequency = 700
        if score > 20:
            cloud_group.update(3)
            house_group.update(3)
            cloud_frequency = 600
            house_frequency = 600
            
        #random location of cloud (generator)
        cloud_height = randint(1, 15)

        # make obstacles recycle
        if run == True:
            time_now = pygame.time.get_ticks()
            if time_now - last_cloud > cloud_frequency:
                skies = Sky(400, int(window_height / cloud_height))
                cloud_group.add(skies)
                last_cloud = time_now

            if time_now - last_house > house_frequency:
                grounds = Ground(400, 500)
                house_group.add(grounds)
                last_house = time_now
        #back button during game
        PLAY_BACK = Button(image=None, pos=(450, 450),
                           text_input="BACK", font=get_font(10), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)
        #game movements(exit, save game, key input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    #save and reload game
                    with open('score.txt', 'w') as file:
                        json.dump(score, file)
                    main_menu()
            if plane.rect.bottom >= 450 or plane.rect.top <= 10:
                #ends game when plane hits boundary of screen
                run = False
            #plane movements
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    plane.moving_up = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    plane.moving_up = False

        clock.tick(60)
        pygame.display.set_caption(f"Plane Game {clock.get_fps():.0f}")
        #score on screen
        img = font.render(f"Score: {score}", True, (15, 10, 10))
        screen.blit(img, (20, 20))

        #high score listed below current game score
        #file for high score
        high_score = "highscore.txt"
        #read high score file for score
        dir = path.dirname(__file__)
        with open(path.join(dir, high_score), 'r') as f:
             highscore = int(f.read())

        #save highscore in file
        if score > highscore:
            highscore = score
            with open(path.join(dir, high_score), 'w') as f:
                f.write(str(score))
        #prints high score on screen
        high_score = font.render(f"High score: {highscore}", True, (15, 10, 10))
        screen.blit(high_score, (20, 40))

        pygame.display.update()

#options button on home screen
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        #fill in screen with a light blue color
        screen.fill("light blue")
        #text on the screen
        OPTIONS_TEXT = get_font(20).render(" play with up arrow key ", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(250, 200))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        #button to go back to main menu
        OPTIONS_BACK = Button(image=None, pos=(250, 300),
                              text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")
        #change button color when hovering
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
        #button creation
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
        #button actions
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


#Run game
while True:
    main_menu()

    #update screen
    pygame.display.flip()
