import sys
import pygame
import time
import random

pygame.init()
winbackgrd = (8, 24, 45)  # rgb color code for black
White = (255, 255, 255)
yellow = (57, 58, 1)
blue = (0, 0, 45)
maroon = (73, 4, 17)
bright_yellow = (102, 104, 4)
bright_blue = (2, 2, 130)
bright_maroon = (122, 7, 29)
black = (0, 0, 0)
display_width = 800
display_height = 600
gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("SPACE INVADER")
clock = pygame.time.Clock()
rocketimg = pygame.image.load('rocket.png')
backgroundimg = pygame.image.load("background.jpg")
backgroundbh = pygame.image.load("bh.png")
backgroundss = pygame.image.load("ss.png")
backgroundas1 = pygame.image.load("asteroid1.png")
backgroundas2 = pygame.image.load("asteroid2.png")
backgroundas3 = pygame.image.load("asteroid3.png")
backgroundas4 = pygame.image.load("asteroid4.png")
intro_back = pygame.image.load("introback.jpg")
instruct_back = pygame.image.load("instructback.png")
laser_pic = pygame.image.load("laser.png")
blast = pygame.image.load("blast.png")
rocket_width = 100
rocket_height = 100
pause = False
last_loc_laserx = 0
last_loc_lasery = 0


