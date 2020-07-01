from Import_Example.card import Card
import random
class Deck:
    suits=["spades","clubs","Diamond","hearts"]
    def __init__(self):
        self._cards=[]
        self.build()

    def build(self):
        for suit in self.suits:
            for value in range(0,12):
                self._cards=Card(suit,value)

    def show(self):
        for card in self._cards:
            card.show()

    def draw(self):
        if self._cards:
            self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

