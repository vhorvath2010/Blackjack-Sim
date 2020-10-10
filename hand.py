class Hand:

    def __init__(self, cards, soft):
        self.cards = cards
        self.soft = soft

    def should_split(self, dealer):
        if self.cards[0] == self.cards[1]:
            if self.cards[0] == 11 or self.cards[0] == 8:
                return True
            if self.cards[0] <= 3 and dealer <= 7:
                return True
            if 6 <= self.cards[0] <= 9 and dealer <= 6:
                return True
        return False

    def should_double(self, dealer):
        if self.cards[0] == self.cards[1] == 5 and dealer <= 9:
            return True
        if self.soft and 13 <= self.cards[0] + self.cards[1] <= 18 and 4 <= dealer <= 6:
            return True
        if 9 <= self.cards[0] + self.cards[1] <= 11 and 2 <= dealer <= 8:
            return True
        return False
