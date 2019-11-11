import pygame
from pygame.time import Clock
from lib.constants import FPS, SPEED, COLORS, MAP_H, MAP_W


class Character:
    def __init__(self):
        # Position
        self.posH = 0
        self.posW = 0

        # Size
        self.rectH = 50
        self.rectW = 50

        # Movement
        self.speed = SPEED

        # Object
        self.rect = (self.posW, self.posH, self.rectW, self.rectH)

    def move(self, keys):
        """
        Update position according to pressed keys.
        """
        # Up
        if keys[pygame.K_w] and self.posH > 20:
            self.posH -= self.speed * Clock().tick(FPS)
        # Down
        if keys[pygame.K_s] and self.posH < MAP_H - self.rectH - 20:
            self.posH += self.speed * Clock().tick(FPS)
        # Left
        if keys[pygame.K_a] and self.posW > 20:
            self.posW -= self.speed * Clock().tick(FPS)
        # Right
        if keys[pygame.K_d] and self.posW < MAP_W - self.rectW - 20:
            self.posW += self.speed * Clock().tick(FPS)

    def update(self, camera):
        """
        Update the rectangle object which is drawn on screen.
        From tilemap coordinates to screen coordinates.
        """
        self.rect = (self.posW - camera.posW,
                     self.posH - camera.posH,
                     self.rectW,
                     self.rectH)

    def draw(self, camera):
        pygame.draw.rect(camera.screen,
                         COLORS['RED'],
                         self.rect)
