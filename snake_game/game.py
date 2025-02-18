# snake_game/game.py
import sys

import pygame

from snake_game.settings import BLOCK_SIZE, FPS, HEIGHT, WIDTH


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Ball Eater")
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.snake = [
            [WIDTH // 2, HEIGHT // 2],
            [WIDTH // 2 - BLOCK_SIZE, HEIGHT // 2],
            [WIDTH // 2 - 2 * BLOCK_SIZE, HEIGHT // 2],
        ]
        self.direction = (BLOCK_SIZE, 0)
        self.running = True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (0, BLOCK_SIZE):
                    self.direction = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and self.direction != (0, -BLOCK_SIZE):
                    self.direction = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and self.direction != (BLOCK_SIZE, 0):
                    self.direction = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-BLOCK_SIZE, 0):
                    self.direction = (BLOCK_SIZE, 0)

    def update(self):
        new_head = [
            self.snake[0][0] + self.direction[0],
            self.snake[0][1] + self.direction[1],
        ]
        self.snake.insert(0, new_head)
        self.snake.pop()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for segment in self.snake:
            pygame.draw.rect(
                self.screen,
                (0, 255, 0),
                (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE),
            )
        pygame.display.flip()

    def run(self):
        while self.running:
            self.process_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
