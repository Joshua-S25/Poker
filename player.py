class Player():
    def __init__(self):
        self.chips = 100

    def raise_bid(self, amount):
        self.chip -= amount

    def call(self, bid):
        self.chip -= bid

    def all_in(self):
        self.chip = 0