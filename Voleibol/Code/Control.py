from Graphic_Manager import *
from Player import *
import sys
import time
from PlayerRegister import *

class Control:
    def __init__(self):
        self.graphManager = Graphic_Manager()
        self.playerList = []
        self.windowLoop()

    def getPlayerList (self):
        return self.playerList

    def windowLoop (self):
        while True:
            self.graphManager.clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        playerRegisterPlat = PlayerRegister()

            self.graphManager.screen.fill((230, 230, 230))
            pygame.display.update()