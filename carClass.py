#! python3
# carClass.py - this file has several classes and functions for cars controlled by player and computer
import pygame
pygame.init()

# create a sprite group
cars = pygame.sprite.Group()

class player_car(pygame.sprite.Sprite):
    carVel = 0
    carVel2 = 1
    carAcc = 3

    # constructor
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.car_x = x
        self.car_y = y
        self.moveForward = False
        self.carImg = img
        self.t_right = False
        self.t_left = False
        self.acc = False

        # add car to sprite group
        cars.add(self)
    
    # update func
    def update(self, gameWindow):
        # check the velocity of car and change acceleration
        if self.carVel >= 80:
            self.carAcc = 1
        elif self.carVel >= 50:
            self.carAcc = 2
        else:
            self.carAcc = 3

        # change y co ordinates when accelerated
        if self.car_y > 400 and self.acc:
            self.car_y -= self.carVel2

        gameWindow.blit(self.carImg, (self.car_x, self.car_y))
    
    # func for car acceleration
    def accCar(self):
        if self.acc and self.carVel < 90:
            self.carVel += self.carAcc

        elif self.carVel > 0:
            self.carVel -= self.carAcc + 1
            if self.car_y <= 520:
                self.car_y += 7

        else:
            self.carVel = 0
            self.moveForward = False

# function for displaying text
font = pygame.font.Font(None, 60)
def displayText(gameWindow, text, colour, xy):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, xy)

# function for choosing car for both single and multi player mode
def chooseCar(gameWindow, singleP = False, multiP = False):
    end = False
    n = 0

    # load images
    cars = []
    for i in range(1, 14):
        car = pygame.image.load(f'car{str(i)}.png')
        car = pygame.transform.scale(car, (70, 140))
        cars.append(car)

    boxIm = pygame.image.load('lvl_box.png')
    boxIm = pygame.transform.scale(boxIm, (70, 140))

    clock = pygame.time.Clock()
    fps = 20

    # loop
    if singleP:
        while not end:
            # loop variables
            x = 45
            y = 250
            car_xy = [[x, y]]

            # check the events
            for event in pygame.event.get():

                # quit if the user wants
                if event.type == pygame.QUIT:
                    end = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        end = True
                    
                    # change co-ordiantes of box when key pressed
                    if event.key == pygame.K_RIGHT:
                        n += 1

            # display text
            txt = 'Choose  a  car  by  arrow  keys'
            displayText(gameWindow, txt, (255, 255, 255), (200, 170))

            # display all car images
            for i in range(13):
                if i == 8:
                    y += 180
                    x = 45
                x += 120
                car_xy.append([x, y])
            print(car_xy)

            # display a box
            gameWindow.blit(boxIm, (car_xy[n]))

            for i in range(len(car_xy)):
                print(car_xy[n])
                gameWindow.blit(cars[i], car_xy[n])

            # update the window
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()
        quit()

    elif multiP:
        pass