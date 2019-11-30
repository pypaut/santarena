import pygame
from lib.constants import SPEED, COLORS, MAP_H, MAP_W
from lib.projectile import Projectile


class Character:
    def __init__(self):
        # Position
        self.posH = 0
        self.posW = 0
        self.nextposH = 0
        self.nextposW = 0

        # Size
        self.rectH = 50
        self.rectW = 50

        # Movement
        self.speed = SPEED
        self.dirH = 0
        self.dirW = 0
        self.moveH = 0
        self.moveW = 0

        # Object
        self.rect = (self.posW, self.posH, self.rectW, self.rectH)

        # Projectiles
        self.projectiles = []
        self.shoot_cooldown = 200
        self.shoot_dirH = 0
        self.shoot_dirW = 1

    def collides(self, block):
        condH = (
            self.nextposH < block.posH + block.rectH
            and self.nextposH > block.posH - self.rectH
        )
        condW = (
            self.nextposW < block.posW + block.rectW
            and self.nextposW > block.posW - self.rectW
        )
        return condH and condW

    def reset_contact(self, block):
        """
        Reset position to contact position, before collision.
        """
        # Collision direction
        # h = self.dirH
        # w = self.dirW
        # length = math.sqrt(h ** 2 + w ** 2)
        # collision_dirH = h / length if length else 0
        # collision_dirW = w / length if length else 0

        # Overlap gap
        gapH = self.dirH * (self.rectH - abs(self.posH - block.posH))
        gapW = self.dirW * (self.rectW - abs(self.posW - block.posW))

        # Reset
        self.posH -= gapH
        self.posW -= gapW
        print(f"GAPH: {gapH}, GAPW: {gapW}")

    def shoot(self, camera):
        self.projectiles.append(
            Projectile(
                self.posH - camera.posH,
                self.posW - camera.posW,
                self.shoot_dirH,
                self.shoot_dirW,
            )
        )
        self.shoot_cooldown = 200

    def event(self, keys, camera, blocks, dt):
        """
        Update according to pressed keys.
        """
        self.dirH = 0
        self.dirW = 0
        self.moveH = 0
        self.moveW = 0

        # Vertically blocked
        if keys[pygame.K_w] and keys[pygame.K_s]:
            return
        # Up
        elif keys[pygame.K_w] and self.posH > 20:
            self.moveH = self.speed * dt
            self.dirH = -1
        # Down
        elif keys[pygame.K_s] and self.posH < MAP_H - self.rectH - 20:
            self.moveH = self.speed * dt
            self.dirH = 1
        else:
            self.dirH = 0
        # Horizontally blocked
        if keys[pygame.K_a] and keys[pygame.K_d]:
            return
        # Left
        elif keys[pygame.K_a] and self.posW > 20:
            self.moveW = self.speed * dt
            self.dirW = -1
        # Right
        elif keys[pygame.K_d] and self.posW < MAP_W - self.rectW - 20:
            self.moveW = self.speed * dt
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
        self.nextposH = self.posH + self.dirH * self.moveH
        self.nextposW = self.posW + self.dirW * self.moveW

        for block in blocks:
            if self.collides(block):
                gapH = self.dirH * (
                    self.rectH - abs(self.nextposH - block.posH)
                )
                gapW = self.dirW * (
                    self.rectW - abs(self.nextposW - block.posW)
                )
                if gapH != 0:
                    self.moveH = 0
                    self.posH += gapH * self.dirH
                if gapW != 0:
                    self.moveW = 0
                    self.posW += gapW * self.dirW

        # Shoot projectile
        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            self.shoot(camera)

    def update(self, camera, blocks, dt):
        """
        Update the rectangle object which is drawn on screen.
        From tilemap coordinates to screen coordinates.

        Update projectiles positions.
        """
        # Update position
        self.posH += self.dirH * self.moveH
        self.posW += self.dirW * self.moveW

        # Update shoot cooldown
        self.shoot_cooldown -= dt

        # Check collision with blocks
        # for block in blocks:
        #     if self.collides(block):
        #         self.reset_contact(block)

        # Update rect
        self.rect = (
            self.posW - camera.posW,
            self.posH - camera.posH,
            self.rectW,
            self.rectH,
        )

        # Update projectiles
        # for projectile in self.projectiles:
        #     projectile.update(camera, dt)
        #     if projectile.isOut():
        #         self.projectiles.remove(projectile)

    def draw(self, camera):
        pygame.draw.rect(camera.screen, COLORS["RED"], self.rect)
        for projectile in self.projectiles:
            projectile.draw(camera)
