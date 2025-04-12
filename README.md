# Free-Code-Project
A repo to hold a group coding project for 235!

# Brainstorming Session  
- Game
  - Snake?
  - Minesweeper?
  - Other Thoughts
- Website
  - Host Game on here?
  - 

**3d Tic-Tac-Toe**  
TTT is on anothet level. The goal of the game is to get three in a row. you can match the usual TTT wins, but you can also win through layers.  

Needs:  
- Website / GUI
- Game logistics
  - Checking win Conditions
  - Organizatuinal logistics
- Other Players // AI



Hours Tracker:  
J - [x][x][x][x][x][x][x][x]  
L - [x][x][x][ ][ ][ ][ ][ ]  

# Project Idea Going Forward - Poker    
Needs:   
- [ ] Deck object  
  - [ ] Shuffle  
  - [ ] Deal  
  - [ ] Draw  
  - [ ] Advance Table's Hand  
  - [ ] Reset?  
- [ ] Play  
  - [ ] Pass / Call  
  - [ ] Check Hand?  
  - [ ] Raise
  - [ ] All in
  - [ ] Fold
- [ ] Score
  - [ ] Compare with Table
  - [ ] Determine if player is only left
  - [ ] Compare highest hands
  - [ ] Collect // Apply winnings
     
Deck Object/Class?
Clubs    | 2 3 4 5 6 7 8 9 10 J Q K A  
C2 C3 C4 ... CJ CQ CK CA  
Spades   | 2 3 4 5 6 7 8 9 10 J Q K A  
S2 S3 S4 ... SJ SQ SK SA  
Diamonds | 2 3 4 5 6 7 8 9 10 J Q K A  
D2 D3 D4 ... DJ DQ DK DA  
Hearts   | 2 3 4 5 6 7 8 9 10 J Q K A  
H2 H3 H4 ... HJ HQ HK HA  

Foundation Logic
  - Deck object
  - Shuffle Functionality
  - Rank Hands Function
  - Showdown Function
  - Game State:
      - Community cards
      - Pot (Chip and Bet functionality required)
      - Current Bet tracker
      - Dealer position
  -AI Players/Multiplayer?

Player Structure
  - Personal Chips
  - Hole Cards
  - Active/Fold/All-in Status

Graphics
  - Game Window
  - Card Images
  - Image Placeholders:
      - Community Cards
      - Hold Cards
      - Poker Chips
      - UI Elements:
          - Buttons (Fold, Call, Raise, All In)
          - Display Current Bet
          - Chip Selection
          - Face down/Face up Cards

Main Game Loop
  - Events (Game Phases, Player Wins, etc.)
      - Phases:
          - Pre-Flop
          - Flop
          - Turn
          - River
          - Showdown
  - Game State
  - Render Graphics
