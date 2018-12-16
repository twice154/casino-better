import Deck
import Player
import Banker
import Better

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(True)
        self.banker = Player(False)
        self.better = Better()
    
    def start(self):
