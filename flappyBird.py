import pygame, random, os
from pygame import mixer
pygame.init()

# check if score.txt exists
if not os.path.exists('score.txt'):
    hsFile = open('score.txt', 'w')
    hsFile.write('0')
    hsFile.close()

# game variables
screen_width = 400
screen_height = 400

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()
fps = 75
gamemode = ''

# load the bird image
birdImg = pygame.image.load('flappybird.png')
birdImg = pygame.transform.scale(birdImg, (50, 35)).convert_alpha()
bird_w = 40
bird_l = 30

# load the background image
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (screen_width, screen_height)).convert_alpha()

# load the pipe images
pipe1 = pygame.image.load('pipe1.png').convert_alpha()
pipe2 = pygame.image.load('pipe2.png').convert_alpha()
pipe_y = 0
pipe_w = 45
pipe_l = 272

# load the homescreen image
homeIm = pygame.image.load('homescreen.jpg')
homeIm = pygame.transform.scale(homeIm, (screen_width, screen_height)).convert_alpha()

# load the info page
infoIm =  pygame.image.load('info.jpg')
infoIm = pygame.transform.scale(infoIm, (screen_width, screen_height)).convert_alpha()

# load the endscreen
endIm = pygame.image.load('endscreen.jpg')
endIm = pygame.transform.scale(endIm, (screen_width, screen_height)).convert_alpha()

# load the number images for score
n_width = 30
n_height = 30

zero = pygame.image.load('0.png')
zero = pygame.transform.scale(zero, (n_width, n_height)).convert_alpha()

one = pygame.image.load('1.png')
one = pygame.transform.scale(one, (n_width, n_height)).convert_alpha()

two = pygame.image.load('2.png')
two = pygame.transform.scale(two, (n_width, n_height)).convert_alpha()

three = pygame.image.load('3.png')   
three = pygame.transform.scale(three, (n_width, n_height)).convert_alpha()

four = pygame.image.load('4.png')
four = pygame.transform.scale(four, (n_width, n_height)).convert_alpha()

five = pygame.image.load('5.png')
five = pygame.transform.scale(five, (n_width, n_height)).convert_alpha()

six = pygame.image.load('6.png')
six = pygame.transform.scale(six, (n_width, n_height)).convert_alpha()

seven = pygame.image.load('7.png')
seven = pygame.transform.scale(seven, (n_width, n_height)).convert_alpha()

eight = pygame.image.load('8.png')
eight = pygame.transform.scale(eight, (n_width, n_height)).convert_alpha()

nine = pygame.image.load('9.png')
nine = pygame.transform.scale(nine, (n_width, n_height)).convert_alpha()

num = [zero, one, two, three, four, five, six, seven, eight, nine]

# read the high score
hsFile = open('score.txt', 'r')
highscore = hsFile.read()

# load the game sounds
flapping = mixer.Sound('flapping.wav')
point = mixer.Sound('point.wav')
out = mixer.Sound('out.wav')

# functions to display the pipes
def plot_pipe1(xyList):
    for x, y in xyList:
        window.blit(pipe1 , (x, y))

def plot_pipe2(xyList):
    for x, y in xyList:
        window.blit(pipe2, (x, y))

# function to show score on the screen
def displayScore(gameWindow, score, xy):
    k = 0
    for n in list(str(score)):

        if len(list(str(score))) > 1 and k == 0:
            xy2 = [xy[0] - 35, xy[1]]
            window.blit(num[int(n)], xy2)
            k = 1

        elif len(list(str(score))) > 1 and k == 1:
            window.blit(num[int(n)], xy)
            k = 0
        
        else:
            window.blit(num[int(n)], xy)

# function to check collision of bird
def checkCollision(bird_xy, p_xy1, p_xy2):
    
    # check if the bird touches the ground
    if bird_xy[1] + bird_l > screen_height:
        pygame.time.delay(300)
        mixer.music.pause()
        mixer.music.load('out.wav')
        mixer.music.play()
        return True

    # check if the bird touches a pipe
    for px, py in p_xy1:
        if px >= bird_xy[0] and px <= bird_xy[0] + bird_w:
            if bird_xy[1] + bird_l > py:
                pygame.time.delay(300)
                mixer.music.pause()
                mixer.music.load('out.wav')
                mixer.music.play()
                return True

    for px, py in p_xy2:
        if px >= bird_xy[0] and px <= bird_xy[0] + bird_w:
            if bird_xy[1] < py + pipe_l:
                pygame.time.delay(300)
                mixer.music.pause()
                mixer.music.load('out.wav')
                mixer.music.play()
                return True

# funcion to display info page
def info():
    # loop specific variables
    end = False

    while not end:
        window.blit(infoIm, (0, 0))

        for event in pygame.event.get():

            # quit if the user wants
            if event.type == pygame.QUIT:
                end = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    homescreen()

        # update the window
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

