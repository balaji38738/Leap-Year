import numpy as np

print("-------Tic Tac Toe-------")
user_char = "x"
comp_char = "o"
filled_cells = 0

board = np.empty((3,3), dtype=str)

def reset_board():
    print("\nNew game starts")
    global filled_cells
    filled_cells = 0
    for row in range(3):
        for column in range(3):
            board[row][column] = " "

reset_board()