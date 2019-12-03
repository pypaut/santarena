import pygame

# Initialization required to import TILESIZE
pygame.init()

SCREEN_SCALE = 25  # The higher, the broader the camera
TILESIZE = pygame.display.list_modes()[0][0] // SCREEN_SCALE
PROJECTILE_SIZE = TILESIZE * (40/100)
MAP_H = TILESIZE * 40
MAP_W = TILESIZE * 40

COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "BLUE": (0, 0, 255),
    "GREY": (100, 100, 100),
    "RED": (200, 20, 20),
    "GREEN": (20, 200, 20),
}

FPS = 60
SPEED = 0.3
ENEMY_SPEED = 0.1
