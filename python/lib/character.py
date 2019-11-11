import pygame
from pygame.time import Clock
from lib.constants import FPS, SPEED


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
        if keys[pygame.K_w]:  # Up
            self.posH -= self.speed * Clock().tick(FPS)
        if keys[pygame.K_s]:  # Down
            self.posH += self.speed * Clock().tick(FPS)
        if keys[pygame.K_a]:  # Left
            self.posW -= self.speed * Clock().tick(FPS)
        if keys[pygame.K_d]:  # Right
            self.posW += self.speed * Clock().tick(FPS)

    def update(self):
        self.rect = (self.posW, self.posH, self.rectW, self.rectH)
