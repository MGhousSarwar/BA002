import random
import cmath


class MarbleGame:
    def __init__(self, n):
        self.n = n
    def init(self):
        return self.n
    def checkEnd(self, marble):
        return True if marble == 0 else False
    def winCheck(self, marble, player):
        if marble == 0:
            if player == 1:
                return float('-inf')
            else:
                return float('+inf')
    def options(self, marble):
        if marble >= 3:
            return [1,2,3]
        return range(1, marble+1)
    def successor(self, marble, action):
        if action > marble:
            return 0
        return marble - action
def minimax(game, marble, player):
    def recursion(marble, player):
        if game.checkEnd(marble) == True:
            return (game.winCheck(marble, player), None)
        if dp in(marble, player):
            return dp[(marble, player)]
        choices = [(recursion(game.successor(marble, option), -1*player)[0], option) for option in game.options(marble)]
        if player == +1:
            val = max(choices)
        else:
            val = min(choices)
        dp[(marble, player)] = val
        return val
    value, option = recursion(marble, player)
    return (value, option)
dp = {}
if __name__ == "__main__":
    game = MarbleGame(15)

    marble = game.init()
    print("Finish The Marbles To Win The Game")
    while (marble > 0):
        action = 0
        print ("marbles remaining ", marble)
        while (action not in [1,2,3]) and marble - action >= 0:
            action = int(input("Choose action from 1,2,3:"))

        marble -= action
        print ("You take ",action)
        print ("marbles remaining ", marble)
        print ("")
        if marble == 0:
            print ("You won!")
            break
        val, act = minimax(game, marble, 1)
        marble -= act
        print ("AI takes ", act)
        if marble == 0:  
            print ("You Lost!")
