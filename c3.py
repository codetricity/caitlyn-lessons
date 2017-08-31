import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
gameon = True
while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
    print(pygame.time.get_ticks()/1000)
    pygame.display.update()