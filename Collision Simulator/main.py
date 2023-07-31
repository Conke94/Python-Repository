import pygame
from pygame.locals import *
from random import randint
import math

FPS = 60
WIDTH = 1280
HEIGHT = 720

MIN_MASS = 50
MAX_MASS = 100
MIN_VEL = -4
MAX_VEL = 4

COLOR = 0x00FF00

class Ball:
    def __init__(self, position_x, position_y):
        self.mass = randint(MIN_MASS, MAX_MASS)
        self.color = COLOR
        self.radius = int(self.mass/2)
        
        self.position = pygame.math.Vector2(position_x, position_y)
        self.velocity = pygame.math.Vector2(randint(MIN_VEL, MAX_VEL), randint(MIN_VEL, MAX_VEL))

        self.screen = screen
        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

    def move (self):
        self.position += self.velocity

    def manage_wall_collision(self):
        if self.position[0] <= self.radius:
            self.velocity[0] = (-1)*self.velocity[0]
            dx = self.radius - self.position[0] + 2
            self.position[0] = self.position[0] + dx
        if self.position[1] <= self.radius:
            self.velocity[1] = (-1)*self.velocity[1]
            dy = self.radius - self.position[1] + 2
            self.position[1] += dy
        if WIDTH-self.position[0] <= self.radius:
            self.velocity[0] = (-1)*self.velocity[0]
            dx = self.radius - WIDTH + self.position[0] + 2
            self.position[0] -= dx
        if HEIGHT-self.position[1] <= self.radius:
            self.velocity[1] = (-1)*self.velocity[1]
            dy = self.radius - HEIGHT + self.position[1] + 2
            self.position[1] -= dy

def def_inicial_balls(list_of_balls):
    for i in range (55, WIDTH-55, 180):
        for j in range (55, HEIGHT-55, 180):
            newBall = Ball(i, j)
            list_of_balls.append(newBall)
    return list_of_balls

def manage_ball_collision (b1, b2):
    distance = math.sqrt(math.pow(b1.position[0]-b2.position[0], 2) + math.pow(b1.position[1]-b2.position[1], 2))

    v1 = b1.velocity
    v2 = b2.velocity
    x1 = b1.position
    x2 = b2.position
    m1 = b1.mass
    m2 = b2.mass

    if distance < b1.radius + b2.radius:
        b1.velocity = v1 - (2*m2/(m1 + m2)) * pygame.math.Vector2.project((v1-v2), (x1-x2))
        b2.velocity = v2 - (2*m1/(m2 + m1)) * pygame.math.Vector2.project((v2-v1), (x2-x1))

    avoid_ball_bug(b1, b2)

def avoid_ball_bug (b1, b2):
    distance = math.sqrt(math.pow(b1.position[0]-b2.position[0], 2) + math.pow(b1.position[1]-b2.position[1], 2))

    while (distance < b1.radius + b2.radius):
        b1.move()
        b2.move()
        distance = math.sqrt(math.pow(b1.position[0]-b2.position[0], 2) + math.pow(b1.position[1]-b2.position[1], 2))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Simulator")
clock = pygame.time.Clock()

list_of_balls = []
list_of_balls = def_inicial_balls(list_of_balls)

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    screen.fill((0, 0, 0))
    for i in range (0, len(list_of_balls)-1, 1):
        for j in range (i+1, len(list_of_balls), 1):
            manage_ball_collision(list_of_balls[i], list_of_balls[j])

    for i in range (0, len(list_of_balls), 1):
        list_of_balls[i].manage_wall_collision()
        list_of_balls[i].move()
        list_of_balls[i].draw()

    pygame.display.update()