import pygame
pygame.init()
testmode = True

FPS = 100
clock = pygame.time.Clock()
SCREENWIDTH = 800
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)



blue = (127, 255, 212)
purple = (180, 182, 227)
pink = (255, 103, 180)
yellow = (255, 252, 197)
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

pea = pygame.image.load("img/pea.png")
pearect = pygame.Rect(650, 80, 64, 64)
peaon = True

pufferRight = pygame.image.load("img/puffer.png")
puffer = pufferRight
pufferrect = pygame.Rect(193, 442, 64, 64)

pufferleft = pygame.image.load("img/pufferleft.png")

sharkleft = pygame.image.load('img/shark.png')
shark = sharkleft
sharkrect = pygame.Rect(400, 100, 64, 64)

sharkright = pygame.image.load("img/sharkright.png")

squid = pygame.image.load('img/squid.png')
squidrect = pygame.Rect(602, 123, 64, 64)
squidOnCouch = False

manta = pygame.image.load('img/manta.png')
mantarect = pygame.Rect(111, 121, 64, 64)
mantaOnCouch = False

seaweedrect2 = pygame.Rect(111, 321, 64, 64)

sofa = pygame.image.load('img/sofa.png')
sofarect = pygame.Rect(100, 450, 300, 143)

fruitnumstart = 2
fruitnum = fruitnumstart

friendnumstart = 2
friendnum = friendnumstart

cupcake = pygame.image.load("img/cupcake.png")
cupcakerect = pygame.Rect(400, 173, 64, 64)

seaweed = pygame.image.load('img/seaweed.png')
seaweedrect = pygame.Rect(301, 123, 64, 72)

fonts = pygame.font.Font("font/animeace2_ital.ttf", 18)
winningFont = pygame.font.Font("font/animeace2_bld.ttf", 72)
playagainsurface = fonts.render("Play Again", False, white)
playagainrect = playagainsurface.get_rect(left=350, top=375)

winsurface = winningFont.render("You Won!", False, white)

quitsurface = fonts.render("Quit", False, white)
quitrect = quitsurface.get_rect(left=370, top=425)
speed = 4
lspeed = 1
sspeed = 1
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
                    speed = 4
                    leorect.center = (700, 321)
                    pineappleon = True
                    peaon = True
                    fruitnum = fruitnumstart
                    friendnum = friendnumstart
                    level = 1
                    print("going to level ", level)
                if quitrect.collidepoint(mousepos):
                    gameon = False
            if level == 200:
                if playagainrect.collidepoint(mousepos):
                    guffyrect.center = (100, 100)
                    leorect.center = (700, 321)
                    pineappleon = True
                    peaon = True
                    fruitnum = fruitnumstart
                    friendnum = friendnumstart
                    pufferrect.center = (193, 442)
                    sharkrect.center = (400, 100)
                    squidrect.center = (602, 123)
                    mantarect.center = (111, 121)
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

        if not testmode:
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

        if peaon:
            if guffyrect.colliderect(pearect):
                speed = 5
                peaon = False
                fruitnum = fruitnum - 1
        if peaon:
            screen.blit(pea, pearect)

        if guffyrect.colliderect(cupcakerect):
            speed = 2

        # go to game over screen
        if guffyrect.colliderect(leorect) and level == 1:
            screen.fill(pink)
            gameoversurface = fonts.render("Game Over", False, white)
            screen.blit(gameoversurface, (350, 302))
            screen.blit(playagainsurface, playagainrect)
            screen.blit(quitsurface, quitrect)
            level = 100

        if fruitnum == 0:
            level = 2
            print("going to level ", level)
            direction = "stop"

    if level == 2:
        "Print I'm at level 2"
        screen.fill(purple)
        screen.blit(sofa, sofarect)
        screen.blit(puffer, pufferrect)
        screen.blit(manta, mantarect)
        screen.blit(squid, squidrect)
        screen.blit(shark, sharkrect)
        screen.blit(seaweed, seaweedrect)
        screen.blit(rightarrow, rightarrow_rect)
        screen.blit(larrow, larrow_rect)
        screen.blit(uarrow, uarrow_rect)
        screen.blit(darrow, darrow_rect)
        screen.blit(seaweed, seaweedrect2)
        
    

        if direction == "right":
            pufferrect.centerx = pufferrect.centerx + speed
            puffer = pufferRight
        if direction == "left":
            puffer = pufferleft
            pufferrect.centerx = pufferrect.centerx - speed
        if direction == "up":
            pufferrect.centery = pufferrect.centery - speed
        if direction == "down":
            pufferrect.centery = pufferrect.centery + speed

        if pufferrect.right > 800:
            direction = "left"
        if pufferrect.left < 0:
            direction = "right"
        if pufferrect.top < 0:
            direction = "down"
        if pufferrect.bottom > 600:
            direction = "up"

        if not testmode:
            if pufferrect.centerx > sharkrect.centerx:
                sharkrect.centerx = sharkrect.centerx + sspeed
                shark = sharkright
            if pufferrect.centerx < sharkrect.centerx:
                sharkrect.centerx = sharkrect.centerx - sspeed
                shark = sharkleft
            if pufferrect.centery > sharkrect.centery:
                sharkrect.centery = sharkrect.centery + sspeed
            if pufferrect.centery < sharkrect.centery:
                sharkrect.centery = sharkrect.centery - sspeed

        if pufferrect.colliderect(sharkrect):
            screen.fill(pink)
            gameoversurface = fonts.render("Game Over", False, white)
            screen.blit(gameoversurface, (350, 302))
            screen.blit(playagainsurface, playagainrect)
            screen.blit(quitsurface, quitrect)
            level = 100
        
        if pufferrect.colliderect(seaweedrect):
            speed = 1
        
        if pufferrect.colliderect(seaweedrect2):
            speed = 1

        if pufferrect.colliderect(squidrect):
            squidrect.centerx = 209
            squidrect.centery = 500
            if not squidOnCouch:
                speed = 4
                friendnum = friendnum - 1
            squidOnCouch = True

        if pufferrect.colliderect(mantarect):
            mantarect.centerx = 275
            mantarect.centery = 500
            if not mantaOnCouch:
                speed = 4
                friendnum = friendnum - 1
            mantaOnCouch = True

    
        if friendnum <= 0:
            screen.fill(yellow)
            screen.blit(winsurface, (200, 100))
            screen.blit(playagainsurface, playagainrect)
            screen.blit(quitsurface, quitrect)
            sspeed = 0
            level = 200



        
    clock.tick(FPS)
    pygame.display.update()
