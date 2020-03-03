import pygame
from lib.constants import COLORS, MAP_H, MAP_W, PROJECTILE_SIZE
from lib.movable import Movable


class Projectile(Movable):
    def __init__(self, posH, posW, dirH, dirW):
        self.posH = posH
        self.posW = posW
        self.dirH = dirH
        self.dirW = dirW
        self.rectH = PROJECTILE_SIZE
        self.rectW = PROJECTILE_SIZE

        self.speed = 1

        self.rect = (self.posW, self.posH, self.rectW, self.rectH)

    def update(self, camera, dt):
        self.posW += self.speed * self.dirW * dt
        self.posH += self.speed * self.dirH * dt
        self.rect = (self.posW, self.posH, PROJECTILE_SIZE, PROJECTILE_SIZE)

    def isOut(self):
        return (
            self.posW >= MAP_W
            or self.posW <= 0
            or self.posH >= MAP_H
            or self.posH <= 0
        )

    def draw(self, camera):
        pygame.draw.rect(camera.screen, COLORS["BLUE"], self.rect)
