from board import Board # import the board settings from the file
from logger import log_game

def main(): # main game loop
    board = Board()
    # player_turn = True
    game_over = False # game status for control flow
    game_diff = str(input('Choose difficulty: [easy, normal, hard]')) # game difficulty selection
    player_name = str(input('Type your name: '))

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
                    log_game(player_name, game_diff, "win", '0') # logger function call
                else:
                    print('CPU wins...') # conditions to win met but not your piece, cpu wins
                    log_game(player_name, game_diff, "loss", '0')
                game_over = True # halts the game
                break

            if board.is_full(): # check if board is full
                board.draw() # maybe a custom game over scene over the board in the future?
                print("The board is full. It's a draw")
                log_game(player_name, game_diff, "draw", '0')
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
                    log_game(player_name, game_diff, "win", '0')
                else:
                    print('CPU wins...')
                    log_game(player_name, game_diff, "loss", '0')
                game_over = True
                break

    elif game_diff == 'normal':

        while not game_over:
            board.draw() # draw current board

            # player turn
            print('Your turn:')
            board.play_turn()
            win_found, winner = board.check_win()

            if win_found:
                board.draw()
                if winner == board.player_piece:
                    print('You win!')
                    log_game(player_name, game_diff, "win", '2')
                else:
                    print('CPU wins...')
                    log_game(player_name, game_diff, "loss", '2')
                game_over = True
                break

            if board.is_full(): 
                board.draw()
                print("The board is full. It's a draw")
                log_game(player_name, game_diff, "draw", '2')
                game_over = True
                break
            
            # cpu turn
            board.draw()
            print("CPU's turn:")
            board.cpu_normal_turn()
            win_found, winner = board.check_win()

            if win_found: # the same process but at cpus turn
                board.draw()
                if winner == board.player_piece:
                    print("You win!")
                    log_game(player_name, game_diff, "win", '2')
                else:
                    print('CPU wins...')
                    log_game(player_name, game_diff, "loss", '2')
                game_over = True
                break

    elif game_diff == 'hard':


        while not game_over:
            board.draw() # draw current board

            # player turn
            print('Your turn:')
            board.play_turn()
            win_found, winner = board.check_win()

            if win_found:
                board.draw() 
                if winner == board.player_piece:
                    print('You win!')
                    log_game(player_name, game_diff, "win", '4')
                else:
                    print('CPU wins...')
                    log_game(player_name, game_diff, "loss", '4')
                game_over = True 
                break

            if board.is_full():
                board.draw() 
                print("The board is full. It's a draw")
                log_game(player_name, game_diff, "draw", '4')
                game_over = True
                break
            
            # cpu turn
            board.draw()
            print("CPU's turn:")
            board.cpu_hard_turn()
            win_found, winner = board.check_win()

            if win_found: # the same process but at cpus turn
                board.draw()
                if winner == board.player_piece:
                    print("You win!")
                    log_game(player_name, game_diff, "win", '4')
                else:
                    print('CPU wins...')
                    log_game(player_name, game_diff, "loss", '4')
                game_over = True
                break

    else:
        print('Please, choose a valid option... [easy, normal, hard]')
        main() # return to the main function if input is wrong

if __name__ == "__main__":
    main()