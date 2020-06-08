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

snake_ladder = SnakeAndLadder()
snake_ladder.print_dice_value()
    