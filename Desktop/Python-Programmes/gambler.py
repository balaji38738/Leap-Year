import random

#Constants
WIN, LOSS = 1, 0

class Gambler:
    def __init__(self, amount, bet, goal):
        self.__amount = amount
        self.__BET = bet
        self.__GOAL = goal
        self.__win_count = 0
        self.__loss_count = 0

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_bet(self):
        return self.__BET
    
    def get_goal(self):
        return self.__GOAL

    def get_win_count(self):
        return self.__win_count
    
    def increment_win_count(self):
        self.__win_count += 1
    
    def get_loss_count(self):
        return self.__loss_count
    
    def increment_loss_count(self):
        self.__loss_count += 1


class GamblingGame:
    def __init__(self, gambler):
        self.__gambler = gambler

    def play_gambling(self):
        amount = self.__gambler.get_amount()
        while amount != 0 and amount < 200:
            gamble = random.choice([WIN, LOSS])
            if gamble == WIN:
                self.__gambler.set_amount(amount + 1)
                self.__gambler.increment_win_count()
            else:
                self.__gambler.set_amount(amount - 1)
                self.__gambler.increment_loss_count()
            amount = self.__gambler.get_amount()
        if amount == self.__gambler.get_goal():
            print("Goal reached")
        else:
            print("Broke")
        print("Gambler won ", self.__gambler.get_win_count(), " times")
        print("Gambler lost ", self.__gambler.get_loss_count(), " times")

gambler = Gambler(100, 1, 200)
gambling_game = GamblingGame(gambler)
gambling_game.play_gambling()