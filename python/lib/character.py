import pygame
from pygame.time import Clock
from lib.constants import FPS, SPEED, COLORS, MAP_H, MAP_W
from lib.projectile import Projectile


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
        self.dirH = 0
        self.dirW = 1

        # Object
        self.rect = (self.posW, self.posH, self.rectW, self.rectH)

        # Projectiles
        self.projectiles = []

    def shoot(self):
        self.projectiles.append(Projectile(self.posH, self.posW, self.dirH, self.dirW))

    def event(self, keys):
        """
        Update according to pressed keys.
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
        # Look down right
        if keys[pygame.K_k] and keys[pygame.K_l]:
            self.dirH = 1
            self.dirW = 1
        # Look down left
        elif keys[pygame.K_k] and keys[pygame.K_j]:
            self.dirH = 1
            self.dirW = -1
        # Look up right
        elif keys[pygame.K_i] and keys[pygame.K_l]:
            self.dirH = -1
            self.dirW = 1
        # Look up left
        elif keys[pygame.K_i] and keys[pygame.K_j]:
            self.dirH = -1
            self.dirW = -1
        # Look down
        elif keys[pygame.K_k]:
            self.dirH = 1
            self.dirW = 0
        # Look up
        elif keys[pygame.K_i]:
            self.dirH = -1
            self.dirW = 0
        # Look left
        elif keys[pygame.K_j]:
            self.dirW = -1
            self.dirH = 0
        # Look right
        elif keys[pygame.K_l]:
            self.dirW = 1
            self.dirH = 0
        else:
            pass
        # Shoot projectile
        if keys[pygame.K_SPACE]:
            self.shoot()

    def update(self, camera):
        """
        Update the rectangle object which is drawn on screen.
        From tilemap coordinates to screen coordinates.

        Update projectiles positions.
        """
        self.rect = (self.posW - camera.posW,
                     self.posH - camera.posH,
                     self.rectW,
                     self.rectH)
        for projectile in self.projectiles:
            projectile.update(camera)
            if projectile.isOut():
                self.projectiles.remove(projectile)

    def draw(self, camera):
        pygame.draw.rect(camera.screen,
                         COLORS['RED'],
                         self.rect)
        for projectile in self.projectiles:
            projectile.draw(camera)
