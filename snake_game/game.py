# snake_game/game.py
import sys

import pygame

from snake_game.settings import BLOCK_SIZE, FPS, HEIGHT, WIDTH
from snake_game.utils import get_ball_position


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
        self.ball = get_ball_position(self.snake)
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

        # Check if the snake has eaten the ball
        if new_head == self.ball:
            # Increase score and generate new ball position
            if not hasattr(self, "score"):
                self.score = 0
            self.score += 10
            from snake_game.utils import get_ball_position

            self.ball = get_ball_position(self.snake)
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill((0, 0, 0))
        # Draw ball (food)
        ball_center = (self.ball[0] + BLOCK_SIZE // 2, self.ball[1] + BLOCK_SIZE // 2)
        pygame.draw.circle(self.screen, (255, 255, 0), ball_center, BLOCK_SIZE // 2)

        # Draw snake
        for segment in self.snake:
            pygame.draw.rect(
                self.screen,
                (0, 255, 0),
                (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE),
            )

        # Display score
        font = pygame.font.SysFont("Arial", 28, bold=True)
        score_surface = font.render(
            f"Score: {getattr(self, 'score', 0)}", True, (255, 255, 255)
        )
        self.screen.blit(score_surface, (10, 10))

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
