class Better:
    def __init__(self):
        self.money = 0
        self.cutMoney = 150
        self.breakEvenPoint = False  # (-)에서 (+)로 전환되었을 때 켜짐

        self.isPlayerWinBefore = False
        self.strokeHistory = 0
        self.strokeHistoryForBEP = 1

        self.betMoney = 10
        self.oldBetPortion = [0,0,1,2,3,8,17,37,37,37,37]
        self.newBetPortion = [0,0,0,0,0,0,12,12,12,12,12,12,12,12,12]

        self.trashFrequency = 5
        self.trashMoney = 1

        self.currentGameStep = 0
        self.finalBetStep = 0
    
    def bet(self):
        if self.strokeHistory < 2:
            if self.currentGameStep - self.finalBetStep == self.trashFrequency:
                self.money -= self.trashMoney
                self.finalBetStep = self.currentGameStep + 1
                return self.isPlayerWinBefore, self.trashMoney
            else:
                return self.isPlayerWinBefore, 0
        else:
            if self.breakEvenPoint:
                if self.strokeHistory >= 6:
                    self.money -= self.betMoney * self.newBetPortion[self.strokeHistory]
                    # print(self.betMoney * self.newBetPortion[self.strokeHistory])
                    self.finalBetStep = self.currentGameStep + 1
                    return self.isPlayerWinBefore, self.betMoney * self.newBetPortion[self.strokeHistory]
                else:
                    self.money -= self.betMoney * self.oldBetPortion[self.strokeHistoryForBEP]
                    # print(self.betMoney * self.oldBetPortion[self.strokeHistoryForBEP])
                    # self.strokeHistoryForNewBet += 1
                    self.finalBetStep = self.currentGameStep + 1
                    return self.isPlayerWinBefore, self.betMoney * self.oldBetPortion[self.strokeHistoryForBEP]
            else:
                self.money -= self.betMoney * self.oldBetPortion[self.strokeHistory]
                # print(self.betMoney * self.oldBetPortion[self.strokeHistory])
                self.finalBetStep = self.currentGameStep + 1
                return self.isPlayerWinBefore, self.betMoney * self.oldBetPortion[self.strokeHistory]

    def get_info_from_game(self, isPlayerWin, bettingMoney, reward, gameStep):
        if self.money + bettingMoney < 0 and self.money + bettingMoney + reward >= 0:
            self.breakEvenPoint = True
            self.strokeHistoryForBEP = 1

        if reward != 0:
            self.money += bettingMoney
            self.money += reward
        else:
            pass
        self.currentGameStep = gameStep

        if self.strokeHistory == 0:
            self.isPlayerWinBefore = isPlayerWin
            self.strokeHistory += 1
        else:
            if self.isPlayerWinBefore == isPlayerWin:
                self.strokeHistory += 1
                self.strokeHistoryForBEP += 1
            else:
                self.isPlayerWinBefore = not self.isPlayerWinBefore
                self.breakEvenPoint = False
                self.strokeHistory = 1

    def game_end_signal(self):
        if self.money >= self.cutMoney:
            return True
        else:
            return False
    
    def print_money(self):
        print("Better's final ending money", self.money)
        f = open("./result.txt", "a")
        f.write(str(self.money) + "\n")
        f.close()
