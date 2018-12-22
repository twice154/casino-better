import random

class Deck:
    def __init__(self):
        self.pointer = 0
        self.cards = [1,2,3,4,5,6,7,8,9,0,0,0,0] * 20
        random.shuffle(self.cards)
    
    def draw(self):
        self.pointer += 1
        return self.cards[self.pointer-1]

    def count_remain_cards(self):
        return len(self.cards) - self.pointer