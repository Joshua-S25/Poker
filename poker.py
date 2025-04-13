from deck import Deck
from player import Player
# ♣♥♦♠

deck = Deck()
player1 = Player()


### All of these are for terminal display purposes

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

def the_flop(hand, d):
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
    
def the_turn(hand, d):
    print(" = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
          "                                                                  \n",
          "                            Player 2                              \n",
          "                            **    **                              \n",
          "                                                                  \n",
          f"                       {d[0]}  {d[1]}  {d[2]}  {d[3]}  **        \n",
          "                                                                  \n",
          f"                            {hand[0]}    {hand[1]}               \n",
          "                            Player 1                              \n",
          "                                                                  \n",
          " = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
        )
    
def the_river(hand, d):
    print(" = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
          "                                                                  \n",
          "                            Player 2                              \n",
          "                            **    **                              \n",
          "                                                                  \n",
          f"                       {d[0]}  {d[1]}  {d[2]}  {d[3]}  {d[4]}    \n",
          "                                                                  \n",
          f"                            {hand[0]}    {hand[1]}               \n",
          "                            Player 1                              \n",
          "                                                                  \n",
          " = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
        )
    
def the_showdown(hand, d):
    print(" = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
          "                                                                  \n",
          "                            Player 2                              \n",
          f"                            {hand[1][0]}    {hand[1][1]}         \n",
          "                                                                  \n",
          f"                       {d[0]}  {d[1]}  {d[2]}  {d[3]}  {d[4]}    \n",
          "                                                                  \n",
          f"                            {hand[0][0]}    {hand[0][1]}         \n",
          "                            Player 1                              \n",
          "                                                                  \n",
          " = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ = ♠ = ♣ = ♥ = ♦ =\n",
        )

def play_turn():
    print("                                                                  \n",
          "      Raise           Call            Fold           All          \n",
          "                                                                  \n",)


### Parsing and Sorting combination

def parse(hand):
    RANK_ORDER = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9,
    '1': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    SUIT_ORDER = {
    '♣': 0, '♦': 1, '♥': 2, '♠': 3
    }

    parsed = []

    i = 0
    while(i < len(hand)):
        rank = RANK_ORDER[hand[i][0]]
        suit = SUIT_ORDER[hand[i][1]]
        parsed_card = (rank, suit)
        parsed.append(parsed_card)
        i += 1

    print(parsed)
    return parsed

def reparse(hand):
    RANK_LOOKUP = {
    2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
    7: '7', 8: '8', 9: '9',
    10: '1',
    11: 'J', 12: 'Q', 13: 'K', 14: 'A'
    }

    SUIT_LOOKUP = {
    0: '♣', 1: '♦', 2: '♥', 3: '♠'
    }

    sort_hold = []

    i = 0
    while(i < len(hand)):
        rank = RANK_LOOKUP[hand[i][0]]
        suit = SUIT_LOOKUP[hand[i][1]]
        reparsed_card = f"{rank}" + f"{suit}"
        sort_hold.append(reparsed_card)
        i += 1

    print(sort_hold)
    return sort_hold

def sort(hand):
    if(len(hand) == 1):
        return hand

    mid = len(hand) // 2

    l_hand = hand[:mid]
    r_hand = hand[mid:]

    l_sorted = sort(l_hand)
    r_sorted = sort(r_hand)

    sorted = []
    l = 0
    r = 0

    print("Here is the splits: ")
    print(l_sorted)
    print(r_sorted)
    print("")

    while(l < len(l_sorted) and r < len(r_sorted)):
        if l_sorted[l] < r_sorted[r]:
            sorted.append(l_sorted[l])
            l += 1
        else:
            sorted.append(r_sorted[r])
            r += 1

    while l < len(l_sorted):
        sorted.append(l_sorted[l])
        l += 1

    while r < len(r_sorted):
        sorted.append(r_sorted[r])
        r += 1

        
    print(sorted)
    return sorted

    
    
### Combination of checks to see if win conditions are met

def check_royal(hand):
    i = 0
    rf_check_diamond = 0
    rf_check_heart = 0
    rf_check_spade = 0
    rf_check_club = 0

    while(i < 7):
        if((hand[i] in ['1♦', 'J♦', 'Q♦', 'K♦', 'A♦'])):
            # print("Diamonds")
            rf_check_diamond += 1
        elif((hand[i] in ['1♥', 'J♥', 'Q♥', 'K♥', 'A♥'])):
            # print("Hearts")
            rf_check_heart += 1
        elif((hand[i] in ['1♠', 'J♠', 'Q♠', 'K♠', 'A♠'])):
            # print("Spades")
            rf_check_spade += 1
        elif((hand[i] in ['1♣', 'J♣', 'Q♣', 'K♣', 'A♣'])):
            # print("Clubs")
            rf_check_club += 1
        
        i += 1

    if((rf_check_diamond == 5) or (rf_check_heart == 5) or (rf_check_spade == 5) or (rf_check_club == 5)):
        return True
    
    return False

