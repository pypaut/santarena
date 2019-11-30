import math
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
        self.dirH = 0
        self.dirW = 0

        # Rect (camera position)
        self.rect = (self.posW, self.posH, self.rectW, self.rectH)

    def collides(self, enemy):
        condH = (
            self.posH < enemy.posH + enemy.rectH
            and self.posH > enemy.posH - self.rectH
        )
        condW = (
            self.posW < enemy.posW + enemy.rectW
            and self.posW > enemy.posW - self.rectW
        )
        return condH and condW

    def reset_contact(self, enemy):
        """
        Reset position to contact position, before collision.
        """
        # Collision direction
        h = self.dirH - enemy.dirH
        w = self.dirW - enemy.dirW
        length = math.sqrt(h ** 2 + w ** 2)
        collision_dirH = h / length
        collision_dirW = w / length

        # Overlap gap
        gapH = collision_dirH * (self.rectH - abs(self.posH - enemy.posH))
        gapW = collision_dirW * (self.rectW - abs(self.posW - enemy.posW))

        # Reset
        if gapH > gapW:
            self.posH -= gapH
        else:
            self.posW -= gapW

    def event(self):
        """
        Collision, death.
        """
        pass

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

        # Check collision with other enemies
        for enemy in [character] + enemies:
            if enemy != self and self.collides(enemy):
                self.reset_contact(enemy)

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
