import lib.constants as c


class Tilemap():
    def __init__(self, h, w, tilesize):
        # Tiles number
        self.tilesH = h // tilesize
        self.tilesW = w // tilesize

        self.map = [
            c.colors['WHITE']
            for i in range(self.tilesH * self.tilesW)
        ]
