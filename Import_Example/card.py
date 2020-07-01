class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    @property
    def suit(self):
        return self.suit

    @property
    def value(self):
        return self.value

    def show(self):
        print(f'{self.suit} and {self.value}')