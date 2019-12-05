import pygame
from lib.constants import (
    SPEED,
    COLORS,
    MAP_H,
    MAP_W,
    TILESIZE,
    PROJECTILE_SIZE
)
from lib.movable import Movable
from lib.projectile import Projectile


class Character(Movable):
    def __init__(self):
        # Position
        self.posH = 0
        self.posW = 0

        # Size
        self.rectH = TILESIZE
        self.rectW = TILESIZE

        # Movement
        self.speed = SPEED
        self.dirH = 0
        self.dirW = 0

        # Object
        self.rect = (self.posW, self.posH, self.rectW, self.rectH)

        # Projectiles
        self.projectiles = []
        self.shoot_cooldown = 100
        self.shoot_dirH = 0
        self.shoot_dirW = 1

    def shoot(self, camera):
        # Center pos
        posH = self.posH + (self.rectH - PROJECTILE_SIZE) // 2 - camera.posH
        posW = self.posW + (self.rectW - PROJECTILE_SIZE) // 2 - camera.posW

        # Set to right side
        posH += self.shoot_dirH * self.rectH // 2
        posW += self.shoot_dirW * self.rectW // 2

        self.projectiles.append(
            Projectile(
                posH,
                posW,
                self.shoot_dirH,
                self.shoot_dirW,
            )
        )
        self.shoot_cooldown = 200

    def event(self, keys, camera, enemies, blocks, dt):
        """
        Update according to pressed keys.
        """
        self.dirH = 0
        self.dirW = 0

        # Vertically blocked
        if keys[pygame.K_w] and keys[pygame.K_s]:
            self.dirH = 0
        # Up
        elif keys[pygame.K_w] and self.posH > 20:
            self.posH -= self.speed * dt
            self.dirH = -1
        # Down
        elif keys[pygame.K_s] and self.posH < MAP_H - self.rectH - 20:
            self.posH += self.speed * dt
            self.dirH = 1
        else:
            self.dirH = 0
        # Horizontally blocked
        if keys[pygame.K_a] and keys[pygame.K_d]:
            self.dirW = 0
        # Left
        elif keys[pygame.K_a] and self.posW > 20:
            self.posW -= self.speed * dt
            self.dirW = -1
        # Right
        elif keys[pygame.K_d] and self.posW < MAP_W - self.rectW - 20:
            self.posW += self.speed * dt
            self.dirW = 1
        else:
            self.dirW = 0
        # Look down right
        if keys[pygame.K_k] and keys[pygame.K_l]:
            self.shoot_dirH = 1
            self.shoot_dirW = 1
        # Look down left
        elif keys[pygame.K_k] and keys[pygame.K_j]:
            self.shoot_dirH = 1
            self.shoot_dirW = -1
        # Look up right
        elif keys[pygame.K_i] and keys[pygame.K_l]:
            self.shoot_dirH = -1
            self.shoot_dirW = 1
        # Look up left
        elif keys[pygame.K_i] and keys[pygame.K_j]:
            self.shoot_dirH = -1
            self.shoot_dirW = -1
        # Look down
        elif keys[pygame.K_k]:
            self.shoot_dirH = 1
            self.shoot_dirW = 0
        # Look up
        elif keys[pygame.K_i]:
            self.shoot_dirH = -1
            self.shoot_dirW = 0
        # Look left
        elif keys[pygame.K_j]:
            self.shoot_dirW = -1
            self.shoot_dirH = 0
        # Look right
        elif keys[pygame.K_l]:
            self.shoot_dirW = 1
            self.shoot_dirH = 0
        else:
            pass

        # Collision detection
        for item in blocks + enemies:
            if self.collides(item):
                self.reset_contact(item)

        # Shoot projectile
        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            self.shoot(camera)

    def update(self, camera, blocks, dt):
        """
        Update the rectangle object which is drawn on screen.
        From tilemap coordinates to screen coordinates.

        Update projectiles positions.
        """
        # Update shoot cooldown
        self.shoot_cooldown -= dt

        # Update rect
        self.rect = (
            self.posW - camera.posW,
            self.posH - camera.posH,
            self.rectW,
            self.rectH,
        )

        # Update projectiles
        for projectile in self.projectiles:
            projectile.update(camera, dt)
            if projectile.isOut():
                self.projectiles.remove(projectile)

    def draw(self, camera):
        pygame.draw.rect(camera.screen, COLORS["RED"], self.rect)
        for projectile in self.projectiles:
            projectile.draw(camera)
