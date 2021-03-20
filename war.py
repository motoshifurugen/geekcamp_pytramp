class Deck:
    def __init__(self):
        self.inHandCards = [None,None,2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.usedCards = []

class Player:
    def __init__(self, name):
        self.name = name
        # 現在の勝利数
        self.numWins = 0
        self.deck = Deck()