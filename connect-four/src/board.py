import random

class Board: # define class Board

    empty_cell = '.'
    player_piece = 'X'
    oponent_piece = '0' # constants for pieces and cells

    def __init__(self):
        self.rows = 6 # define number of rows
        self.columns = 7 # define number of columns
        self.board = [] # define the board as an empty list to be filled

        for i in range(self.rows): 
            self.board.append([self.empty_cell] * self.columns) # for every row, draw a cell in each column

    def draw(self): # draw method to pribt the board

        # column numbers
        print(' ', end='') # first space for alignment
        for column in range(self.columns):
            print(f'{column+1 } ', end='')
        print()

        # draw the board
        for row in self.board:
            print(' ' + ' '.join(row)) # joins all elements in each row with a the necessary spaces for alignment

    def is_full(self):  # function to check if board is fulla nd stop the game
        for column in range(self.columns):
            if self.board[0][column] == self.empty_cell: # look for empty cells
                return False # theres empty cell, return false and dont stop the game
        return True # theres NOT empty cells left, return true and stop the game

    def insert_piece(self, column): # insert player piece
        
        column = column -1 # 0-based adjustment
        if column < 0 or column >= self.columns: # check if column is valid
            return False
        
        for row in range(self.rows -1, -1, -1): # iterate from bottom to top
            if self.board[row][column] == self.empty_cell:
                self.board[row][column] = self.player_piece
                return True
        
        return False # if column is full
    
    def insert_oponent_piece(self, column): # insert rivals piece
        
        column = column -1 # 0-based adjustment
        if column < 0 or column >= self.columns: # check if column is valid
            return False
            
        for row in range(self.rows -1, -1, -1): # iterate from bottom to top
            if self.board[row][column] == self.empty_cell:
                self.board[row][column] = self.oponent_piece
                return True
            
        return False # if column is full
    
    def play_turn(self): # the whole logic to play a turn and place a piece 
        while True: 
            try:
                column = int(input('Select a column (0-6): ')) # user input as int
                
                if column == 1: # check column input
                    if self.insert_piece(column): # put the piece at the selected column
                        break # halt the loop
                    else:
                        print('Column is full. Try another column')

                elif column == 2:
                    if self.insert_piece(column):
                        break
                    else:
                        print('Column is full. Try another column')

                elif column == 3:
                    if self.insert_piece(column):
                        break
                    else:
                        print('Column is full. Try another column')

                elif column == 4:
                    if self.insert_piece(column):
                        break
                    else:
                        print('Column is full. Try another column')

                elif column == 5:
                    if self.insert_piece(column):
                        break
                    else:
                        print('Column is full. Try another column')

                elif column == 6:
                    if self.insert_piece(column):
                        break
                    else:
                        print('Column is full. Try another column')

                elif column == 7:
                    if self.insert_piece(column):
                        break
                    else:
                        print('Column is full. Try another column')

                else:
                    print('Please enter a valid number')

            except ValueError: # error handliing for the input
                print('Please enter a number')
    
    def cpu_easy_turn(self): # easy mode to play against cpu, places a random piece at a random column
        
        while True:
            column = random.choice(range(8))

            if column == 1: # check column input
                if self.insert_oponent_piece(column): # put the piece at the selected column
                    break # halt the loop

            elif column == 2:
                if self.insert_oponent_piece(column):
                    break
                
            elif column == 3:
                if self.insert_oponent_piece(column):
                    break
                
            elif column == 4:
                if self.insert_oponent_piece(column):
                    break
                
            elif column == 5:
                if self.insert_oponent_piece(column):
                    break
                
            elif column == 6:
                if self.insert_oponent_piece(column):
                    break
                
            elif column == 7:
                if self.insert_oponent_piece(column):
                    break

    def cpu_normal_turn(): # cpu actually thinks whats doing, always gonna try to win or avoid you winning. (uses minimax algorithm)
        pass

    def cpu_hard_turn(): # allegedly a challenge, cpus a couple turns ahead. look for more comlpex alorithms
        pass
    
    def check_win(self): # checks when four pieces of the same type are in a row and declares the winning piece (which declares a winner)
        # check horizontal
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if (self.board[row][col] != '.' and
                    self.board[row][col] == self.board[row][col + 1] == 
                    self.board[row][col + 2] == self.board[row][col + 3]):
                    return True, self.board[row][col]  # returns win_found(true) and winning_piece(player)

        # check vertical
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if (self.board[row][col] != '.' and
                    self.board[row][col] == self.board[row + 1][col] == 
                    self.board[row + 2][col] == self.board[row + 3][col]):
                    winner = self.board[row][col]
                    return True, winner

        # check diagonal (right to left)
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if (self.board[row][col] != '.' and
                    self.board[row][col] == self.board[row - 1][col + 1] ==
                    self.board[row - 2][col + 2] == self.board[row - 3][col + 3]):
                    winner = self.board[row][col]
                    return True, winner

        # check diagonal (left ro right)
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if (self.board[row][col] != '.' and
                    self.board[row][col] == self.board[row + 1][col + 1] ==
                    self.board[row + 2][col + 2] == self.board[row + 3][col + 3]):
                    winner = self.board[row][col]
                    return True, winner

        return False, None  # no win found