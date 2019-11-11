import pygame
import sys
from pygame.locals import QUIT

from lib.camera import Camera
from lib.constants import MAP_H, MAP_W
from lib.character import Character
from lib.tilemap import Tilemap


class Game:
    def __init__(self):
        # Pygame launch
        pygame.init()
        pygame.display.set_caption("SANTARENA")

        # Screen (camera)
        self.camera = Camera(500, 800)

        # Tilemap
        self.tilemap = Tilemap(MAP_H, MAP_W)

        # Character
        self.character = Character()

    def start(self):
        """
        Called once.
        """
        # Set the character sprite in the center of the screen
        self.character.posH = (self.camera.h - self.character.rectH) / 2
        self.character.posW = (self.camera.w - self.character.rectW) / 2

        # Set the camera in the center of the map FIXME
        # self.camera.posH = (self.tilemap.h - self.camera.h) / 2
        # self.camera.posW = (self.tilemap.w - self.camera.w) / 2

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # self.character.move(pygame.key.get_pressed())
        self.camera.move(pygame.key.get_pressed())

    def update(self):
        self.character.update()

    def draw(self):
        self.camera.draw(self.tilemap)    # Tilemap
        self.character.draw(self.camera)  # Character

        pygame.display.update()
