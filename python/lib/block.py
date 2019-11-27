import pygame
from lib.constants import COLORS, TILESIZE


class Block:
    def __init__(self, posH, posW):
        # Position
        self.posH = posH
        self.posW = posW

        # Size
        self.rectH = TILESIZE
        self.rectW = TILESIZE

        # Rect
        self.rect = (self.posW, self.posH, self.rectW, self.rectH)

    def event(self):
        pass

    def update(self, camera):
        """
        Rect position relative to the camera.
        """
        self.rect = (
            self.posW - camera.posW,
            self.posH - camera.posH,
            self.rectW,
            self.rectH,
        )

    def draw(self, camera):
        pygame.draw.rect(camera.screen, COLORS["GREY"], self.rect)
