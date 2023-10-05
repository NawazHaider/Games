#! python3
# carRace.py - game of car racing

import pygame, time
from PIL import ImageColor
pygame.init()

# game variables
screen_w = 1000
screen_h = 700
car_w = 100
car_h = 50
loading_x = (screen_w - 614) / 2
loading_y = (screen_h - 119) - 150
font = pygame.font.Font(None, 50)

clock = pygame.time.Clock()
fps = 50

window = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Car Race')

# colours
green = ImageColor.getcolor('green', 'RGBA')

# load the background image
bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (screen_w, screen_h))

# load the car images
carIm = pygame.image.load('car3.png')
carIm = pygame.transform.scale(carIm, (car_w, car_h)).convert_alpha()

# load the loading screen
loadingIm = pygame.image.load('loading.png').convert_alpha()

# function to display text
def display_text(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    window.blit(screen_text, [x, y])

# function to plot rectangle
def plot_rect(gameWindow,colour , x, y, l, b):
    pygame.draw.rect(window, colour,  (x, y, l, b))

# function of game loop
def homescreen():
    # loop specific variables
    end = False
    loading_l = 10
    add_l = pygame.USEREVENT + 1
    pygame.time.set_timer(add_l, 100)
    load_time = time.time()

    # game loop
    while not end:
        # display bakground and loading screen
        window.blit(bg, (0, 0))
        if not time.time() - load_time >= 4:
            window.blit(loadingIm, (loading_x, loading_y))
            plot_rect(window, green, loading_x + 9, loading_y + 8, loading_l, 42)

        # check the events
        for event in pygame.event.get():

            # quit if the user wants
            if event.type == pygame.QUIT:
                end = True

            # increase the length of loading_l
            if event.type == add_l and loading_l <+ loading_x + 387:
                loading_l += 30
        
        # display a text after loading

        # display the gamemode images

        # update the window
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

homescreen()