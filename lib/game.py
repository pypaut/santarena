from lib.character import Character
import lib.constants as c
import pygame, sys
from pygame.locals import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SANTARENA")
        self.screen = pygame.display.set_mode((c.SURFWIDTH, c.SURFHEIGHT))
        self.character = Character()

    def Event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def Update(self):
        pass

    def Draw(self):
        self.screen.fill(c.BLUE)
        pygame.draw.rect(self.screen, c.WHITE, self.character.sprite)
        pygame.display.update()
