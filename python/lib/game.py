import pygame
import sys
from pygame.locals import QUIT

from lib.constants import TILESIZE, COLORS
from lib.character import Character
from lib.tilemap import Tilemap


class Game:
    def __init__(self):
        # Pygame launch
        pygame.init()
        pygame.display.set_caption("SANTARENA")

        # Screen (camera)
        self.screenH = 500
        self.screenW = 800
        self.screen = pygame.display.set_mode((self.screenW,
                                               self.screenH))

        # Tilemap
        self.tilemap = Tilemap(self.screenH, self.screenW)

        # Character
        self.character = Character()

    def start(self):
        """
        Called once.
        """
        # Set the character sprite in the center of the screen
        self.character.posH = (self.screenH / 2) - (self.character.spriteH / 2)
        self.character.posW = (self.screenW / 2) - (self.character.spriteW / 2)

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        self.character.move(pygame.key.get_pressed())

    def update(self):
        self.character.update()

    def draw(self):
        # Tilemap
        for i in range(self.tilemap.tilesH):
            for j in range(self.tilemap.tilesW):
                rect = (j * TILESIZE,
                        i * TILESIZE,
                        TILESIZE,
                        TILESIZE)
                pygame.draw.rect(self.screen, self.tilemap.map[i * j], rect)

        # Character
        pygame.draw.rect(self.screen, COLORS['RED'], self.character.sprite)
        pygame.display.update()
