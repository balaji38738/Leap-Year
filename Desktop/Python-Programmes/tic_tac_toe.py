import numpy as np
import random

print("-------Tic Tac Toe-------")
user_char = "x"
comp_char = "o"
filled_cells = 0
TOTAL_COLUMNS = 3
TOTAL_ROWS = 3
USER = 0
COMP = 1

board = np.empty((3,3), dtype=str)

class TicTacToe:

    #Starts a fresh board
    def reset_board(self):
        print("\nNew game starts")
        global filled_cells
        filled_cells = 0
        for row in range(TOTAL_ROWS):
            for column in range(TOTAL_COLUMNS):
                board[row][column] = " "

    def coin_toss(self):
        face = random.choice(["HEAD", "TAIL"])
        if face == "HEAD":
            self.turn = USER
            print("Your turn first")
        else:
            self.turn = COMP
            print("Computer's turn first")
        return face

    def display_board(self):
        for row in range(TOTAL_ROWS):
            for column in range(TOTAL_COLUMNS):
                print(board[row, column], end=" ")
                if column != TOTAL_COLUMNS - 1:
                    print("|", end="")
            if row != TOTAL_ROWS - 1:
                print("\n--------")
        print("\n")

    #Starts a new game
    def play_game(self):
        print("You are assigned", user_char)
        self.coin_toss()

    #Checks equality of three cells & finds the winner if any
    def are_three_equal(
            self, cell1,
            cell2, cell3):
        if cell1 != " ":
            if cell1 == cell2 and cell2 == cell3:
                self.is_won = True
                if cell1 == user_char:
                    self.winner = USER
                else:
                    self.winner = COMP

    #Finds if anyone won
    def check_if_game_won(self):
        self.is_won = False
        for i in range(TOTAL_ROWS):

            #Method call to check equality of ith row 
            self.are_three_equal(board[i, 0], board[i, 1], board[i, 2])

            #Method call to check equality of ith column
            self.are_three_equal(board[0, i], board[1, i], board[2, i])
        
        #Method calls to check equality of diagonals
        self.are_three_equal(board[0, 0], board[1, 1], board[2, 2])
        self.are_three_equal(board[0, 2], board[1, 1], board[2, 0])

        if self.is_won == True:
            if self.winner == USER:
                print("You won")
            else:
                print("Computer won")
        elif filled_cells == TOTAL_ROWS * TOTAL_COLUMNS:
            print("Game Tie")

    def check_win_possibility(self, char):
        empty_cell_row, empty_cell_column = None, None
        for i in range(TOTAL_ROWS):

            #Finds single empty cell in ith row
            concat_cells = board[i, 0] + board [i, 1] + board[i, 2]
            if concat_cells == " " + char + char:
                empty_cell_row, empty_cell_column = i, 0
                break
            elif concat_cells == char + " " + char:
                empty_cell_row, empty_cell_column = i, 1
                break
            elif concat_cells == char + char + " ":
                empty_cell_row, empty_cell_column = i, 2
                break
            
            #Find single empty cell in ith column
            if empty_cell_row == None:
                concat_cells = board[0, i] + board[1, i] + board[2, i]
                if concat_cells == " " + char + char:
                    empty_cell_row, empty_cell_column = 0, i
                    break
                elif concat_cells == char + " " + char:
                    empty_cell_row, empty_cell_column = 1, i
                    break
                elif concat_cells == char + char + " ":
                    empty_cell_row, empty_cell_column = 2, i
                    break
            
        #Finds single empty cell in diagonal from top-left corner to bottom-right corner
        if empty_cell_row == None:
            concat_cells = board[0, 0] + board[1, 1] + board[2, 2]
            if concat_cells == " " + char + char:
                empty_cell_row, empty_cell_column = 0, 0
            elif concat_cells == char + " " + char:
                empty_cell_row, empty_cell_column = 1, 1
            elif concat_cells == char + char + " ":
                empty_cell_row, empty_cell_column = 2, 2
        
        #Finds single empty cell in diagonal from top-right corner to bottom-left corner
        if empty_cell_row == None:
            concat_cells = board[0, 2] + board[1, 1] + board[2, 0]
            if concat_cells == " " + char + char:
                empty_cell_row, empty_cell_column = 0, 2
            elif concat_cells == char + " " + char:
                empty_cell_row, empty_cell_column = 1, 1
            elif concat_cells == char + char + " ":
                empty_cell_row, empty_cell_column = 2, 0
        return empty_cell_row, empty_cell_column
    
    #Fills the cells & changes the turn
    def fill_cell(
            self, char,
            row, column):
        board[row, column] = char
        global filled_cells
        filled_cells += 1
        self.turn = (1 - self.turn)

    #Fills empty corner
    def fill_corner(self):
        is_empty_corner = True
        if board[0, 0] == " ":
            self.fill_cell(comp_char, 0, 0)
        elif board[0, 2] == " ":
            self.fill_cell(comp_char, 0, 2)
        elif board[2, 0] == " ":
            self.fill_cell(comp_char, 2, 0)
        elif board[2, 2] == " ":
            self.fill_cell(comp_char, 2, 2)
        else:
            is_empty_corner = False
        return is_empty_corner

    def fill_side(self):
        is_empty_side = True
        if board[0, 1] == " ":
            self.fill_cell(comp_char, 0, 1)
        elif board[1, 0] == " ":
            self.fill_cell(comp_char, 1, 0)
        elif board[1, 2] == " ":
            self.fill_cell(comp_char, 1, 2)
        elif board[2, 1] == " ":
            self.fill_cell(comp_char, 2, 1)
        else:
            is_empty_side = False
        return is_empty_side

tic_tac_toe = TicTacToe()
tic_tac_toe.reset_board()
tic_tac_toe.display_board()
tic_tac_toe.play_game()