# function to display homescreen
def homescreen():
    # loop specific variables
    end = False
    hsFile = open('score.txt', 'r')
    highscore = hsFile.read()
    hsFile.close()

    while not end:
        window.blit(homeIm, (0, 0))
        displayScore(window, highscore, (255, 205))

        for event in pygame.event.get():

            # quit if the user wants
            if event.type == pygame.QUIT:
                end = True

            if event.type == pygame.KEYDOWN:

                # set the gamemode accordingly
                if event.key == pygame.K_e:
                    gamemode = 'easy'
                    gameLoop(gamemode)

                if event.key == pygame.K_m:
                    gamemode = 'medium'
                    gameLoop(gamemode)

                if event.key == pygame.K_h:
                    gamemode = 'hard'
                    gameLoop(gamemode)

                if event.key == pygame.K_i:
                    info()

        # update the window
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

def endscreen(sc):
    # loop specific variables
    end = False
    hsFile = open('score.txt', 'r')
    highscore = hsFile.read()
    hsFile.close()

    while not end:
        window.blit(endIm, (0, 0))
        displayScore(window, highscore, (320, 220))
        displayScore(window, sc, (320, 320))

        for event in pygame.event.get():

            # quit if the user wants
            if event.type == pygame.QUIT:
                end = True

            # restart the game    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    homescreen()

        # update the window
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

# function for playing the game
def gameLoop(gm):
    # loop specific variables
    end = False
    bird_x = 80
    bird_y = 200
    init_vel = 1.5
    vel_y = 0
    bird_speed = -40
    score = 0
    score_xy = [(screen_width/2) - 5, screen_height/22]
    gameover = False

    vert_pipe_gap = 400
    hori_pipe_gap = 200
    pipe_xy = [[screen_width - 50, random.randint(150, screen_height-40)]]
    pipe_xy2 = [[screen_width -200, pipe_xy[0][1]-vert_pipe_gap]]
    pipe_vel_x = 1

    # read the high score
    hsFile = open('score.txt', 'r')
    highscore = hsFile.read()
    hsFile.close()

    # game loop
    while not end:
        window.blit(bg, (0, 0))

        if gameover:
            endscreen(score)

        # check the events
        for event in pygame.event.get():

            # close the window if user wants
            if event.type == pygame.QUIT:
                end = True

            # change the velocity of bird when space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flapping.play()
                    if bird_y+50 < 40:
                        vel_y = 0
                    else:
                        vel_y = bird_speed
                
                if event.key == pygame.K_n:
                    score += 1

        # change the y co-ordinates of the bird
        bird_y += vel_y
        window.blit(birdImg, (bird_x, bird_y))
        vel_y = init_vel

        # close the game when the bird touches the ground or collides with a pipe
        gameover = checkCollision((bird_x, bird_y), pipe_xy, pipe_xy2)

        # change the x co-ordinates of pipes
        n = 0
        for x, y in pipe_xy:
            x -= pipe_vel_x
            pipe_xy[n][0] = x
            pipe_xy2[n][0] = x
            n += 1
        plot_pipe1(pipe_xy)
        plot_pipe2(pipe_xy2)

        # remove the pipe if it has reached the end of screen
        if pipe_xy[0][0] < -50:
            del pipe_xy[0]
            del pipe_xy2[0]
        
        # plot a new pipe if the pipe reches a certain co-ordinates
        if pipe_xy[-1][0] < hori_pipe_gap:
            pipe_x = screen_width
            pipe_y = random.randint(150, screen_height-40)
            pipe_xy.append([pipe_x, pipe_y])
            pipe_xy2.append([pipe_x, pipe_y-vert_pipe_gap])

        # add score when bird crosses a pipe
        if bird_x == round(pipe_xy[0][0]+10):
            score += 1
            point.play()
        
        # display the score
        displayScore(window, score, score_xy)

        # write the score if it is greater than highscore
        if int(highscore) < score:
            highscore = score
            hsFile = open('score.txt', 'w')
            hsFile.write(str(highscore))
            hsFile.close()

        # check the gamemode
        if gm == 'medium':
            if score >= 10 and score <= 25:
                pipe_vel_x = 1.2
            
            elif score > 25 and score <= 50:
                bird_speed = -42
                init_vel = 1.8
                pipe_vel_x = 1.6

            elif score > 50:
                init_vel = 2
                pipe_vel_x = 2

        elif gm == 'hard':
            if score >= 10 and score <= 25:
                pipe_vel_x = 1.2
                vert_pipe_gap = 385
            
            elif score > 25 and score <= 50:
                pipe_vel_x = 1.6
                vert_pipe_gap = 375
                bird_speed = -42
                init_vel = 1.8

            elif score > 50:
                bird_speed = -42
                init_vel = 2
                pipe_vel_x = 2
        
        # update the window
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

# start the game
homescreen()