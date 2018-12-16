class Player:
    def __init__(self, isPlayer):
        self.player = False
        self.banker = False
        self.hand = []

        if isPlayer:
            self.player = True
        else:
            self.banker = True
    
    def calc_hand(self):
        hand_value = 0
        for i in self.hand:
            hand_value += i
        hand_value = hand_value % 10

        return hand_value
    
    def flush_hand(self):
        self.hand = []
    
    def get_hand(self, num):
        self.hand += [num]