import random

class Deck:

    def __init__(self, decks):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 * decks
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