def check_sflush(hand):
    tally_matches = {}
    i = 0
    flushed = False

    while(i < 7):
        if(hand[i][1] in tally_matches):
            tally_matches[hand[i][1]] += 1
        else:
            tally_matches[hand[i][1]] = 1

        i += 1

    max_key = max(tally_matches, key = lambda key: tally_matches[key])

    print(tally_matches)

    if(tally_matches[max_key] <= 5):
        flushed = True

    # if(flushed = True):
    #     ### Now solve how to look at a straight
    #     place = "holder"

    return

def check_four(hand):
    tally_matches = {}
    i = 0

    while(i < 7):
        if(hand[i][0] in tally_matches):
            tally_matches[hand[i][0]] += 1
        else:
            tally_matches[hand[i][0]] = 1

        i += 1

    max_key = max(tally_matches, key = lambda key: tally_matches[key])

    # print(tally_matches)

    if(tally_matches[max_key] == 4):
        print("Winner!")
        return True
    
    return False

def check_fhouse(hand):
    return False

def check_flush(hand):
    tally_matches = {}
    i = 0

    while(i < 7):
        if(hand[i][1] in tally_matches):
            tally_matches[hand[i][1]] += 1
        else:
            tally_matches[hand[i][1]] = 1

        i += 1

    max_key = max(tally_matches, key = lambda key: tally_matches[key])

    print(tally_matches)

    if(tally_matches[max_key] >= 5):
        print("Winner!")
        return True
    
    return False

def check_straight(hand):                           # Attention to this funciton really quick. I have the methods for sorting, however, I don't believe it's working
    parsed_hand = parse(hand)                       # Would you be able to help check what could be incorrect? - JS
    parsed_sort = sort(parsed_hand)
    sorted_hand = reparse(parsed_sort)
    return False


def check_win(hand):
    if(check_royal(hand)):
        return "Royal Flush"
    elif(check_sflush(hand)): # Not yet implemented
        return "Straight Flush"
    elif(check_four(hand)):
        return "Four of a Kind"
    elif(check_fhouse(hand)):
        return "Full House"
    elif(check_flush(hand)):
        return "Flush"
    elif(check_straight(hand)):
        return "Straight"

def main():

    if(intro() == False):
        return

    blank_screen()
    print("Dealing your cards...")
    
    deck.shuffle()
    hands = deck.deal(2) # Currently hardcoded number of players

    deck.burn()
    table_hand = []
    i = 0
    while(i < 5):
        cardDrawn = deck.draw()
        table_hand.append(cardDrawn)
        i += 1
    
    playerOneHand = hands[0]
    playerTwoHand = hands[1]

    # Pre Flop - Main Set up of hands and display
    blank_screen()
    pre_flop(playerOneHand)

    play_turn()
    turnPlayed = input("You Turn: ")
    if(turnPlayed.lower() == "raise"):
        print("raised")
    elif(turnPlayed.lower() == "call"):
        print("called")
    elif(turnPlayed.lower() == "fold"):
        print("I'm out")
    elif(turnPlayed.lower() == "all"):
        print("I'm in")
    else:
        print("HAHAHAHA")

    # The Flop - Displays three cards and P1 hand
    blank_screen()
    the_flop(playerOneHand, table_hand)
    
    if(turnPlayed.lower() != "fold" and turnPlayed.lower() != "all"):
        play_turn()
        turnPlayed = input("You Turn: ")
        if(turnPlayed.lower() == "raise"):
            print("raise")
        elif(turnPlayed.lower() == "call"):
            print("called")
        elif(turnPlayed.lower() == "fold"):
            print("I'm out")
        elif(turnPlayed.lower() == "all"):
            print("I'm in")
        else:
            print("HAHAHAHA")

    # The Turn - Displays four cards and P1 hand
    blank_screen()
    the_turn(playerOneHand, table_hand)

    if(turnPlayed.lower() != "fold" and turnPlayed.lower() != "all"):
        play_turn()
        turnPlayed = input("You Turn: ")
        if(turnPlayed.lower() == "raise"):
            print("raise")
        elif(turnPlayed.lower() == "call"):
            print("called")
        elif(turnPlayed.lower() == "fold"):
            print("I'm out")
        elif(turnPlayed.lower() == "all"):
            print("I'm in")
        else:
            print("HAHAHAHA")

    # The River - Display five cards and P1 hand
    blank_screen()
    the_river(playerOneHand, table_hand)

    if(turnPlayed.lower() != "fold" and turnPlayed.lower() != "all"):
        play_turn()
        turnPlayed = input("You Turn: ")
        if(turnPlayed.lower() == "raise"):
            print("raise")
        elif(turnPlayed.lower() == "call"):
            print("called")
        elif(turnPlayed.lower() == "fold"):
            print("I'm out")
        elif(turnPlayed.lower() == "all"):
            print("I'm in")
        else:
            print("HAHAHAHA")

    # The Showdown - Displays all cards
    players_hands = [playerOneHand, playerTwoHand]
    blank_screen()
    the_showdown(players_hands, table_hand)
    usable_hand = table_hand + playerOneHand

    win = check_win(usable_hand)

    print(f"You won through a {win}")

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



## Win conditions
    # You are the only one still in ( All folded )

    # Royal Flush
    # Straight Flush
    # Four of a Kind
    # Full House 
    # Flush
    # Straight
    # Three of a Kind
    # Two Pair
    # One Pair
    # High Card
