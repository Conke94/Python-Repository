import pygame 
from pygame.locals import *
from Player import *

WIDTH = 1280
HEIGHT = 720

class Graphic_Manager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Estatísticas Voleibol")
        pygame.font.init()
        
        self.fontBold = pygame.font.SysFont("Monospace", 30, True, False)
        self.fontClassic = pygame.font.SysFont("Monospace", 30, False, False)
        
        self.clock = pygame.time.Clock()