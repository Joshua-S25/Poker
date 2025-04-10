from deck import Deck
# ♣♥♦♠

deck = Deck()

def blank_screen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

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
    
def pre_flop(hand):
    print(" = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
          "                                                                  \n",
          "                            Player 2                              \n",
          "                            **    **                              \n",
          "                                                                  \n",
          "                       **  **  **  **  **                         \n",
          "                                                                  \n",
          f"                            {hand[0]}    {hand[1]}               \n",
          "                            Player 1                              \n",
          "                                                                  \n",
          " = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
        )

def the_turn(hand, d):
    print(" = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
          "                                                                  \n",
          "                            Player 2                              \n",
          "                            **    **                              \n",
          "                                                                  \n",
          f"                       {d[0]}  {d[1]}  {d[2]}  **  **            \n",
          "                                                                  \n",
          f"                            {hand[0]}    {hand[1]}               \n",
          "                            Player 1                              \n",
          "                                                                  \n",
          " = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
        )

def main():

    if(intro() == False):
        return

    blank_screen()
    print("Dealing your cards...")
    
    deck.shuffle()
    hands = deck.deal(2)
    
    playerOneHand = hands[0]
    playerTwoHand = hands[1]

    pre_flop(playerOneHand)

    print(playerOneHand)
    print(playerTwoHand)

    table_hand = []
    i = 0
    while(i < 3):
        cardDrawn = deck.draw()
        table_hand.append(cardDrawn)
        i += 1

    

    

    the_turn(playerOneHand, table_hand)

    print(playerOneHand)
    print(playerTwoHand)
    print(table_hand)


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