# snake_game/utils.py
import random

import pygame

from snake_game.settings import BLOCK_SIZE, HEIGHT, WIDTH


def get_random_position():
    x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return [x, y]


def get_ball_position(snake):
    pos = get_random_position()
    while pos in snake:
        pos = get_random_position()
    return pos


def create_gradient_surface(width, height, top_color, bottom_color):
    surface = pygame.Surface((width, height))
    for y in range(height):
        ratio = y / height
        r = int(top_color[0] * (1 - ratio) + bottom_color[0] * ratio)
        g = int(top_color[1] * (1 - ratio) + bottom_color[1] * ratio)
        b = int(top_color[2] * (1 - ratio) + bottom_color[2] * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (width, y))
    return surface
