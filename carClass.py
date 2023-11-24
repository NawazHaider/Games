#! python3
# carClass.py - this file has several classes and functions for cars controlled by player and computer
import pygame
pygame.init()

# create sprite groups
cars = pygame.sprite.Group()
computerCars = pygame.sprite.Group()

class player_car(pygame.sprite.Sprite):
    carVel2 = 1
    carAcc = 3

    # constructor
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.car_x = x
        self.car_y = y
        self.carImg = img
        self.carVel = 0
        self.moveForward = False
        self.t_right = False
        self.t_left = False
        self.acc = False
        self.carTurnVel = 5
        self.retard = False

        # add car to sprite group
        cars.add(self)
    
    # update func
    def update(self, gameWindow):
        # check the velocity of car and change acceleration
        if self.carVel >= 80:
            self.carAcc = 1
            self.carTurnVel = 10

        elif self.carVel >= 50:
            self.carAcc = 2
            self.carTurnVel = 7

        else:
            self.carAcc = 3
            self.carTurnVel = 5

        # change y co ordinates when accelerated or retarded
        if self.car_y > 400 and self.acc:
            self.car_y -= self.carVel2

        if self.retard and self.car_y < 500:
            self.car_y += 10
            self.carVel -= self.carAcc

        # change x co ordinates when t_left or t_right are true
        if self.t_left and self.car_x > 40:
            self.car_x -= self.carTurnVel
            if self.car_y > 300 and self.acc:
                self.car_y -= self.carTurnVel/3

        if self.t_right and self.car_x + 110 < 1000:
            self.car_x += self.carTurnVel
            if self.car_y > 300 and self.acc:
                self.car_y -= self.carTurnVel/3

        gameWindow.blit(self.carImg, (self.car_x, self.car_y))
    
    # func for car acceleration
    def accCar(self):
        if self.acc and self.carVel < 90:
            self.carVel += self.carAcc

        elif self.carVel > 0:
            self.carVel -= self.carAcc + 1
            if self.car_y <= 500:
                self.car_y += 7

        else:
            self.carVel = 0
            self.moveForward = False

# create a class for computer cars
class compCars(pygame.sprite.Sprite):

    # constructor
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.car_x = x
        self.car_y = y
        self.carImg = img

        # add cars to sprite group
        computerCars.add(self)

    # update func
    def update(self, gameWindow):
        self.car_y -= 10
        gameWindow.blit(self.carImg, (self.car_x, self.car_y))

# function for displaying text
font = pygame.font.Font(None, 60)
def displayText(gameWindow, text, colour, xy):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, xy)

# function for choosing car for both single and multi player mode

def chooseCar(gameWindow, singleP = False, multiP = False):
    end = False
    n = 0
    car_xy = []
    screen_w = 1000
    screen_h = 700

    # load images
    cars = []
    for i in range(14):
        car = pygame.image.load(f'car{str(i+1)}.png')
        car = pygame.transform.scale(car, (70, 140))
        cars.append(car)

    boxIm = pygame.image.load('lvl_box.png')
    boxIm = pygame.transform.scale(boxIm, (70, 140))

    bg = pygame.image.load('bg.png')
    bg = pygame.transform.scale(bg, (screen_w, screen_h))

    bg2 = pygame.image.load('bg2.png')
    bg2 = pygame.transform.scale(bg2, (screen_w-60, (screen_h/2) + 100))

    clock = pygame.time.Clock()
    fps = 20

    # loop
    if singleP:
        while not end:
            # loop variables
            x = 45
            y = 250

            gameWindow.blit(bg, (0, 0))
            gameWindow.blit(bg2, (30, 150))

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
                        if n < 13:
                            n += 1
                        else:
                            n = 0
                    
                    if event.key == pygame.K_LEFT:
                        if n > 0:
                            n -= 1
                        else:
                            n = 13

                    # check player has selected which car
                    if event.key == pygame.K_RETURN:
                        return n
                        end = True

            # display text
            txt = 'Choose  a  car  by  left  and  right  arrow  keys'
            displayText(gameWindow, txt, (255, 255, 255), (45, 170))

            # display all car images
            for i in range(14):
                if i == 8:
                    y += 180
                    x = 45

                if len(car_xy) != 14:
                    car_xy.append([x, y])
                x += 120

            # display a box
            gameWindow.blit(boxIm, (car_xy[n]))

            for i in range(len(car_xy)):
                gameWindow.blit(cars[i], car_xy[i])

            # update the window
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()
        quit()

    elif multiP:
        pass