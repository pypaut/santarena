import pygame
import sys
from pygame.locals import QUIT
from pygame.time import Clock
from random import randrange

from lib.camera import Camera
from lib.constants import MAP_H, MAP_W, FPS
from lib.character import Character
from lib.enemy import Enemy
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

        # Characters
        self.character = Character()
        self.enemies = []

        # Clock
        self.clock = Clock()
        self.dt = 0

    def start(self):
        """
        Called once.
        """
        # Set the camera in the center of the map
        self.camera.posH = (self.tilemap.h - self.camera.h) / 2
        self.camera.posW = (self.tilemap.w - self.camera.w) / 2

        # Set the character sprite in the center of the screen
        self.character.posH = (
            self.camera.posH + (self.camera.h - self.character.rectH) / 2
        )
        self.character.posW = (
            self.camera.posW + (self.camera.w - self.character.rectW) / 2
        )

        # Spawn some enemies
        for _ in range(3):
            randH = randrange(400)
            randW = randrange(700)
            self.enemies.append(Enemy(randH, randW))

    def event(self):
        # Quit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Character
        self.character.event(pygame.key.get_pressed(), self.camera, self.dt)

        # Enemies
        for enemy in self.enemies:
            enemy.event()

        # Camera
        self.camera.move(pygame.key.get_pressed(), self.character, self.dt)

    def update(self):
        # Map
        self.tilemap.update(self.camera)

        # Character & projectiles
        self.character.update(self.camera, self.dt)

        # Enemies
        for enemy in self.enemies:
            enemy.update(self.character, self.enemies, self.camera, self.dt)

        # Tic tac
        self.dt = self.clock.tick(FPS)

    def draw(self):
        # Tilemap
        self.tilemap.draw(self.camera)

        # Enemies
        for enemy in self.enemies:
            enemy.draw(self.camera)

        # Character
        self.character.draw(self.camera)

        pygame.display.update()
