from lib.constants import COLORS, TILESIZE


class Tilemap():
    def __init__(self, h, w):
        # Tiles number
        self.tilesH = h // TILESIZE
        self.tilesW = w // TILESIZE

        self.map = [
            COLORS['WHITE']
            for i in range(self.tilesH * self.tilesW)
        ]
