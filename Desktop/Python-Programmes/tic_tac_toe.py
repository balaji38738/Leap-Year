import numpy as np
import random

print("-------Tic Tac Toe-------")
user_char = "x"
comp_char = "o"
filled_cells = 0

board = np.empty((3,3), dtype=str)

#Starts a fresh board
def reset_board():
    print("\nNew game starts")
    global filled_cells
    filled_cells = 0
    for row in range(3):
        for column in range(3):
            board[row][column] = " "

def coin_toss():
    face = random.choice(["HEAD", "TAIL"])
    if face == "HEAD":
        print("Your turn first")
    else:
        print("Computer's turn first")
    return face

def display_board():
    for row in range(3):
        for column in range(3):
            print(board[row, column], end=" ")
            if column != 2:
                print("|", end="")
        if row != 2:
            print("\n--------")
    print("\n")

def play_game():
    print("You are assigned", user_char)
    coin_toss()

reset_board()
display_board()
play_game()