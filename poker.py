from Deck import Deck

deck = Deck()

deck.shuffle()


# Poker Rules and Route

## Pre-Flop
    # Deal Out - 2 Private cards to all players
    # First bettering Turn
        # Fold - Give up
        # Call - Match current highest bet
        # Raise - Increase bet
    # Turn Passes until bets are played or players fold

## The Flop
    # Three Community Cards - Revealed and face up on table
    # Another Round of betting

## The Turn
    # Fourth Community Card - Revealed
    # Another Round of Betting

## The River
    # Fifth Community Card - Revealed -> final card
    # Last round bets

## The Showdown
    # All reveal cards
    # Best 5-card hand using hole or community wins