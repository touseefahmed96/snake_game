# snake_game/utils.py
import random

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
