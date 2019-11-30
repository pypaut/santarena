import pygame
from lib.constants import SPEED, MAP_H, MAP_W


class Camera:
    def __init__(self, h, w):
        # Size
        self.h = h
        self.w = w

        # Position
        self.posH = 0
        self.posW = 0

        # Speed
        self.speed = SPEED

        self.screen = pygame.display.set_mode((self.w, self.h))

    def move(self, keys, character, dt):
        """
        Update position according to pressed keys.
        """
        centerH = self.posH + self.h / 2
        centerW = self.posW + self.w / 2
        # Vertically blocked
        if keys[pygame.K_w] and keys[pygame.K_s]:
            pass
        # Up
        elif keys[pygame.K_w] and self.posH > 0 and character.posH <= centerH:
            self.posH -= self.speed * dt
        # Down
        elif (
            keys[pygame.K_s]
            and self.posH < MAP_H - self.h
            and character.posH >= centerH
        ):
            self.posH += self.speed * dt
        # Horizontally blocked
        if keys[pygame.K_a] and keys[pygame.K_d]:
            pass
        # Left
        elif keys[pygame.K_a] and self.posW > 0 and character.posW <= centerW:
            self.posW -= self.speed * dt
        # Right
        elif (
            keys[pygame.K_d]
            and self.posW < MAP_W - self.w
            and character.posW >= centerW
        ):
            self.posW += self.speed * dt

    def draw(self, tilemap):
        pass
