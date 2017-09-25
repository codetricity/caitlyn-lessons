import pygame
pygame.init()

FPS = 100
clock = pygame.time.Clock()
size = (800, 600)
screen = pygame.display.set_mode(size)

blue = (127, 255, 212)
purple = (180, 182, 227)
pink = (255, 103, 180)
white = (255, 255, 255)

rightarrow = pygame.image.load('img/arrows/right.png')
rightarrow_rect = pygame.Rect(680, 400, 100, 55)
larrow = pygame.image.load('img/arrows/left.png')
larrow_rect = pygame.Rect(500, 400, 100, 55)
uarrow = pygame.image.load('img/arrows/up.png')
uarrow_rect = pygame.Rect(610, 300, 55, 100)
darrow = pygame.image.load('img/arrows/down.png')
darrow_rect = pygame.Rect(610, 475, 55, 100)

guffy = pygame.image.load("img/giraffe.png")
guffyrect = pygame.Rect(100, 100, 64, 64)

leo = pygame.image.load("img/lion.png")
leorect = pygame.Rect(700, 321, 64, 64)

pineapple = pygame.image.load("img/pineapple.png")
pineapplerect = pygame.Rect(308, 497, 64, 64)
pineappleon = True

puffer = pygame.image.load("img/puffer.png")
pufferrect = pygame.Rect(193, 442, 64, 64)

fruitnumstart = 1
fruitnum = fruitnumstart

cupcake = pygame.image.load("img/cupcake.png")
cupcakerect = pygame.Rect(400, 173, 64, 64)

fonts = pygame.font.Font("font/animeace2_ital.ttf", 18)
playagainsurface = fonts.render("Play Again", False, white)
playagainrect = playagainsurface.get_rect(left=350, top=375)

quitsurface = fonts.render("Quit", False, white)
quitrect = quitsurface.get_rect(left=370, top=425)
speed = 4
lspeed = 2
direction = "up"
level = 1
gameon = True

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if rightarrow_rect.collidepoint(mousepos):
                direction = "right"
            if larrow_rect.collidepoint(mousepos):
                direction = "left"
            if uarrow_rect.collidepoint(mousepos):
                direction = "up"
            if darrow_rect.collidepoint(mousepos):
                direction = 'down'
            if level == 100:
                if playagainrect.collidepoint(mousepos):
                    guffyrect.center = (100, 100)
                    leorect.center = (700, 321)
                    fruitnum = fruitnumstart
                    level = 1
                if quitrect.collidepoint(mousepos):
                    gameon = False
                    
                    

    if level == 1:
        screen.fill(blue)
        screen.blit(rightarrow, rightarrow_rect)
        screen.blit(larrow, larrow_rect)
        screen.blit(uarrow, uarrow_rect)
        screen.blit(darrow, darrow_rect)
        screen.blit(cupcake, cupcakerect)
        screen.blit(guffy, guffyrect)
        screen.blit(leo, leorect)

        if direction == "right":
            guffyrect.centerx = guffyrect.centerx + speed
        if direction == 'left':
            guffyrect.centerx = guffyrect.centerx - speed
        if direction == "up":
            guffyrect.centery = guffyrect.centery - speed
        if direction == 'down':
            guffyrect.centery = guffyrect.centery + speed

        if guffyrect.right > 800:
            direction = "left"
        if guffyrect.left < 0:
            direction = "right"
        if guffyrect.top < 0:
            direction = "down"
        if guffyrect.bottom > 600:
            direction = "up"

        if guffyrect.centerx > leorect.centerx:
            leorect.centerx = leorect.centerx + lspeed
        if guffyrect.centerx < leorect.centerx:
            leorect.centerx = leorect.centerx - lspeed
        if guffyrect.centery < leorect.centery:
            leorect.centery = leorect.centery - lspeed
        if guffyrect.centery > leorect.centery:
            leorect.centery = leorect.centery + lspeed
        
        if pineappleon:
            if guffyrect.colliderect(pineapplerect):
                speed = 5
                pineappleon = False
                fruitnum = fruitnum - 1
        if pineappleon:
            screen.blit(pineapple, pineapplerect)

        if guffyrect.colliderect(cupcakerect):
            speed = 2
        
        if fruitnum == 0:
            level = 2
    
        if guffyrect.colliderect(leorect):
            screen.fill(pink)
            panda = fonts.render("Game Over", False, white)
           
            screen.blit(panda, (350, 302))
            screen.blit(playagainsurface, playagainrect)
            screen.blit(quitsurface, quitrect)
            level = 100


    if level == 2:
        screen.fill(purple)
        screen.blit(puffer, pufferrect)
        pufferrect.centerx = pufferrect.centerx + speed
    clock.tick(FPS)
    pygame.display.update()
