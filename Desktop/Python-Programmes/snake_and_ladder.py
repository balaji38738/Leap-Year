import random

print("Snake And Ladder")
print("----------------")
START = 0
print("Starting position is", START)

class SnakeAndLadder:
    def dice_roll(self):
        return random.randint(1, 6)

    def print_dice_value(self):
        print(f"Dice value is: {self.dice_roll()}")

class Player:
    def __init__(self, name):
        self.__position = START
        self.__name = name

    def get_position(self):
        return self.__position

    def set_position(self, position):
        if position >= 0 and position <= 100:
            self.__position = position

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


snake_ladder = SnakeAndLadder()
snake_ladder.print_dice_value()
    