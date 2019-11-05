from lib.character import Character
import lib.constants as c
import pygame, sys
from pygame.locals import *

class Game():
    def __init__(self):
        # Pygame launch
        pygame.init()
        pygame.display.set_caption("SANTARENA")

        # Screen
        self.screenH = 500
        self.screenW = 800
        self.screen = pygame.display.set_mode((self.screenW, self.screenH))

        # Character
        self.character = Character()

    def Start(self):
        """
        Called once.
        """
        # Set the character sprite in the center of the screen
        self.character.posH = (self.screenH / 2) - (self.character.spriteH / 2)
        self.character.posW = (self.screenW / 2) - (self.character.spriteW / 2)

    def Event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def Update(self):
        self.character.Update()

    def Draw(self):
        self.screen.fill(c.BLUE)
        pygame.draw.rect(self.screen, c.WHITE, self.character.sprite)
        pygame.display.update()
