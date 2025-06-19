"""
Using references from: 
- https://www.datacamp.com/tutorial/minimax-algorithm-for-ai-in-python
- https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html
- https://stackoverflow.com/questions/71187789/why-my-connect4-minimax-doesnt-work-properly
- A.I. (Claude Sonet 3.5)

"""

def minimax(board, depth, is_maximizing, max_depth=0):  # added max_depth parameter to avoid infinite recursion and difficulty level management
    # maximum depth reached then stop thinking
    # print(f'Thinking with a depth index of {max_depth}') # debugging print (lots of thinking at 4...)
    if depth >= max_depth:
        return 0
        
    # get game state using board's existing check_win method
    win_found, winner = board.check_win()
    
    # terminal states
    if win_found:
        if winner == board.oponent_piece:  # CPU wins
            return 10 - depth  # prefer winning sooner
        elif winner == board.player_piece:  # Player wins
            return -10 + depth  # prefer losing later
    elif board.is_full():
        return 0
        
    if is_maximizing:
        best_score = float('-inf')
        for col in range(1, 8):
            if board.insert_oponent_piece(col):  # try move
                score = minimax(board, depth + 1, False, max_depth)
                # undo move
                for row in range(board.rows):
                    if board.board[row][col-1] != board.empty_cell:
                        board.board[row][col-1] = board.empty_cell
                        break
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for col in range(1, 8):
            if board.insert_piece(col):  # try move
                score = minimax(board, depth + 1, True, max_depth)
                # undo move
                for row in range(board.rows):
                    if board.board[row][col-1] != board.empty_cell:
                        board.board[row][col-1] = board.empty_cell
                        break
                best_score = min(score, best_score)
        return best_score

def get_best_move(board, max_depth=2):  # add max_depth parameter with default value
    best_score = float('-inf')
    best_col = 1
    
    print(f"CPU is thinking with depth {max_depth}...")
    
    for col in range(1, 8):
        if board.insert_oponent_piece(col):
            score = minimax(board, 0, False, max_depth)  # pass max_depth to minimax
            print(f"Evaluating column {col}: score = {score}")
            
            # undo move
            for row in range(board.rows):
                if board.board[row][col-1] != board.empty_cell:
                    board.board[row][col-1] = board.empty_cell
                    break
                    
            if score > best_score:
                best_score = score
                best_col = col
    
    print(f"CPU chose column {best_col}")
    return best_col