from board import Board # import the board

def main(): # main game loop
    board = Board()
    player_turn = True
    game_over = False

    while not game_over:
        board.draw()
        print('Your turn:')
        board.play_turn()
        if board.is_full():
            board.draw() # maybe a custom game over scene over the board in the future?
            print("The board is full. It's a draw")
            game_over = True
            break

        board.draw()
        print("CPU's turn:")
        board.cpu_easy_turn(board)
        if board.is_full():
            board.draw()
            print("The board is full. It's a draw")
            game_over = True
            break


if __name__ == "__main__":
    main()