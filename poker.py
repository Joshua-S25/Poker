from deck import Deck
# ♣♥♦♠

deck = Deck()

def intro():
    print(" = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
           "|                WELCOME TO THE TEXAS HOLD 'EM                  |\n",
           "= ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
           "                                                                 \n",
           "                    Would you like to Play?                      \n",
           "                          ( Y / N )                              \n")
    play = input("                               ")

    while(play not in ['Y', 'y', 'n', 'N', 'exit', 'EXIT']):
        print("             Sorry, that's not an answer. Try again: ")
        play = input("                               ")


    if((play == 'N' or play == 'n') or (play == 'EXIT' or play == 'exit')):
        print("                    Maybe next time... Goodbye")
        return False
    else:
        return True

def main():

    if(intro() == False):
        return

    print("Dealing your cards...")


main()



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