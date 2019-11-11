import pygame
from pygame.time import Clock
from lib.constants import FPS, SPEED, TILESIZE, MAP_H, MAP_W


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
        # Up
        if keys[pygame.K_w] and self.posH > 0:
            self.posH -= self.speed * Clock().tick(FPS)
        # Down
        if keys[pygame.K_s] and self.posH < MAP_H - self.h:
            self.posH += self.speed * Clock().tick(FPS)
        # Left
        if keys[pygame.K_a] and self.posW > 0:
            self.posW -= self.speed * Clock().tick(FPS)
        # Right
        if keys[pygame.K_d] and self.posW < MAP_W - self.w:
            self.posW += self.speed * Clock().tick(FPS)

    def draw(self, tilemap):
        for i in range(tilemap.tilesH):
            for j in range(tilemap.tilesW):
                rect = (j * TILESIZE - self.posW,
                        i * TILESIZE - self.posH,
                        TILESIZE,
                        TILESIZE)
                pygame.draw.rect(self.screen,
                                 tilemap.map[i * j],
                                 rect)
