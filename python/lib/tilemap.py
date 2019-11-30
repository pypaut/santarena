import pygame
from lib.block import Block
from lib.constants import COLORS, TILESIZE


class Tilemap:
    def __init__(self, h, w):
        # Size
        self.h = h
        self.w = w

        # Tiles number
        self.tilesH = h // TILESIZE
        self.tilesW = w // TILESIZE

        # Blocks
        self.blocks = []
        # Outer bounds
        for i in range(self.tilesH):
            for j in range(self.tilesW):
                if (
                    i == 0
                    or i == self.tilesH - 1
                    or j == 0
                    or j == self.tilesW - 1
                ):
                    self.blocks.append(Block(i * TILESIZE, j * TILESIZE))
        # Random block
        self.blocks.append(Block(self.h // 3, self.w // 2))

        # Map colors
        self.map = [COLORS["WHITE"] for i in range(self.tilesH * self.tilesW)]

    def event(self):
        pass

    def update(self, camera):
        for block in self.blocks:
            block.update(camera)

    def draw(self, camera):
        # Whole map
        for i in range(self.tilesH):
            for j in range(self.tilesW):
                rect = (
                    j * TILESIZE - camera.posW,
                    i * TILESIZE - camera.posH,
                    TILESIZE,
                    TILESIZE,
                )
                pygame.draw.rect(camera.screen, self.map[i * j], rect)

        # Blocks
        for block in self.blocks:
            block.draw(camera)
