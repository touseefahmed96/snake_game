# Snake Ball Eater

Snake Ball Eater is a modern twist on the classic snake game built using Python and Pygame. Guide your snake to eat balls, grow longer, and avoid collisions while enjoying dynamic visuals and smooth gameplay.

## Features

- **Dynamic Gameplay:** 
  - A growing snake that consumes balls to increase both its length and score.
- **Collision Detection:**
  - The game ends if the snake collides with the walls or itself.
- **Visually Enhanced:**
  - A gradient background creates a dynamic visual experience.
  - The snake features a gradient effect along its body.
- **Game Over Screen:**
  - When the game ends, a dedicated screen displays your score and provides options to restart or quit.
- **Modular Codebase:**
  - The project is organized into modules to facilitate easy maintenance and future enhancements.

## Project Structure

```
snake_ball_eater/
├── snake_game/
│   ├── __init__.py          # Package initializer
│   ├── main.py              # Entry point for the game
│   ├── game.py              # Contains game logic and the main loop
│   ├── settings.py          # Game settings and constants
│   └── utils.py             # Utility functions (e.g., gradients, random positions)
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies (Pygame)
└── .gitignore               # For Github
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/touseefahmed96/snake_ball_eater.git
   cd snake_ball_eater
   ```

2. **Install Dependencies:**

   Ensure you have Python 3.x installed. Then install the required packages with:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

To launch the game, run:

```bash
python -m snake_game.main
```

**Controls:**

- **Arrow Keys:** Steer the snake.
- **Game Over Screen:** Press **R** to restart or **Q** to quit.

## Future Enhancements

- **High Score System:** Track and display the best scores.
- **Multiple Levels:** Add different levels with increasing difficulty.


## Acknowledgements

- Built with [Pygame](https://www.pygame.org/).
- Inspired by classic snake games.
