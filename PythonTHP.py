import pygame
import platform
from deck import Deck
from player import Player

# Initialize Pygame
pygame.init()

# Screen setup
SCR_WIDTH = 1280
SCR_HEIGHT = 720
scr = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption("TEXAS HOLD'EM")

# Colors
WHITE = (255, 255, 255)
GREEN_FELT = (0, 100, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Card dimensions
CARD_WIDTH = 80
CARD_HEIGHT = 120
CARD_SPACING = 10

# Chip dimensions
CHIP_SIZE = 40

# Button dimensions
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 30

# Layout
TABLE_CENTER = (SCR_WIDTH // 2.18, SCR_HEIGHT // 2)
COMMUNITY_CARD_POSITIONS = [
    (TABLE_CENTER[0] - 2 * (CARD_WIDTH + CARD_SPACING), TABLE_CENTER[1]),
    (TABLE_CENTER[0] - 1 * (CARD_WIDTH + CARD_SPACING), TABLE_CENTER[1]),
    (TABLE_CENTER[0], TABLE_CENTER[1]),
    (TABLE_CENTER[0] + 1 * (CARD_WIDTH + CARD_SPACING), TABLE_CENTER[1]),
    (TABLE_CENTER[0] + 2 * (CARD_WIDTH + CARD_SPACING), TABLE_CENTER[1])
]
PLAYER_POSITIONS = [
    (SCR_WIDTH // 2.35, SCR_HEIGHT - 150),  #Bottom (Player 1, human)
    (SCR_WIDTH//4 - 280, (SCR_HEIGHT // 2) - 100),     #Top Left (Player 2)
    (SCR_WIDTH // 2.35, 50),                #Top (Player 3)
    (SCR_WIDTH - 200, (SCR_HEIGHT // 2) - 100),       #Top Right (Player 4)
]
HOLE_CARD_POSITIONS = [
    [
        (pos[0] - CARD_SPACING // 2, pos[1] + 20),
        (pos[0] + CARD_WIDTH + CARD_SPACING // 2, pos[1] + 20)
    ]
    for pos in PLAYER_POSITIONS
]
BUTTON_POSITIONS = {
    "Fold": (SCR_WIDTH - 150, SCR_HEIGHT - 80),
    "Call": (SCR_WIDTH - 150, SCR_HEIGHT - 120),
    "Raise": (SCR_WIDTH - 150, SCR_HEIGHT - 160),
    "All-in": (SCR_WIDTH - 150, SCR_HEIGHT - 200)
}
POT_TEXT_POSITION = (TABLE_CENTER[0] - 20, TABLE_CENTER[1] - 50)
CHIP_SELECTION_AREA = (SCR_WIDTH - 250, SCR_HEIGHT - 200)

# Load assets
def load_assets():
    try:
        table_image = pygame.image.load("table.png").convert()
        table_image = pygame.transform.scale(table_image, (SCR_WIDTH, SCR_HEIGHT))
    except (pygame.error, FileNotFoundError) as e:
        print(f"Failed to load table.png: {e}")
        table_image = pygame.Surface((SCR_WIDTH, SCR_HEIGHT))
        table_image.fill(GREEN_FELT)

    card_images = {}
    deck_to_image = {
        '1♣': '10clubs', '1♠': '10spades', '1♥': '10hearts', '1♦': '10diamonds',
        '2♣': '2clubs', '3♣': '3clubs', '4♣': '4clubs', '5♣': '5clubs', '6♣': '6clubs',
        '7♣': '7clubs', '8♣': '8clubs', '9♣': '9clubs', 'J♣': 'Jclubs', 'Q♣': 'Qclubs',
        'K♣': 'Kclubs', 'A♣': 'Aclubs',
        '2♠': '2spades', '3♠': '3spades', '4♠': '4spades', '5♠': '5spades', '6♠': '6spades',
        '7♠': '7spades', '8♠': '8spades', '9♠': '9spades', 'J♠': 'Jspades', 'Q♠': 'Qspades',
        'K♠': 'Kspades', 'A♠': 'Aspades',
        '2♥': '2hearts', '3♥': '3hearts', '4♥': '4hearts', '5♥': '5hearts', '6♥': '6hearts',
        '7♥': '7hearts', '8♥': '8hearts', '9♥': '9hearts', 'J♥': 'Jhearts', 'Q♥': 'Qhearts',
        'K♥': 'Khearts', 'A♥': 'Ahearts',
        '2♦': '2diamonds', '3♦': '3diamonds', '4♦': '4diamonds', '5♦': '5diamonds', '6♦': '6diamonds',
        '7♦': '7diamonds', '8♦': '8diamonds', '9♦': '9diamonds', 'J♦': 'Jdiamonds', 'Q♦': 'Qdiamonds',
        'K♦': 'Kdiamonds', 'A♦': 'Adiamonds'
    }
    for card, key in deck_to_image.items():
        filename = f"{key}.png"
        try:
            card_image = pygame.image.load(filename).convert_alpha()
            card_images[card] = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))
        except (pygame.error, FileNotFoundError) as e:
            print(f"Failed to load {filename}: {e}")
            card_images[card] = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
            card_images[card].fill(WHITE)
    try:
        back_image = pygame.image.load("back.png").convert_alpha()
        card_images["back"] = pygame.transform.scale(back_image, (CARD_WIDTH, CARD_HEIGHT))
    except (pygame.error, FileNotFoundError) as e:
        print(f"Failed to load back.png: {e}")
        card_images["back"] = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        card_images["back"].fill(BLUE)

    chip_images = {}
    chip_values = [5, 10, 25, 100]
    chip_colors = {5: RED, 10: BLUE, 25: GREEN, 100: BLACK}
    for value in chip_values:
        filename = f"chip_{value}.png"
        try:
            chip_image = pygame.image.load(filename).convert_alpha()
            chip_images[value] = pygame.transform.scale(chip_image, (CHIP_SIZE, CHIP_SIZE))
        except (pygame.error, FileNotFoundError) as e:
            print(f"Failed to load {filename}: {e}")
            chip_images[value] = pygame.Surface((CHIP_SIZE, CHIP_SIZE))
            chip_images[value].fill(chip_colors.get(value, BLACK))

    button_images = {}
    button_types = ["Fold", "Call", "Raise", "All-in"]
    button_colors = {"Fold": RED, "Call": GREEN, "Raise": BLUE, "All-in": BLACK}
    for button in button_types:
        filename = f"{button}.png"
        try:
            button_image = pygame.image.load(filename).convert_alpha()
            button_images[button] = pygame.transform.scale(button_image, (BUTTON_WIDTH, BUTTON_HEIGHT))
        except (pygame.error, FileNotFoundError) as e:
            print(f"Failed to load {filename}: {e}")
            button_images[button] = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
            button_images[button].fill(button_colors[button])

    return table_image, card_images, chip_images, button_images

# Hand evaluation functions
def parse(hand):
    RANK_ORDER = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        '1': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }
    SUIT_ORDER = {'♣': 0, '♦': 1, '♥': 2, '♠': 3}
    return [(RANK_ORDER[card[0]], SUIT_ORDER[card[1]]) for card in hand]

def reparse(parsed_hand):
    RANK_LOOKUP = {
        2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: '1', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'
    }
    SUIT_LOOKUP = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}
    return [f"{RANK_LOOKUP[rank]}{SUIT_LOOKUP[suit]}" for rank, suit in parsed_hand]

def sort(parsed_hand):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    return merge_sort(parsed_hand)

def check_royal(hand):
    parsed = parse(hand)
    suits = {}
    for rank, suit in parsed:
        if rank >= 10:
            suits.setdefault(suit, []).append(rank)
    for ranks in suits.values():
        if sorted(ranks) == [10, 11, 12, 13, 14]:
            return True
    return False

def check_sflush(hand):
    parsed = parse(hand)
    suits = {}
    for rank, suit in parsed:
        suits.setdefault(suit, []).append(rank)
    for ranks in suits.values():
        if len(ranks) >= 5:
            sorted_ranks = sorted(ranks)
            for i in range(len(sorted_ranks) - 4):
                if sorted_ranks[i+4] - sorted_ranks[i] == 4 and len(set(sorted_ranks[i:i+5])) == 5:
                    return sorted_ranks[i+4]
                if sorted_ranks[:5] == [2, 3, 4, 5, 14]:
                    return 5
    return False

def check_four(hand):
    parsed = parse(hand)
    ranks = [rank for rank, _ in parsed]
    for rank in set(ranks):
        if ranks.count(rank) == 4:
            return rank
    return False

def check_fhouse(hand):
    parsed = parse(hand)
    ranks = [rank for rank, _ in parsed]
    three = two = 0
    three_rank = two_rank = 0
    for rank in set(ranks):
        count = ranks.count(rank)
        if count >= 3 and rank > three_rank:
            three, three_rank = count, rank
        elif count >= 2 and rank > two_rank:
            two, two_rank = count, rank
    if three >= 3 and two >= 2:
        return (three_rank, two_rank)
    return False

def check_flush(hand):
    parsed = parse(hand)
    suits = {}
    for rank, suit in parsed:
        suits.setdefault(suit, []).append(rank)
    for ranks in suits.values():
        if len(ranks) >= 5:
            return max(ranks)
    return False

def check_straight(hand):
    parsed = parse(hand)
    ranks = sorted(set(rank for rank, _ in parsed))
    if len(ranks) < 5:
        return False
    for i in range(len(ranks) - 4):
        if ranks[i+4] - ranks[i] == 4:
            return ranks[i+4]
    if ranks[-1] == 14 and ranks[:4] == [2, 3, 4, 5]:
        return 5
    return False

def check_three(hand):
    parsed = parse(hand)
    ranks = [rank for rank, _ in parsed]
    for rank in set(ranks):
        if ranks.count(rank) == 3:
            return rank
    return False

def check_two_pair(hand):
    parsed = parse(hand)
    ranks = [rank for rank, _ in parsed]
    pairs = []
    for rank in set(ranks):
        if ranks.count(rank) >= 2:
            pairs.append(rank)
    if len(pairs) >= 2:
        return sorted(pairs, reverse=True)[:2]
    return False

def check_pair(hand):
    parsed = parse(hand)
    ranks = [rank for rank, _ in parsed]
    for rank in set(ranks):
        if ranks.count(rank) == 2:
            return rank
    return False

def check_high_card(hand):
    parsed = parse(hand)
    return max(rank for rank, _ in parsed)

def check_win(hand):
    if check_royal(hand):
        return (10, "Royal Flush", 0)
    sflush = check_sflush(hand)
    if sflush:
        return (9, "Straight Flush", sflush)
    four = check_four(hand)
    if four:
        return (8, "Four of a Kind", four)
    fhouse = check_fhouse(hand)
    if fhouse:
        return (7, "Full House", fhouse[0])
    flush = check_flush(hand)
    if flush:
        return (6, "Flush", flush)
    straight = check_straight(hand)
    if straight:
        return (5, "Straight", straight)
    three = check_three(hand)
    if three:
        return (4, "Three of a Kind", three)
    two_pair = check_two_pair(hand)
    if two_pair:
        return (3, "Two Pair", two_pair[0])
    pair = check_pair(hand)
    if pair:
        return (2, "One Pair", pair)
    high = check_high_card(hand)
    return (1, "High Card", high)

# Render game state
def render_game(scr, table_image, card_images, button_images, player_hands, community_cards, pot, phase, players, current_bet, current_player, winner=None):
    scr.blit(table_image, (0, 0))
    
    # Draw community cards
    for i, pos in enumerate(COMMUNITY_CARD_POSITIONS):
        if i < len(community_cards):
            scr.blit(card_images[community_cards[i]], pos)
        else:
            scr.blit(card_images["back"], pos)
    
    # Draw hole cards
    for i, player_hole_positions in enumerate(HOLE_CARD_POSITIONS):
        if i < len(player_hands):
            if players[i]["folded"]:
                continue
            if i == 0 and player_hands[i]:
                scr.blit(card_images[player_hands[i][0]], player_hole_positions[0])
                scr.blit(card_images[player_hands[i][1]], player_hole_positions[1])
            else:
                if phase == "showdown" and player_hands[i]:
                    scr.blit(card_images[player_hands[i][0]], player_hole_positions[0])
                    scr.blit(card_images[player_hands[i][1]], player_hole_positions[1])
                elif player_hands[i]:
                    scr.blit(card_images["back"], player_hole_positions[0])
                    scr.blit(card_images["back"], player_hole_positions[1])

    # Draw buttons for Player 1
    if current_player == 0 and not players[0]["folded"]:
        for button, pos in BUTTON_POSITIONS.items():
            scr.blit(button_images[button], pos)

    # Draw pot, bet, phase, and turn text
    font = pygame.font.SysFont("impact", 24)
    pot_text = font.render(f"POT: {pot}", True, WHITE)
    scr.blit(pot_text, POT_TEXT_POSITION)
    bet_text = font.render(f"Current Bet: {current_bet}", True, WHITE)
    scr.blit(bet_text, (TABLE_CENTER[0] - 20, TABLE_CENTER[1] - 110))
    phase_text = font.render(f"Phase: {phase}", True, WHITE)
    scr.blit(phase_text, (TABLE_CENTER[0] - 20, TABLE_CENTER[1] - 80))
    turn_text = font.render(f"Player {current_player + 1}'s Turn", True, WHITE)
    scr.blit(turn_text, (TABLE_CENTER[0] - 20, TABLE_CENTER[1] - 140))

    # Draw player chips
    for i, player in enumerate(players):
        chip_text = font.render(f"P{i+1} Chips: {player['chips']}", True, WHITE)
        scr.blit(chip_text, (PLAYER_POSITIONS[i][0], PLAYER_POSITIONS[i][1] - 20))

    # Draw winner if applicable
    if winner:
        winner_text = font.render(winner, True, YELLOW)
        scr.blit(winner_text, (TABLE_CENTER[0] - 95, TABLE_CENTER[1] + 125))

    pygame.display.flip()

# Main game logic
def main():
    table_image, card_images, chip_images, button_images = load_assets()
    deck = Deck()
    num_players = 4
    players = [{"chips": 1000, "folded": False, "bet": 0, "has_acted": False} for _ in range(num_players)]
    pot = 0
    current_bet = 0
    phase = "pre-flop"
    player_hands = [[] for _ in range(num_players)]
    community_cards = []
    running = True
    current_player = 0
    last_raiser = None
    winner = None

    while running:
        if phase == "pre-flop" and not player_hands[0]:
            deck.shuffle()
            # Deal two cards to each player
            player_hands = deck.deal(num_players)
            # Blinds
            players[1]["bet"] = 10  # Small blind
            players[1]["chips"] -= 10
            players[1]["has_acted"] = True
            players[2]["bet"] = 20  # Big blind
            players[2]["chips"] -= 20
            players[2]["has_acted"] = True
            current_bet = 20
            pot += 30
            current_player = 3  # Start with Player 4 (after big blind)
            last_raiser = 2  # Big blind is the initial "raise"
            render_game(scr, table_image, card_images, button_images, player_hands, community_cards, pot, phase, players, current_bet, current_player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and current_player == 0 and not players[0]["folded"]:
                mouse_pos = event.pos
                for button, pos in BUTTON_POSITIONS.items():
                    button_rect = pygame.Rect(pos[0], pos[1], BUTTON_WIDTH, BUTTON_HEIGHT)
                    if button_rect.collidepoint(mouse_pos):
                        players[0]["has_acted"] = True
                        if button == "Fold":
                            players[0]["folded"] = True
                        elif button == "Call":
                            bet_to_match = current_bet - players[0]["bet"]
                            if bet_to_match > players[0]["chips"]:
                                bet_to_match = players[0]["chips"]
                            players[0]["chips"] -= bet_to_match
                            players[0]["bet"] += bet_to_match
                            pot += bet_to_match
                        elif button == "Raise":
                            bet_to_match = current_bet - players[0]["bet"] + 10
                            if bet_to_match > players[0]["chips"]:
                                bet_to_match = players[0]["chips"]
                            players[0]["chips"] -= bet_to_match
                            players[0]["bet"] += bet_to_match
                            pot += bet_to_match
                            current_bet = players[0]["bet"]
                            last_raiser = 0
                            # Reset has_acted for others
                            for i in range(1, num_players):
                                if not players[i]["folded"]:
                                    players[i]["has_acted"] = False
                        elif button == "All-in":
                            bet_to_match = players[0]["chips"]
                            players[0]["chips"] = 0
                            players[0]["bet"] += bet_to_match
                            pot += bet_to_match
                            current_bet = max(current_bet, players[0]["bet"])
                            last_raiser = 0
                            for i in range(1, num_players):
                                if not players[i]["folded"]:
                                    players[i]["has_acted"] = False
                        # Advance to next player
                        current_player = (current_player + 1) % num_players
                        while players[current_player]["folded"]:
                            current_player = (current_player + 1) % num_players
                        render_game(scr, table_image, card_images, button_images, player_hands, community_cards, pot, phase, players, current_bet, current_player)

        # AI for Players 2, 3, 4
        if current_player in [1, 2, 3] and not players[current_player]["folded"]:
            bet_to_match = current_bet - players[current_player]["bet"]
            players[current_player]["has_acted"] = True
            if bet_to_match > 0:
                if bet_to_match > players[current_player]["chips"]:
                    bet_to_match = players[current_player]["chips"]
                players[current_player]["chips"] -= bet_to_match
                players[current_player]["bet"] += bet_to_match
                pot += bet_to_match
            next_player = (current_player + 1) % num_players
            while players[next_player]["folded"]:
                next_player = (next_player + 1) % num_players
            current_player = next_player
            render_game(scr, table_image, card_images, button_images, player_hands, community_cards, pot, phase, players, current_bet, current_player)

        # Check if betting round is complete
        active_players = [p for p in players if not p["folded"]]
        if len(active_players) > 1:
            all_acted = all(p["has_acted"] or p["folded"] for p in players)
            bets_matched = all(p["bet"] == current_bet or p["folded"] for p in players)
            if all_acted and bets_matched and current_player == (last_raiser or 0):
                if phase == "pre-flop":
                    deck.burn()
                    community_cards = [deck.draw() for _ in range(3)]
                    phase = "flop"
                elif phase == "flop":
                    deck.burn()
                    community_cards.append(deck.draw())
                    phase = "turn"
                elif phase == "turn":
                    deck.burn()
                    community_cards.append(deck.draw())
                    phase = "river"
                elif phase == "river":
                    phase = "showdown"
                # Reset betting state
                current_bet = 0
                last_raiser = None
                for p in players:
                    p["bet"] = 0
                    p["has_acted"] = False
                current_player = 0
                render_game(scr, table_image, card_images, button_images, player_hands, community_cards, pot, phase, players, current_bet, current_player)

        # Handle single remaining player
        if len(active_players) == 1 and not winner:
            winner = f"Player {next(i for i, p in enumerate(players) if not p['folded']) + 1} wins (others folded)"
            phase = "showdown"
            render_game(scr, table_image, card_images, button_images, player_hands, community_cards, pot, phase, players, current_bet, current_player, winner)

        # Showdown
        if phase == "showdown" and not winner:
            active_players = [i for i, p in enumerate(players) if not p["folded"]]
            if len(active_players) == 1:
                winner = f"Player {active_players[0] + 1} wins (others folded)"
            else:
                best_score = (-1, "", 0)
                best_player = 0
                for i in active_players:
                    hand = player_hands[i] + community_cards
                    score = check_win(hand)
                    if score[0] > best_score[0] or (score[0] == best_score[0] and score[2] > best_score[2]):
                        best_score = score
                        best_player = i
                winner = f"Player {best_player + 1} wins with {best_score[1]}"
            render_game(scr, table_image, card_images, button_images, player_hands, community_cards, pot, phase, players, current_bet, current_player, winner)
            pygame.time.wait(3000)
            running = False

    pygame.quit()

# Initialize game display
def initialize_game_display():
    table_image, card_images, chip_images, button_images = load_assets()
    initial_render(scr, table_image, card_images, button_images)
    return scr, COMMUNITY_CARD_POSITIONS, HOLE_CARD_POSITIONS, BUTTON_POSITIONS

# Initial rendering
def initial_render(scr, table_image, card_images, button_images):
    scr.blit(table_image, (0, 0))
    for pos in COMMUNITY_CARD_POSITIONS:
        scr.blit(card_images["back"], pos)
    for player_hole_positions in HOLE_CARD_POSITIONS:
        scr.blit(card_images["back"], player_hole_positions[0])
        scr.blit(card_images["back"], player_hole_positions[1])
    for button, pos in BUTTON_POSITIONS.items():
        scr.blit(button_images[button], pos)
    font = pygame.font.SysFont("impact", 24)
    pot_text = font.render("POT: 0", True, WHITE)
    scr.blit(pot_text, POT_TEXT_POSITION)
    pygame.display.flip()

if platform.system() == "Emscripten":
    import asyncio
    async def main():
        main()
        await asyncio.sleep(1.0 / 60)
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        main()