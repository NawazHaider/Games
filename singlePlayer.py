#! python3
# singlePlayer.py - a module for single player mode of Car Race

import pygame, os, time
import carClass
pygame.init()

# check if level file exists
if not os.path.exists('passed levels.txt'):
    pass_lvl_file = open('passed levels.txt', 'w')
    pass_lvl_file.write('0')
    pass_lvl = 0

# open and read passed levels
else:
    pass_lvl_file = open('passed levels.txt', 'r')
    pass_lvl = int(pass_lvl_file.read())

# mode specific variables
clock = pygame.time.Clock()
fps = 100
screen_w = 1000
screen_h = 700

lvl_w = 100
lvl_h = 100
car_w = 70
car_h = 140

# car images
car1 = pygame.image.load('car1.png')
car1 = pygame.transform.scale(car1, (car_w, car_h))

car2 = pygame.image.load('car2.png')
car2 = pygame.transform.scale(car2, (car_w, car_h))

car3 = pygame.image.load('car3.png')
car3 = pygame.transform.scale(car3, (car_w, car_h))

carList = [car1, car2, car3]

# function for displaying text
font = pygame.font.Font(None, 80)
def displayText(gameWindow, text, colour, xy):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, xy)

# funtion for single player mode
def singlePl_homescreen(gameWindow, background):
    # load images
    level_bg = pygame.image.load('level_bg.png')
    level_bg = pygame.transform.scale(level_bg, (screen_w, screen_h)).convert_alpha()

    lock = pygame.image.load('lock.png')
    lock = pygame.transform.scale(lock, (lvl_w, lvl_h)).convert_alpha()

    boxIm = pygame.image.load('lvl_box.png')
    boxIm = pygame.transform.scale(boxIm, (lvl_w-20, lvl_h-20)).convert_alpha()

    # loop specific variables
    end = False
    pass_lvl_xy = []
    level = 0

    # game loop
    while not end:
        # check the events
        for event in pygame.event.get():
            # quit if the user wants
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end = True

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.BUTTON_LEFT:
                pos = pygame.mouse.get_pos()

                # check player has choosed which level
                for x, y in pass_lvl_xy:
                    if pos[0] >= x and pos[0] <= x + (lvl_w-20):
                        if pos[1] >= y and pos[1] <= y + (lvl_h-20):
                            
                            i = 0
                            for lx, ly in pass_lvl_xy:
                                if x == lx and y == ly:
                                    level = i + 1
                                i += 1
                            singlePl_game(gameWindow)

        # display the background
        gameWindow.blit(level_bg, (0, 0))
        carClass.chooseCar(gameWindow, singleP=True)

        # display the passed levels
        lvl_x = 70
        lvl_y = 200

        for i in range(pass_lvl):
            gameWindow.blit(boxIm, (lvl_x, lvl_y))
            displayText(gameWindow, str(i+1), (0, 0, 0), (lvl_x + 10, lvl_y+15))
            if len(pass_lvl_xy) < pass_lvl:
                pass_lvl_xy.append([lvl_x, lvl_y])

            lvl_x += 150
            if lvl_x >= screen_w-100:
                lvl_y += 100
                lvl_x = 70

        # display the locked levels
        for i in range(30 - pass_lvl):
            gameWindow.blit(lock, (lvl_x, lvl_y))
            lvl_x += 150
            if lvl_x >= screen_w-100:
                lvl_y += 100
                lvl_x = 70

        # update the window
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

# function for singleplayer game
def singlePl_game(gameWindow):
    # load images
    track = pygame.image.load('track.png')
    track = pygame.transform.scale(track, (screen_w, screen_h)).convert_alpha()

    count1 = pygame.image.load('count1.png')
    count2 = pygame.image.load('count2.png')
    count3 = pygame.image.load('count3.png')
    countGo = pygame.image.load('countGo.png')
    count = [count3, count2, count1, countGo]

    lock = pygame.image.load('lock.png')
    lock = pygame.transform.scale(lock, (lvl_w, lvl_h)).convert_alpha()

    # mode specific variables
    end = False
    car_x = 460
    car_y = 500
    num = -1
    track_y = 0
    tracks = [[0, track_y]]
    addTrack = True

    car = carClass.player_car(car_x, car_y, car1)

    # make an event for countdown
    countdown = pygame.USEREVENT + 1
    pygame.time.set_timer(countdown, 1100)
    countTime = time.time()

    # make an event for car acceleration
    accel = pygame.USEREVENT + 1
    pygame.time.set_timer(accel, 1000)

    while not end:
        # loop specific variables
        startCount = False
        
        # move the car forward
        for track_xy in tracks:
            if car.moveForward:
                track_xy[1] += car.carVel

            # display the background
            gameWindow.blit(track, track_xy)

        # check the events
        for event in pygame.event.get():

            # quit if the user wants
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end = True
                
                # check the pressed key
                if event.key == pygame.K_w and time.time() - countTime > 5:
                    car.moveForward = True
                    car.acc = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    car.acc = False

            # accerlerate the car
            if event.type == accel:
                car.accCar()

        # start countdown
            if event.type == countdown:
                startCount = True
                num += 1

        if startCount and num <= 3:
            gameWindow.blit(count[num], ((screen_w/2) - 70, (screen_h/2) - 50))
        pygame.time.wait(200)

        # check y level of track
        if tracks[0][1] >= 0 and addTrack:
            tracks.append([0, tracks[0][1] - screen_h])
            addTrack = False
        
        # remove tracks which are outside the screen
        if tracks[0][1] > screen_h:
            tracks.remove(tracks[0])
            addTrack = True

        # display the car
        carClass.cars.update(gameWindow)

        # update the window
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()