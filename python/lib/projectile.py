import pygame
from pygame.time import Clock
from lib.constants import FPS, COLORS, MAP_H, MAP_W


class Projectile:
    def __init__(self, posH, posW, dirH, dirW):
        self.posH = posH
        self.posW = posW
        self.dirH = dirH
        self.dirW = dirW

        self.speed = 2

        self.rect = (self.posW, self.posH, 20, 20)

    def update(self, camera):
        self.posW += self.speed * self.dirW * Clock().tick(FPS)
        self.posH += self.speed * self.dirH * Clock().tick(FPS)
        self.rect = (self.posW, self.posH, 20, 20)

    def isOut(self):
        return (self.posW >= MAP_W or self.posW <= 0 or self.posH >= MAP_H or self.posH <= 0)


    def draw(self, camera):
        pygame.draw.rect(camera.screen,
                         COLORS['BLUE'],
                         self.rect)
