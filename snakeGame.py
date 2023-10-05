#! python3
# snakeGame.py - my first game with pygame

import pygame, random
from PIL import ImageColor
pygame.init()

screen_width = 800
screen_height = 500
clock = pygame.time.Clock()
fps = 50

# game colours
green = (0, 200, 50)
red = ImageColor.getcolor('red', 'RGBA')
black = ImageColor.getcolor('black', 'RGBA')
blue = ImageColor.getcolor('blue', 'RGBA')

# game window
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

font = pygame.font.Font(None, 50)
def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    window.blit(screen_text, [x, y])

def plot_snake(gameWindow, colour, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, colour, (x, y, snake_size, snake_size))

# home screen
def home_screen():
    exit_game = False
    while not exit_game:
        window.fill((200, 50, 250))
        text_screen('Welcome To Snake Game', black, 180, 200)
        text_screen('Press Space Bar To Play', black, 185, 240)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()
    
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

# game loop
def gameLoop():
    # read the high score
    file = open('highscore.txt', 'r')
    highscore = file.read()
    file.close()

    # game variables
    exit_game = False
    score = 0
    game_over = False

    snake_x = 300
    snake_y = 250
    snake_size = 20

    velocity_x = 0
    velocity_y = 0
    init_velocity = 4

    food_x = random.randint(10, screen_width-100)
    food_y = random.randint(10, screen_height-100)

    snake_list = []
    snake_length = 1

    while not exit_game:
        if game_over:
            window.fill(green)
            text_screen('Game Over! Press Enter To Continue', red, 100, 200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()
        
        else:
            window.fill(green)
            text_screen(f'Score: {str(score)} Highscore: {highscore}', red, 5, 5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

                    if event.key == pygame.K_w:
                        snake_length += 50

            if abs(snake_x - food_x) < 18 and abs(snake_y - food_y) < 18:
                score += 10
                food_x = random.randint(10, screen_width-100)
                food_y = random.randint(10, screen_height-100)
                snake_length += 5

            if score > int(highscore):
                highscore = score
                file = open('highscore.txt', 'w')
                file.write(str(highscore))
                file.close()
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]
            
            snake_x += velocity_x
            snake_y += velocity_y

            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            plot_snake(window, black, snake_list, snake_size)
            pygame.draw.rect(window, blue, (food_x, food_y, snake_size, snake_size))
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

home_screen()