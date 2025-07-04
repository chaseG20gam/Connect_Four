# Connect Four

A school project implementing the classic Connect Four game in Python, featuring a graphical board, colored pieces, AI opponents, and game logging.

## Features

- **Graphical Board Drawing:** The game displays a Connect Four board in the terminal or GUI, with clear representation of columns and rows.
- **Colored Pieces:** Each player’s pieces are visually distinct using colors for easy identification.
- **Win Checking:** Automatic detection of win conditions (horizontal, vertical, and diagonal) after every move.
- **Difficulty Management:** Four difficulty levels—Easy, Normal, Hard, and Insane—adjust the AI’s strategy and depth of thinking.
- **Minimax Algorithm:** The AI uses the minimax algorithm to determine its moves. Higher difficulties allow the AI to look further ahead and make smarter decisions.
- **Modular Codebase:** The project is organized into multiple files and modules, demonstrating the use of imports, classes, and objects for clean, maintainable code.
- **Game Logger:** A logger records the progress and results of each game for analysis and debugging.

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/chaseG20gam/Connect_Four
    cd connect-four
    ```

### Running the Game

```bash
python main.py
```

Follow the on-screen instructions to select difficulty and start playing.

## Project Structure

```
connect-four/
├── board.py         # Board drawing and management
├── ai.py            # Minimax algorithm and AI logic
├── game.py          # Game loop and win checking
├── logger.py        # Game logging functionality
├── main.py          # Entry point
└── README.md
```

## How to Play

- Players take turns dropping pieces into columns.
- The first player to connect four of their pieces in a row (horizontally, vertically, or diagonally) wins.
- Play against the AI at your chosen difficulty.

## License

This project is for educational purposes.

---

*Developed as a school project to demonstrate object-oriented programming, AI algorithms, and modular Python design.*
