import Deck
import Player
import Better
import matplotlib.pyplot as plt

class Game:
    def __init__(self):
        self.deck = Deck.Deck()
        self.player = Player.Player(True)
        self.banker = Player.Player(False)
        self.better = Better.Better()

        self.gameStep = 0

        self.endFlag = False
    
    def game_next_step(self):
        self.gameStep += 1

        whoYouSelect, howMuch = self.better.bet()

        self.player.get_hand(self.deck.draw())
        self.banker.get_hand(self.deck.draw())
        self.player.get_hand(self.deck.draw())
        self.banker.get_hand(self.deck.draw())

        if self.player.calc_hand() == 8 or self.player.calc_hand() == 9 or self.banker.calc_hand() == 8 or self.banker.calc_hand() == 9:
            pass
        elif self.player.calc_hand() == 6 or self.player.calc_hand() == 7:
            if self.banker.calc_hand() == 6 or self.banker.calc_hand() == 7:
                pass
            else:
                self.banker.get_hand(self.deck.draw())
        else:
            thirdPlayerCard = self.deck.draw()
            self.player.get_hand(thirdPlayerCard)

            if self.banker.calc_hand() == 0 or self.banker.calc_hand() == 1 or self.banker.calc_hand() == 2:
                self.banker.get_hand(self.deck.draw())
            elif self.banker.calc_hand() == 3:
                if thirdPlayerCard == 8:
                    pass
                else:
                    self.banker.get_hand(self.deck.draw()) 
            elif self.banker.calc_hand() == 4:
                if thirdPlayerCard == 0 or thirdPlayerCard == 1 or thirdPlayerCard == 8 or thirdPlayerCard == 9:
                    pass
                else:
                    self.banker.get_hand(self.deck.draw())
            elif self.banker.calc_hand() == 5:
                if thirdPlayerCard == 4 or thirdPlayerCard == 5 or thirdPlayerCard == 6 or thirdPlayerCard == 7:
                    self.banker.get_hand(self.deck.draw())
                else:
                    pass
            elif self.banker.calc_hand() == 6:
                if thirdPlayerCard == 6 or thirdPlayerCard == 7:
                    self.banker.get_hand(self.deck.draw())
                else:
                    pass
            elif self.banker.calc_hand() == 7:
                pass
            else:
                pass
        
        if self.player.calc_hand() > self.banker.calc_hand():
            if whoYouSelect:
                self.better.get_info_from_game(True, howMuch * 2, self.gameStep)
            else:
                self.better.get_info_from_game(True, 0, self.gameStep)
        elif self.player.calc_hand() == self.banker.calc_hand():
            self.better.currrentGameStep = self.gameStep
            self.better.money += howMuch
        else:
            if whoYouSelect:
                self.better.get_info_from_game(False, 0, self.gameStep)
            else:
                self.better.get_info_from_game(False, howMuch * 1.95, self.gameStep)
        
        if self.deck.count_remain_cards() < 6 or self.better.game_end_signal():
            self.better.print_money()
            self.endFlag = True

game = Game()

for i in range(100):
    game = Game()

    while not game.endFlag:
        game.game_next_step()