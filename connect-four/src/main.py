from board import Board # import the board

def main(): # main game loop
    board = Board()
    while True:
        board.draw()
        board.play_turn()

if __name__ == "__main__":
    main()