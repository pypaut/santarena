import pygame
from pygame.time import Clock
from lib.constants import FPS, SPEED, TILESIZE


class Camera:
    def __init__(self, h, w):
        # Size
        self.h = h
        self.w = w

        # Position
        self.posH = 0
        self.posW = 0

        # Speed
        self.speed = SPEED

        self.screen = pygame.display.set_mode((self.w, self.h))

    def move(self, keys):
        """
        Update position according to pressed keys.
        """
        if keys[pygame.K_w]:  # Up
            self.posH += self.speed * Clock().tick(FPS)
        if keys[pygame.K_s]:  # Down
            self.posH -= self.speed * Clock().tick(FPS)
        if keys[pygame.K_a]:  # Left
            self.posW += self.speed * Clock().tick(FPS)
        if keys[pygame.K_d]:  # Right
            self.posW -= self.speed * Clock().tick(FPS)

    def draw(self, tilemap):
        for i in range(tilemap.tilesH):
            for j in range(tilemap.tilesW):
                rect = (j * TILESIZE + self.posW,
                        i * TILESIZE + self.posH,
                        TILESIZE,
                        TILESIZE)
                pygame.draw.rect(self.screen,
                                 tilemap.map[i * j],
                                 rect)
