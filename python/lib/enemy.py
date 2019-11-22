import pygame

from lib.constants import ENEMY_SPEED, COLORS


class Enemy:
    def __init__(self, posH, posW):
        # Position
        self.posH = posH
        self.posW = posW

        # Size
        self.rectH = 50
        self.rectW = 50

        # Movement
        self.speed = ENEMY_SPEED

        # Rect
        self.rect = (self.posW, self.posH, self.rectW, self.rectH)

    def event(self):
        """
        Collision, death.
        """
        pass

    def update(self, character, camera, dt):
        """
        AI for movement.
        """
        h = character.posH - self.posH
        directionH = h / abs(h)
        w = character.posW - self.posW
        directionW = w / abs(w)

        self.posW += directionW * self.speed * dt
        self.posH += directionH * self.speed * dt
        self.rect = (self.posW - camera.posW,
                     self.posH - camera.posH,
                     self.rectW,
                     self.rectH)

    def draw(self, camera):
        """
        Display rect.
        """
        pygame.draw.rect(camera.screen,
                         COLORS['GREEN'],
                         self.rect)
