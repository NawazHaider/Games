#! python3
# carRace.py - game of car racing

import pygame, time, singlePlayer
from PIL import ImageColor
pygame.init()

# game variables
screen_w = 1000
screen_h = 700
loading_x = (screen_w - 614) / 2
loading_y = (screen_h - 119) - 150

font = pygame.font.Font(None, 70)
txt_x = 210
txt_y = 300

clock = pygame.time.Clock()
fps = 20

window = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Car Race')

# colours
green = ImageColor.getcolor('green', 'RGBA')

# load the background image
bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (screen_w, screen_h)).convert_alpha()

# load the loading screen
loadingIm = pygame.image.load('loading.png').convert_alpha()

# load the gamemode images
chooseGm = pygame.image.load('gamemode.png').convert_alpha()
singleIm = pygame.image.load('singleplayer.png').convert_alpha()
multiIm = pygame.image.load('multiplayer.png').convert_alpha()

# function to plot rectangle
def plot_rect(gameWindow,colour , x, y, l, b):
    pygame.draw.rect(window, colour,  (x, y, l, b))

# function of homescreen
def homescreen():
    # loop specific variables
    end = False
    loading_l = 10
    add_l = pygame.USEREVENT + 1
    pygame.time.set_timer(add_l, 100)
    load_time = time.time()

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

            # increase the length of loading_l
            if event.type == add_l and loading_l < loading_x + 387:
                loading_l += 30
            
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.BUTTON_LEFT:
                pos = pygame.mouse.get_pos()

                # check the x and y position for singleplayer
                if pos[0] >= txt_x-50 and pos[0] <= (txt_x-50) + 284:
                    if pos[1] >= txt_y+120 and pos[1] <= (txt_y+120) + 59:
                        singlePlayer.singlePl_homescreen(window, bg)

                # check the x and y position for multiplayer
                if pos[0] >= txt_x+380 and pos[0] <= (txt_x+380) + 284:
                    if pos[1] >= txt_y+120 and pos[1] <= (txt_y+120) + 59:
                        print('multiplayer')

        # display bakground and loading screen
        window.blit(bg, (0, 0))
        if not time.time() - load_time >= 3:
            window.blit(loadingIm, (loading_x, loading_y))
            plot_rect(window, green, loading_x + 9, loading_y + 8, loading_l, 42)
        
        else:
            # create a box for content
            plot_rect(window, (255, 255, 255), 115, 270, 800, 250)

            # display a text after loading
            window.blit(chooseGm, (txt_x, txt_y))

            # display the gamemode images
            window.blit(singleIm, (txt_x-50, txt_y+120))
            window.blit(multiIm,  (txt_x+380, txt_y+120))

        # update the window
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

homescreen()