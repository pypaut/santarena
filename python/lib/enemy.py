import math
import pygame

from lib.constants import ENEMY_SPEED, COLORS
from lib.movable import Movable


class Enemy(Movable):
    def __init__(self, posH, posW):
        # Position
        self.posH = posH
        self.posW = posW

        # Size
        self.rectH = 50
        self.rectW = 50

        # Movement
        self.speed = ENEMY_SPEED
        self.dirH = 0
        self.dirW = 0

        # Rect (camera position)
        self.rect = (self.posW, self.posH, self.rectW, self.rectH)

    def event(self, character, enemies, blocks):
        """
        Collision, death.
        """
        # Check collision with other enemies
        for enemy in [character] + enemies + blocks:
            if enemy != self and self.collides(enemy):
                self.reset_contact(enemy)

    def update(self, character, enemies, camera, dt):
        """
        AI for movement.
        """
        # Set direction and normalize
        h = character.posH - self.posH
        w = character.posW - self.posW
        length = math.sqrt(h ** 2 + w ** 2)
        self.dirH = h / length
        self.dirW = w / length

        # Update position
        self.posW += self.dirW * self.speed * dt
        self.posH += self.dirH * self.speed * dt

        # Camera position
        self.rect = (
            self.posW - camera.posW,
            self.posH - camera.posH,
            self.rectW,
            self.rectH,
        )

    def draw(self, camera):
        """
        Display rect.
        """
        pygame.draw.rect(camera.screen, COLORS["GREEN"], self.rect)
