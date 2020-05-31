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
            print("Your turn first")
        else:
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
                    winner = USER
                else:
                    winner = COMP



tic_tac_toe = TicTacToe()
tic_tac_toe.reset_board()
tic_tac_toe.display_board()
tic_tac_toe.play_game()