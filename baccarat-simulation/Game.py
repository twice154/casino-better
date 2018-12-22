import Deck
import Player
import Better
import time

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
        self.player.flush_hand()
        self.banker.flush_hand()
        print("=================================================")

        # betting stage
        print("Better's money before bet", self.better.money)
        whoYouSelect, howMuch = self.better.bet()  # whoYouSelect True -> select player win
        print("Is better bet to player", whoYouSelect)
        print("How much better bet", howMuch)
        print("Better's money after bet", self.better.money)
        print("Deck", self.deck.cards[self.deck.pointer:])

        # draw cards
        self.player.get_hand(self.deck.draw())
        self.banker.get_hand(self.deck.draw())
        self.player.get_hand(self.deck.draw())
        self.banker.get_hand(self.deck.draw())
        print("Player's hand at first draw", self.player.hand)
        print("Banker's hand at first draw", self.banker.hand)
        print("Deck", self.deck.cards[self.deck.pointer:])

        # calculate scores
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
        print("Player's hand at second draw", self.player.hand)
        print("Banker's hand at second draw", self.banker.hand)
        
        # reward calculation
        if self.player.calc_hand() > self.banker.calc_hand():
            print("Player wins")
            if whoYouSelect:
                self.better.get_info_from_game(True, howMuch, howMuch, self.gameStep)
            else:
                self.better.get_info_from_game(True, howMuch, 0, self.gameStep)
        elif self.player.calc_hand() == self.banker.calc_hand():
            print("Ties")
            self.better.currrentGameStep = self.gameStep
            self.better.money += howMuch
        else:
            print("Banker wins")
            if whoYouSelect:
                self.better.get_info_from_game(False, howMuch, 0, self.gameStep)
            else:
                self.better.get_info_from_game(False, howMuch, howMuch * 0.95, self.gameStep)
        print("Better's money", self.better.money)
        
        # check game end
        if self.deck.count_remain_cards() < 6 or self.better.game_end_signal():
            self.better.print_money()
            self.endFlag = True

game = Game()

for i in range(1000):
    game = Game()

    while not game.endFlag:
        game.game_next_step()
