import random

class Deck():
    def __init__(self):
        # Init a full 52 card deck
        # NOTE # '1' Cards represent 10s
        self.deck = [
            '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '1♣', 'J♣', 'Q♣', 'K♣', 'A♣',
            '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '1♠', 'J♠', 'Q♠', 'K♠', 'A♠',
            '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '1♥', 'J♥', 'Q♥', 'K♥', 'A♥',
            '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '1♦', 'J♦', 'Q♦', 'K♦', 'A♦'
        ]

    def __str__(self):
        return f"Deck() = {self.deck}"
    
    def __repr__(self):
        return f"newDeck = Deck()"
    
    def shuffle(self):
        # print(self.deck)  # Pre Shuffle

        i = 0
        while(i < 5):
            random.shuffle(self.deck)
            i += 1

        # print(self.deck)  # Post Shuffle
    
    def deal(self, numPlayers):
        dealt_hands = [[] for _ in range(numPlayers)]

        print(dealt_hands)
        i = 0
        
        while(i < 2):
            j = 0

            while(j < numPlayers):
                dealt_hands[j].append(self.draw())
                j += 1
            i += 1

        return dealt_hands
    
    def draw(self):
        card = self.deck.pop()

        return card
    
    def burn(self):
        self.deck.pop()