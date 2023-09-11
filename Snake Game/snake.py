import pygame
from pygame.locals import *
import random

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def collision (c1, c2):
    return (c1[0] == c2[0]) and (c1[1]==c2[1])

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")

snake = [(200,200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))
direction = LEFT

apple_pos = (random.randint(0, 49)*10, random.randint(0, 49)*10)
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

clock = pygame.time.Clock()

while True:
    clock.tick(13)

    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit()

        if event.type == KEYDOWN:
            if (event.key == K_w):
                direction = UP
            if (event.key == K_d):
                direction = RIGHT
            if (event.key == K_s):
                direction = DOWN
            if (event.key == K_a):
                direction = LEFT

    if (collision(snake[0], apple_pos)):
        apple_pos = (random.randint(0, 49)*10, random.randint(0, 49)*10)
        snake.append((0, 0))

    if (snake[0][0] > 490 or snake[0][0]<0):
        pygame.quit()
        exit()
    elif (snake[0][1] > 490 or snake[0][1]<0):
        pygame.quit()
        exit()
    else:
        for i in range (1, len(snake), 1):
            if snake[0][0] == snake[i][0] and snake[0][1]==snake[i][1]:
                pygame.quit()
                exit()
    
    for i in range (len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if (direction == UP):
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif (direction == RIGHT):
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif (direction == DOWN):
        snake[0] = (snake[0][0], snake[0][1] + 10)
    else:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 0, 0))
    for pos in snake:
        screen.blit(snake_skin, pos)
    screen.blit(apple, apple_pos)

    pygame.display.update()