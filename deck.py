class Deck():
    def __init__(self):
        # Init a full 52 card deck
        self.deck = [
            '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '1C', 'JC', 'QC', 'KC', 'AC',
            '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '1S', 'JS', 'QS', 'KS', 'AS',
            '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '1H', 'JH', 'QH', 'KH', 'AH',
            '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '1D', 'JD', 'QD', 'KD', 'AD'
        ]

    def __str__(self):
        return f"Deck() = {self.deck}"
    
    def __repr__(self):
        return f"newDeck = Deck()"