class Better:
    def __init__(self):
        self.money = 0
        self.cutMoney = 75
        self.breakEvenPoint = False

        self.isPlayerWinBefore = False
        self.strokeHistory = 0
        self.strokeHistoryForNewBet = 2

        self.betMoney = 5
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
                return self.trashMoney
        else:
            if self.breakEvenPoint:
                if self.strokeHistory >= 6:
                    self.money -= self.betMoney * self.newBetPortion[self.strokeHistory]
                    self.finalBetStep = self.currentGameStep + 1
                    return self.betMoney * self.newBetPortion[self.strokeHistory]
                else:
                    self.money -= self.betMoney * self.oldBetPortion[self.strokeHistoryForNewBet]
                    self.strokeHistoryForNewBet += 1
                    self.finalBetStep = self.currentGameStep + 1
                    return self.betMoney * self.oldBetPortion[self.strokeHistoryForNewBet]
            else:
                self.money -= self.betMoney * self.oldBetPortion[self.strokeHistory]
                self.finalBetStep = self.currentGameStep + 1
                return self.betMoney * self.oldBetPortion[self.strokeHistory]

    def get_info_from_game(self, isPlayerWin, reward, gameStep):
        if self.money < 0 and self.money + reward >= 0:
            self.breakEvenPoint = True
            self.strokeHistoryForNewBet = 2

        self.money += reward
        self.currentGameStep = gameStep

        if self.strokeHistory == 0:
            self.isPlayerWinBefore = isPlayerWin
            self.strokeHistory += 1
        else:
            if self.isPlayerWinBefore == isPlayerWin:
                self.strokeHistory += 1
            else:
                self.isPlayerWinBefore = not self.isPlayerWinBefore
                self.breakEvenPoint = False
                self.strokeHistory = 1

    def game_end_signal(self):
        if self.money >= 75:
            return True
        else:
            return False
