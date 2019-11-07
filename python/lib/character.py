import pygame
from pygame.time import Clock
from lib.constants import FPS


class Character:
    def __init__(self):
        # Position
        self.posH = 0
        self.posW = 0

        # Size
        self.spriteH = 50
        self.spriteW = 50

        # Movement
        self.speed = 0.5

        # Object
        self.sprite = (self.posW, self.posH, self.spriteW, self.spriteH)

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
        self.sprite = (self.posW, self.posH, self.spriteW, self.spriteH)
