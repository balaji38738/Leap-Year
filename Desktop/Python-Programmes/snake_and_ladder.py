import random

print("Snake And Ladder")
print("----------------")
START = 0
FINISH = 100
print("Starting position is", START)

class SnakeAndLadder:
    def __init__(self, players_list):
        self.__players_list = players_list
        self.__current_player_index = 0

    def dice_roll(self):
        return random.randint(1, 6)

    def increment_position(self, player, dice_value):
        print("\nPlayer:", player.get_name(), "| Move: Ladder | Dice value:", dice_value)
        position = player.get_position() + dice_value
        player.set_position(position)

    def decrement_position(self, player, dice_value):
        print("\nPlayer:", player.get_name(), "| Move: Snake | Dice value:", dice_value)
        position = player.get_position() - dice_value
        player.set_position(position)

    def no_play(self, player, dice_value):
        print("\nPlayer:", player.get_name(), "| Move: No play | Dice value:", dice_value)

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

    def print_positions(self):
        for player in self.__players_list:
            print(player.get_name(), ":", player.get_position())

    def change_turn(self):
        self.__current_player_index += 1
        self.__current_player_index %= len(self.__players_list)

    def get_current_player_index(self):
        return self.__current_player_index

    def get_unfinished_players(self):
         return list(filter(lambda player: player.get_position() != FINISH,
                    self.__players_list))
    
    def is_finished(self):
        unfinished_players = self.get_unfinished_players()
        return len(unfinished_players) == 1

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


players_list = (Player("Balaji"), Player("Sagar"))
snake_ladder = SnakeAndLadder(players_list)
rolls = 0
while not snake_ladder.is_finished():
    current_player = snake_ladder.get_current_player_index()
    print(players_list[current_player].get_name(), "'s turn", sep="")
    input("Press Enter to roll the dice: ")
    dice_value = snake_ladder.dice_roll()
    snake_ladder.move_player(players_list[current_player], dice_value)
    snake_ladder.print_positions()
    snake_ladder.change_turn()
    rolls += 1
print("Total dice rolls =", rolls)
lost_player = snake_ladder.get_unfinished_players()[0]
print(lost_player.get_name(), "lost the game")