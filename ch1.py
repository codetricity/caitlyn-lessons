import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
fonts = pygame.font.Font("font/animeace2_ital.ttf", 17)
pink = (255, 105, 180)
blue = (123, 231, 235)
salmon = (244, 160, 122)
square = pygame.Rect(243, 421, 24, 24)
direction = 'right'

gameon = True

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False

    screen.fill(blue)

    timernum = pygame.time.get_ticks()/1000
    roundnum = round(timernum, 1)
    timerstr = str(roundnum)
    timersurface = fonts.render("Time:" + timerstr, False, pink)
    screen.blit(timersurface, (20, 20))

    pygame.draw.rect(screen, salmon, square)
   
    if direction == "right":
        square.centerx = square.centerx + 1
    if direction == "left":
        square.centerx = square.centerx - 1

    if square.left > 800:
        direction = "left"
    if square.right < 0:
        direction  = 'right'
    
    pygame.display.update()