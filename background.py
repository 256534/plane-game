import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
background = pygame.image.load('images/background.png')

running = True



while running:
    screen.fill((255,255,255))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()