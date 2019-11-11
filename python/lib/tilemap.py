from lib.constants import COLORS, TILESIZE


class Tilemap():
    def __init__(self, h, w):
        # Size
        self.h = h
        self.w = w

        # Tiles number
        self.tilesH = h // TILESIZE
        self.tilesW = w // TILESIZE

        # Map
        self.map = [
            COLORS['WHITE']
            for i in range(self.tilesH * self.tilesW)
        ]
        for i in range(self.tilesH):
            for j in range(self.tilesW):
                if i * j == 0 or i == self.tilesH - 1 or j == self.tilesW - 1:
                    self.map[i * j] = COLORS["GREY"]
