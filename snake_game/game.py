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

        # Check collision with walls
        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
        ):
            self.running = False  # Or set a game_over flag

        # Check collision with self
        if new_head in self.snake:
            self.running = False

        self.snake.insert(0, new_head)

        if new_head == self.ball:
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

    def handle_game_over(self):
        # Display Game Over screen
        font = pygame.font.SysFont("Arial", 50, bold=True)
        small_font = pygame.font.SysFont("Arial", 28, bold=True)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = small_font.render(f"Score: {self.score}", True, (255, 255, 0))
        restart_text = small_font.render(
            "Press R to Restart or Q to Quit", True, (255, 255, 255)
        )

        self.screen.fill((0, 0, 0))
        self.screen.blit(
            game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3)
        )
        self.screen.blit(
            score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 3 + 60)
        )
        self.screen.blit(
            restart_text,
            (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 3 + 120),
        )
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                        self.reset_game()
                    elif event.key == pygame.K_q:
                        waiting = False
                        self.running = False

    def run(self):
        while self.running:
            self.process_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        # Game over loop
        self.handle_game_over()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
