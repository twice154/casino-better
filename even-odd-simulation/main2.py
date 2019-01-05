import random
import matplotlib.pyplot as plt

class Better:
    def __init__(self):
        self.money = 0
        self.cutMinMoney = 2
        # self.cutMaxMoney = 3
        self.discardMoney = -64
        # self.breakEvenPoint = False  # (-)에서 (+)로 전환되었을 때 켜짐

        # self.isPlayerWinBefore = False
        self.strokeHistory = 0
        # self.strokeHistoryForBEP = 1

        self.betMoney = 1
        self.betPortion = [0,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        # self.oldBetPortion = [0,0,1,2,3,8,17,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37]
        # self.newBetPortion = [0,0,0,0,0,0,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]

        # self.trashFrequency = 5
        # self.trashMoney = 1

        # self.currentGameStep = 0
        # self.finalBetStep = 0
    
    def bet(self):
        # if self.strokeHistory < 2:
        #     # if self.currentGameStep - self.finalBetStep == self.trashFrequency:
        #     #     self.money -= self.trashMoney
        #     #     self.finalBetStep = self.currentGameStep + 1
        #     #     return self.isPlayerWinBefore, self.trashMoney
        #     # else:
        #     return self.isPlayerWinBefore, 0
        # else:
        #     if self.breakEvenPoint:
        #         if self.strokeHistory >= 6:
        #             self.money -= self.betMoney * self.newBetPortion[self.strokeHistory]
        #             # print(self.betMoney * self.newBetPortion[self.strokeHistory])
        #             # self.finalBetStep = self.currentGameStep + 1
        #             return self.isPlayerWinBefore, self.betMoney * self.newBetPortion[self.strokeHistory]
        #         else:
        #             self.money -= self.betMoney * self.oldBetPortion[self.strokeHistoryForBEP]
        #             # print(self.betMoney * self.oldBetPortion[self.strokeHistoryForBEP])
        #             # self.strokeHistoryForNewBet += 1
        #             # self.finalBetStep = self.currentGameStep + 1
        #             return self.isPlayerWinBefore, self.betMoney * self.oldBetPortion[self.strokeHistoryForBEP]
        #     else:
        #         self.money -= self.betMoney * self.oldBetPortion[self.strokeHistory]
        #         # print(self.betMoney * self.oldBetPortion[self.strokeHistory])
        #         # self.finalBetStep = self.currentGameStep + 1
        #         return self.isPlayerWinBefore, self.betMoney * self.oldBetPortion[self.strokeHistory]
        self.money -= self.betMoney * self.betPortion[self.strokeHistory]
        print(self.betMoney * self.betPortion[self.strokeHistory])
        return True, self.betMoney * self.betPortion[self.strokeHistory]


    def get_info_from_game(self, isPlayerWin, bettingMoney, reward):
        # if self.money + bettingMoney < 0 and self.money + bettingMoney + reward >= 0:
        #     self.breakEvenPoint = True
        #     self.strokeHistoryForBEP = 1

        if reward != 0:
            self.money += bettingMoney
            self.money += reward
        else:
            pass
        # self.currentGameStep = gameStep

        if self.strokeHistory == 0:
            self.isPlayerWinBefore = isPlayerWin
            self.strokeHistory += 1
        else:
            if self.isPlayerWinBefore == isPlayerWin:
                self.strokeHistory += 1
                # self.strokeHistoryForBEP += 1
            else:
                self.isPlayerWinBefore = not self.isPlayerWinBefore
                # self.breakEvenPoint = False
                self.strokeHistory = 1

    def game_end_signal(self):
        if self.money >= self.cutMinMoney or self.money <= self.discardMoney :
            return True
        else:
            return False
    
    # def print_money(self):
    #     print("Better's final ending money", self.money)
    #     f = open("./result.txt", "a")
    #     f.write(str(self.money) + "\n")
    #     f.close()

# 1: Player, 2: Banker
# minMoney = 0
for i in range(500000):
    better = Better()
    minMoney = 0
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

        if better.money < minMoney:
            minMoney = better.money

        if better.game_end_signal():
            print("Better's final money", better.money)
            # print("Better's minimum money", minMoney)
            f = open("./result.txt", "a")
            f.write(str(better.money) + "\n")
            f.close()
            # minMoney = 0
            break
