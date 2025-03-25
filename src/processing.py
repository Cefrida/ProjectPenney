import random
from datagen import get_decks
from src.helpers import PATH_DATA, debugger_factory
from datagen import generate_sequences 

@debugger_factory
def simulate_game(deck, seq1, seq2):
    """
    Simulate a game where two players choose a sequence and the player who wins is the one with the most tricks.
    """
    p1_tricks, p2_tricks = 0, 0
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

    if p1_tricks > p2_tricks:
        return 'Player 1 wins'
    elif p2_tricks > p1_tricks:
        return 'Player 2 wins'
    else:
        return 'Draw'


@debugger_factory
def compute_win_draw_percentages(n_decks: int, n_simulations: int = 1000):
    """
    Compute the percentage of Player 2 wins and draws for all sequence matchups.
    """
    results = {}
    all_sequences = generate_sequences()
    
    for seq1 in all_sequences:
        results[seq1] = {'Player 2 Wins': {}, 'Draws': {}}
        
        for seq2 in all_sequences:
            p2_wins, draws = 0, 0
            
            for _ in range(n_simulations):
                seed = random.randint(0, 10000)
                deck = get_decks(n_decks, seed)
                outcome = simulate_game(deck, seq1, seq2)
                
                if outcome == 'Player 2 wins':
                    p2_wins += 1
                elif outcome == 'Draw':
                    draws += 1
            
            results[seq1]['Player 2 Wins'][seq2] = p2_wins / n_simulations * 100
            results[seq1]['Draws'][seq2] = draws / n_simulations * 100
    
    return results
