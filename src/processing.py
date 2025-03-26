import random
from datagen import get_decks, generate_sequences
from src.helpers import PATH_DATA, debugger_factory

@debugger_factory
def simulate_game(deck, seq1, seq2):
    """
    Simulate a game where two players choose a sequence and the player who wins is the one with the most tricks.
    """
    p1_tricks, p2_tricks = 0, 0
    p1_cards, p2_cards = 0, 0
    current_sequence = []
    
    for card in deck:  # Loop through each card in the deck
        current_sequence.append(card)
        if len(current_sequence) > 3:
            current_sequence.pop(0)  # Remove the oldest card when there are more than 3 cards

        if ''.join(current_sequence) == seq1:
            p1_tricks += 1
            current_sequence = []  # Reset sequence
        elif ''.join(current_sequence) == seq2:
            p2_tricks += 1
            current_sequence = []  # Reset sequence

    # Count the number of cards for each player (half the deck)
    p1_cards = len([card for card in deck if card == 0])  # Cards assigned to Player 1 (B)
    p2_cards = len([card for card in deck if card == 1])  # Cards assigned to Player 2 (R)

    if p1_tricks > p2_tricks:
        return 'Player 1 wins', p1_tricks, p2_tricks, p1_cards, p2_cards
    elif p2_tricks > p1_tricks:
        return 'Player 2 wins', p1_tricks, p2_tricks, p1_cards, p2_cards
    else:
        return 'Draw', p1_tricks, p2_tricks, p1_cards, p2_cards


@debugger_factory
def compute_win_draw_percentages(n_decks: int, n_simulations: int = 1000):
    """
    Compute the percentage of Player 2 wins and draws for all sequence matchups.
    """
    results = {}
    all_sequences = generate_sequences()
    
    for seq1 in all_sequences:
        results[seq1] = {'Player 2 Wins': {}, 'Draws': {}, 'P1 Tricks': {}, 'P2 Tricks': {}, 'P1 Cards': {}, 'P2 Cards': {}}
        
        for seq2 in all_sequences:
            p2_wins, draws = 0, 0
            p1_tricks_total, p2_tricks_total = 0, 0
            p1_cards_total, p2_cards_total = 0, 0
            
            for _ in range(n_simulations):
                seed = random.randint(0, 10000)
                decks, _ = get_decks(n_decks, seed)  # Ensure unpacking the decks correctly
                outcome, p1_tricks, p2_tricks, p1_cards, p2_cards = simulate_game(decks, seq1, seq2)
                
                if outcome == 'Player 2 wins':
                    p2_wins += 1
                elif outcome == 'Draw':
                    draws += 1
                
                p1_tricks_total += p1_tricks
                p2_tricks_total += p2_tricks
                p1_cards_total += p1_cards
                p2_cards_total += p2_cards
            
            # Calculate percentages
            results[seq1]['Player 2 Wins'][seq2] = p2_wins / n_simulations * 100
            results[seq1]['Draws'][seq2] = draws / n_simulations * 100
            
            # Calculate average tricks and cards
            results[seq1]['P1 Tricks'][seq2] = p1_tricks_total / n_simulations
            results[seq1]['P2 Tricks'][seq2] = p2_tricks_total / n_simulations
            results[seq1]['P1 Cards'][seq2] = p1_cards_total / n_simulations
            results[seq1]['P2 Cards'][seq2] = p2_cards_total / n_simulations
    
    # Formatting results with win and draw percentages in the same box
    formatted_results = {}
    for seq1, seq_data in results.items():
        formatted_results[seq1] = {}
        for seq2 in all_sequences:
            win_percentage = results[seq1]['Player 2 Wins'][seq2]
            draw_percentage = results[seq1]['Draws'][seq2]
            formatted_results[seq1][seq2] = f"{win_percentage:.2f}% ({draw_percentage:.2f}%)"

    return formatted_results
