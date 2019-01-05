import random

class Better:
    def __init__(self):
        self.money = 0
        self.cutMoney = 2
        self.discardMoney = -60

        self.isPlayerWinBefore = False
        self.strokeHistory = 0

        self.betMoney = 1
        self.betPortion = [0,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    def bet(self):
        self.money -= self.betMoney * self.betPortion[self.strokeHistory]
        print(self.betMoney * self.betPortion[self.strokeHistory])
        return True, self.betMoney * self.betPortion[self.strokeHistory]


    def get_info_from_game(self, isPlayerWin, bettingMoney, reward):
        if reward != 0:
            self.money += bettingMoney
            self.money += reward
        else:
            pass

        if self.strokeHistory == 0:
            self.isPlayerWinBefore = isPlayerWin
            self.strokeHistory += 1
        else:
            if self.isPlayerWinBefore == isPlayerWin:
                self.strokeHistory += 1
            else:
                self.isPlayerWinBefore = not self.isPlayerWinBefore
                self.strokeHistory = 1

    def game_end_signal(self):
        if self.money >= self.cutMoney or self.money <= self.discardMoney :
            return True
        else:
            return False

# 1: Player, 2: Banker
# minMoney = 0
for i in range(100000):
    better = Better()
    while True:
        print("====================================================================================================")
        print("Better's money before bet", better.money)
        numberOneSelect, howMuch = better.bet()
        print("Is better bet to 1", numberOneSelect)
        print("How much better bet", howMuch)
        randomNumber = random.randint(1, 2)
        print("randomNumber is", randomNumber)

        if randomNumber == 1:
            if numberOneSelect:
                better.get_info_from_game(True, howMuch, howMuch)
            # else:
            #     better.get_info_from_game(True, howMuch, 0)
        else:
            if numberOneSelect:
                better.get_info_from_game(False, howMuch, 0)
            # else:
            #     better.get_info_from_game(False, howMuch, 0.95)

        # if better.money < minMoney:
        #     minMoney = better.money
        print("Better's money after one step", better.money)

        if better.game_end_signal():
            print("Better's final money", better.money)
            # print("Better's minimum money", minMoney)
            f = open("./result.txt", "a")
            f.write(str(better.money) + "\n")
            f.close()
            # minMoney = 0
            break
