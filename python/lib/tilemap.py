import lib.constants as c
import random

class Tilemap():
    def __init__(self, H, W, tilesize):
        # Tiles number
        self.tilesH = H // tilesize
        self.tilesW = W // tilesize

        self.map = [
            c.colors[random.randint(0,2)] for i in range(self.tilesH * self.tilesW)
        ]
