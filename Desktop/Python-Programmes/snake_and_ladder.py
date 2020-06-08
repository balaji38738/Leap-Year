import random

print("Snake And Ladder")
print("----------------")
START = 0
FINISH = 100
print("Starting position is", START)

class SnakeAndLadder:
    def __init__(self, player):
        self.__player = player

    def dice_roll(self):
        return random.randint(1, 6)

    def increment_position(self, player, dice_value):
        print("Ladder")
        position = player.get_position() + dice_value
        player.set_position(position)

    def decrement_position(self, player, dice_value):
        position = player.get_position() - dice_value
        print("Snake")
        player.set_position(position)

    def no_play(self, player, dice_value):
        print("No play")
        pass

    def move_player(self, player, dice_value):
        SNAKE = 1
        LADDER = 2
        NO_PLAY = 3
        move_options = {
           LADDER: self.increment_position,
           SNAKE: self.decrement_position,
           NO_PLAY: self.no_play
        }
        move = random.randint(1, 3)
        move_options[move](player, dice_value)

    def print_position(self, player):
        print(player.get_name(), player.get_position())


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


balaji = Player("Balaji")
snake_ladder = SnakeAndLadder(balaji)
rolls = 0
while balaji.get_position() != FINISH:
    dice_value = snake_ladder.dice_roll()
    snake_ladder.move_player(balaji, dice_value)
    snake_ladder.print_position(balaji)
    rolls += 1
print(rolls)

    