def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(intro_back, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("SPACE INVADER", largetext)
        TextRect.center = (400, 100)
        gamedisplay.blit(TextSurf, TextRect)
        button("START", 150, 520, 100, 50, blue, bright_blue, "play")
        button("QUIT", 550, 520, 100, 50, maroon, bright_maroon, "quit")
        button("INSTRUCTION", 300, 520, 200, 50, yellow, bright_yellow, "intro")
        pygame.display.update()
        clock.tick(50)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplay, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplay.blit(textsurf, textrect)


def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(instruct_back, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = text_objects("This is a rocket game in which you need dodge the coming asteroids",
                                          smalltext)
        textRect.center = ((350), (200))
        TextSurf, TextRect = text_objects("INSTRUCTION", largetext)
        TextRect.center = ((400), (100))
        gamedisplay.blit(TextSurf, TextRect)
        gamedisplay.blit(textSurf, textRect)
        stextSurf, stextRect = text_objects("ARROW LEFT : LEFT TURN", smalltext)
        stextRect.center = ((150), (400))
        hTextSurf, hTextRect = text_objects("ARROW RIGHT : RIGHT TURN", smalltext)
        hTextRect.center = ((150), (450))
        atextSurf, atextRect = text_objects("A : ACCELERATOR", smalltext)
        atextRect.center = ((150), (500))
        rtextSurf, rtextRect = text_objects("B : BRAKE ", smalltext)
        rtextRect.center = ((150), (550))
        ptextSurf, ptextRect = text_objects("P : PAUSE  ", smalltext)
        ptextRect.center = ((150), (350))
        sTextSurf, sTextRect = text_objects("CONTROLS", mediumtext)
        sTextRect.center = ((350), (300))
        gamedisplay.blit(sTextSurf, sTextRect)
        gamedisplay.blit(stextSurf, stextRect)
        gamedisplay.blit(hTextSurf, hTextRect)
        gamedisplay.blit(atextSurf, atextRect)
        gamedisplay.blit(rtextSurf, rtextRect)
        gamedisplay.blit(ptextSurf, ptextRect)
        button("BACK", 600, 450, 100, 50, maroon, bright_maroon, "menu")
        pygame.display.update()
        clock.tick(30)


def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(instruct_back, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("PAUSED", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf, TextRect)
        button("CONTINUE", 150, 450, 150, 50, yellow, bright_yellow, "unpause")
        button("RESTART", 350, 450, 150, 50, blue, bright_blue, "play")
        button("MAIN MENU", 550, 450, 200, 50, maroon, bright_maroon, "menu")
        pygame.display.update()
        clock.tick(30)


def unpaused():
    global pause
    pause = False


def countdown_background():
    font = pygame.font.SysFont(None, 25)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    gamedisplay.blit(backgroundimg, (0, 0))
    gamedisplay.blit(backgroundbh, (0, 0))
    gamedisplay.blit(backgroundss, (0, 500))
    gamedisplay.blit(rocketimg, (x, y))
    text = font.render("DODGED: 0", True, White)
    score = font.render("SCORE: 0", True, White)
    gamedisplay.blit(text, (0, 50))
    gamedisplay.blit(score, (0, 30))
    button("PAUSE", 650, 0, 150, 50, blue, bright_blue, "pause")


def countdown():
    countdown = True

    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.fill(winbackgrd)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("3", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplay.fill(winbackgrd)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("2", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplay.fill(winbackgrd)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("1", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplay.fill(winbackgrd)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("GO!!!", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        game_loop()


def laser_func(x, y):
    while (y > 0):
        gamedisplay.blit(laser_pic, (x, y))
        y -= 50
    return x, y


# obstacle
def obstacle(obstacle_start_x, obstacle_start_y, obs):
    if obs == 0:
        obs_pic = pygame.image.load("asteroid1.png")
    elif obs == 1:
        obs_pic = pygame.image.load("asteroid2.png")
    elif obs == 2:
        obs_pic = pygame.image.load("asteroid3.png")
    elif obs == 3:
        obs_pic = pygame.image.load("asteroid4.png")
    elif obs == 4:
        obs_pic = pygame.image.load("asteroid5.png")
    elif obs == 5:
        obs_pic = pygame.image.load("asteroid6.png")
    elif obs == 6:
        obs_pic = pygame.image.load("asteroid7.png")
    elif obs == 7:
        obs_pic = pygame.image.load("asteroid8.png")
    elif obs == 8:
        obs_pic = pygame.image.load("asteroid9.png")
    elif obs == 9:
        obs_pic = pygame.image.load("asteroid10.png")
    gamedisplay.blit(obs_pic, (obstacle_start_x, obstacle_start_y))


# score function
def score_system(as_passed, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("PASSED:" + str(as_passed), True, White)
    score = font.render("SCORE:" + str(score), True, White)
    gamedisplay.blit(text, (0, 200))
    gamedisplay.blit(score, (0, 170))


# backround images
def back():
    gamedisplay.blit(backgroundimg, (0, 0))
    gamedisplay.blit(backgroundbh, (0, 0))
    gamedisplay.blit(backgroundss, (0, 500))


def text_objects(text, font):
    textsurface = font.render(text, True, White)
    return textsurface, textsurface.get_rect()


# to display any kind of message
def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    gamedisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


# if the rocket went out of the screen
def wentoutofthescreen():
    message_display("SPACESHIP LOST")


# putting rockeet on the screen
def rocket(x, y):
    gamedisplay.blit(rocketimg, (x, y))  # puts the imah=ge on the window with x and y coordinates


# game coding
def game_loop():
    # starting location of the rocket
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    global pause

    # for moving the rocket
    x_change = 0
    y_change = 0

    # obstacle
    obstacle_speed = 5
    obs = 0
    obstacle_y_change = 0
    obstacle_start_x = random.randrange(200, (display_width - 200))
    obstacle_start_y = -750
    obstacle_width = 100
    obstacle_height = 100

    laser_width = 50
    laser_height = 50

    laser_speed = 9

    as_passed = 0
    level = 0
    score = 0
    blastflag = 0
    laser = False

    # for closing the window when cross button pressed
    bumped = False
    while not bumped:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # if we press the yellow cross button on top of window loop  game will stop
                pygame.quit()
                quit()

            # moving the rocket
            if event.type == pygame.KEYDOWN:  # that is when the key is pressed
                if event.key == pygame.K_LEFT:
                    x_change = -5  # changing coordinates
                if event.key == pygame.K_RIGHT:
                    x_change = 5  # changing coordinates
                if event.key == pygame.K_UP:
                    y_change = -5  # changing coordinates
                if event.key == pygame.K_DOWN:
                    y_change = 5  # changing coordinates
                # acceleration and deceleration
                if event.key == pygame.K_a:
                    obstacle_speed += 0.3
                if event.key == pygame.K_d:
                    obstacle_speed -= 0.3
                if event.key == pygame.K_SPACE:
                    laser = True

            # that is when the key i released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                if event.key == pygame.K_SPACE:
                    laser = False

        y += y_change  # applying changes to x coordinates
        x += x_change  # applying changes to x coordinates
        pause = True
        gamedisplay.fill(winbackgrd)
        laserx = x + 28
        lasery = y - 33
        back()

        obstacle_start_y -= (obstacle_speed / 4)
        if blastflag==0:
            obstacle(obstacle_start_x, obstacle_start_y, obs)
        obstacle_start_y += obstacle_speed
        last_loc_laserx=0
        rocket(x, y)  # putting image on the screen
        if laser == True:
            #print(obstacle_start_x)
            last_loc_laserx, last_loclasery = laser_func(laserx, lasery)
            #print(last_loc_laserx)#last_loc_lasery)
        score_system(as_passed, score)

        if x > 800 - rocket_width or x < 0:
            wentoutofthescreen()
        if y > 600 - rocket_height or y < 0:
            wentoutofthescreen()

        #if x > display_width - (rocket_width + 110) or x < 110:
         #   wentoutofthescreen()

        if  last_loc_laserx>obstacle_start_x+30 or last_loc_laserx>obstacle_start_x-30:
            gamedisplay.blit(blast,(last_loc_laserx-50,obstacle_start_y -30))
            blastflag=1
            #score=score+10
 
        if obstacle_start_y > display_height or blastflag==1:
            obstacle_start_y = 0 - obstacle_height
            obstacle_start_x = random.randrange(200, (display_width - 200))
            obs = random.randrange(0, 9)

            # counting no. of asteroid passed and giving score
            as_passed = as_passed + 1
            #print(as_passed)
            score = score + 5
            #print(score)
            
            # increasing level if 10 as passed
            if int(as_passed) % 10 == 0:
                level = level + 1
                obstacle_speed += 1
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("LEVEL" + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplay.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obstacle_start_y + obstacle_height and blastflag==0:
            if (x > obstacle_start_x and x < (obstacle_start_x + obstacle_width)) or (
                    (x + rocket_width) > (obstacle_start_x) and (x + rocket_width) < (
                    obstacle_start_x + obstacle_width)):
                wentoutofthescreen()
        blastflag=0
        button("pause", 650, 0, 150, 50, blue, bright_blue, "pause")
        #score_system(as_passed, score)
        pygame.display.update()  # updating the window
        clock.tick(60)
    # this all(calling) code inside while loop but outside for loop


intro_loop()
game_loop()
pygame.quit()
quit()
