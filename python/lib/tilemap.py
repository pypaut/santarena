import lib.constants as c
import random


class Tilemap():
    def __init__(self, h, w, tilesize):
        # Tiles number
        self.tilesH = h // tilesize
        self.tilesW = w // tilesize

        self.map = [
            c.colors[random.randint(0, 2)]
            for i in range(self.tilesH * self.tilesW)
        ]
