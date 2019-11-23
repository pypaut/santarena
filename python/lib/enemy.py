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

        # Rect
        self.rect = (self.posW, self.posH, self.rectW, self.rectH)

    def collides(self, enemy):
        condH = enemy.posH > self.posH and enemy.posH < self.posH + self.rectH
        condW = enemy.posW > self.posW and enemy.posW < self.posW + self.rectW
        if condH and condW:
            return True

    def reset_contact(self, enemy):
        """
        Reset position to contact position, before collision.
        """
        pass

    def event(self):
        """
        Collision, death.
        """
        pass

    def update(self, character, enemies, camera, dt):
        """
        AI for movement.
        """
        # Set direction
        h = character.posH - self.posH
        self.dirH = h / abs(h)
        w = character.posW - self.posW
        self.dirW = w / abs(w)

        # Update position
        self.posW += moveW
        self.posH += moveH

        # Check collision with other enemies
        for enemy in enemies:
            if self.collides(enemy):
                self.reset_contact(enemy)

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
