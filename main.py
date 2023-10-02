import time

import pygame
import random

#Konstanten

WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (34, 139, 34)
SPACE = 50

#Globalen
sx = 0
sy = 0

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#Setup

pygame.init()
clock = pygame.time.Clock()
running = True
SCREEN.fill(BLACK)
pygame.display.set_caption('Snake')





def drawGrid():
    blockSize = 50
    for x in range(0, WIDTH , blockSize):
        for y in range(0, HEIGHT , blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


food_position = None

def generate_food_position():
    # ändern falls Schlange länger wird
    x1 = random.randint(0, (WIDTH/SPACE)-1) * SPACE
    y1 = random.randint(0, (HEIGHT / SPACE) - 1) * SPACE
    return x1, y1

def drawFood():
    global food_position
    if food_position is None:
        food_position = generate_food_position()
    rect = pygame.Rect(food_position[0], food_position[1], SPACE, SPACE)
    SCREEN.fill(RED, rect)

def drawSnake():
    global sx,sy
    slegth = 1
    if slegth == 1:
        rect = pygame.Rect(sx, sy, SPACE, SPACE)
        SCREEN.fill(GREEN, rect)

def displayScore(Score):
    font = pygame.font.SysFont(None, 36)
    score_text = font.render("Score: " + str(Score), True, WHITE)
    SCREEN.blit(score_text, (10, 10))

def moveSnake():
    global sx, sy
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and sy > 0:
        sy -= SPACE
        time.sleep(0.2)
    elif keys[pygame.K_s] and sy < HEIGHT - SPACE:
        sy += SPACE
        time.sleep(0.2)
    elif keys[pygame.K_a] and sx > 0:
        sx -= SPACE
        time.sleep(0.2)
    elif keys[pygame.K_d] and sx < WIDTH - SPACE:
        sx += SPACE
        time.sleep(0.2)
Score = 0
def checkIfOnFood():
    global food_position, Score
    global sx, sy


    if(food_position[0] == sx and food_position[1] == sy):

        Score += 1
        food_position = None
        drawFood()
    displayScore(Score)




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    SCREEN.fill(BLACK)


    moveSnake()


    drawGrid()

    drawFood()
    drawSnake()
    checkIfOnFood()
    #isplayScore(0)

    pygame.display.update()

    clock.tick(60)