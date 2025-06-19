from board import Board # import the board settings from the file

def main(): # main game loop
    board = Board()
    # player_turn = True
    game_over = False
    game_diff = str(input('Choose difficulty: [easy, normal, hard]').lower) # game difficulty selection

    if game_diff == 'easy':
        while not game_over:
            board.draw() # draw current board

            # player turn
            print('Your turn:')
            board.play_turn()
            win_found, winner = board.check_win() # two variables at one 'cause function returns two values

            if win_found: # check if player won
                board.draw() # show board state
                if winner == board.player_piece: # checks if the piece that won is yours
                    print('You win!')
                else:
                    print('CPU wins...') # conditions to win met but not your piece, cpu wins
                game_over = True # halts the game
                break

            if board.is_full(): # check if board is full
                board.draw() # maybe a custom game over scene over the board in the future?
                print("The board is full. It's a draw")
                game_over = True
                break
            
            # cpu turn
            print("CPU's turn:")
            board.cpu_easy_turn()
            win_found, winner = board.check_win()

            if win_found: # the same process but at cpus turn
                board.draw()
                if winner == board.player_piece:
                    print("You win!")
                else:
                    print('CPU wins...')
                game_over = True
                break

    elif game_diff == 'Normal':

        while not game_over:
            board.draw()
            print('Your turn:')
            board.play_turn()
            if board.is_full():
                board.draw() 
                print("The board is full. It's a draw")
                game_over = True
                break

            board.draw()
            print("CPU's turn:")
            board.cpu_normal_turn()
            if board.is_full():
                board.draw()
                print("The board is full. It's a draw")
                game_over = True
                break

    elif game_diff == 'Hard':

        while not game_over:
            board.draw()
            print('Your turn:')
            board.play_turn()
            if board.is_full():
                board.draw() 
                print("The board is full. It's a draw")
                game_over = True
                break

            board.draw()
            print("CPU's turn:")
            board.cpu_hard_turn()
            if board.is_full():
                board.draw()
                print("The board is full. It's a draw")
                game_over = True
                break


if __name__ == "__main__":
    main()