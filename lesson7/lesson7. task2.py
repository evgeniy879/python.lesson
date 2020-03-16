from abc import ABC, abstractmethod


class Clothes(ABC):
    pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def coat(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def suit(self):
        return 2 * self.height + 0.3


coat = Coat(46)
suit = Suit(189)

cost_coat = float(coat.coat)
cost_suit = float(suit.suit)

print(f'общий расход на пошив одежды составил {cost_coat + cost_suit: 0.5}')
