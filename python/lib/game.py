import pygame
import sys
from pygame.locals import QUIT
from pygame.time import Clock

import lib.constants as c
from lib.character import Character
from lib.tilemap import Tilemap


class Game:
    def __init__(self):
        # Pygame launch
        pygame.init()
        pygame.display.set_caption("SANTARENA")
        self.fps = 60

        # Screen
        self.screenH = 500
        self.screenW = 800
        self.screen = pygame.display.set_mode((self.screenW, self.screenH))

        # Tilemap
        self.tilesize = 50
        self.tilemap = Tilemap(self.screenH, self.screenW, self.tilesize)

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
        keys = pygame.key.get_pressed()
        speed = self.character.speed

        if keys[pygame.K_w]:  # Up
            self.character.posH -= speed * Clock().tick(self.fps)
        if keys[pygame.K_s]:  # Down
            self.character.posH += speed * Clock().tick(self.fps)
        if keys[pygame.K_a]:  # Left
            self.character.posW -= speed * Clock().tick(self.fps)
        if keys[pygame.K_d]:  # Right
            self.character.posW += speed * Clock().tick(self.fps)

    def update(self):
        self.character.update()

    def draw(self):
        # Tilemap
        for i in range(self.tilemap.tilesH):
            for j in range(self.tilemap.tilesW):
                rect = (j * self.tilesize,
                        i * self.tilesize,
                        self.tilesize,
                        self.tilesize)
                pygame.draw.rect(self.screen, self.tilemap.map[i * j], rect)

        # Character
        pygame.draw.rect(self.screen, c.colors['RED'], self.character.sprite)
        pygame.display.update()
