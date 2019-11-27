import pygame
from lib.constants import COLORS, TILESIZE


class Tilemap:
    def __init__(self, h, w):
        # Size
        self.h = h
        self.w = w

        # Tiles number
        self.tilesH = h // TILESIZE
        self.tilesW = w // TILESIZE

        # Map
        self.map = [COLORS["WHITE"] for i in range(self.tilesH * self.tilesW)]
        for i in range(self.tilesH):
            for j in range(self.tilesW):
                if i * j == 0 or i == self.tilesH - 1 or j == self.tilesW - 1:
                    self.map[i * j] = COLORS["GREY"]

    def event(self):
        pass

    def update(self):
        pass

    def draw(self, camera):
        for i in range(self.tilesH):
            for j in range(self.tilesW):
                rect = (
                    j * TILESIZE - camera.posW,
                    i * TILESIZE - camera.posH,
                    TILESIZE,
                    TILESIZE,
                )
                pygame.draw.rect(camera.screen, self.map[i * j], rect)
