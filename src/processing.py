import random
from src.helpers import PATH_DATA
from src.datagen import generate_sequences, DeckStorage
import numpy as np
from collections import defaultdict
from tqdm import tqdm
from typing import List, Dict, Tuple

def load_decks_in_batches(n_decks: int, seed: int, batch_size: int = 10000) -> List[List[List[int]]]:
    """
    Load decks in batches of the given size.
    
    Args:
        n_decks (int): The number of decks to load.
        seed (int): The seed for randomization.
        batch_size (int): The size of each batch to load.
        
    Returns:
        List[List[List[int]]]: List of decks, chunked by batch size.
    """
    deck_storage = DeckStorage(storage_dir="data")
    all_decks = deck_storage.get_decks(seed)

    all_decks = all_decks[:n_decks]

    batches = [all_decks[i:i + batch_size] for i in range(0, len(all_decks), batch_size)]
    
    return batches


def simulate_game(deck: List[int], seq1: str, seq2: str) -> Tuple[int, int, int, int]:
    """
    Simulate a single game with the given deck and sequences.
    
    Args:
        deck (List[int]): The deck of cards to simulate.
        seq1 (str): The sequence for player 1.
        seq2 (str): The sequence for player 2.
        
    Returns:
        Tuple[int, int, int, int]: Player 1 tricks, Player 2 tricks, total cards collected by Player 1, total
        cards collected by Player 2
    """
    p1_tricks = 0
    p2_tricks = 0
    p1_collected_cards = []
    p2_collected_cards = []
    table = [] 

    for card in deck:
        table.append(card)

        if len(table) >= 3 and table[-3:] == list(map(int, seq1[:3])): 
            p1_tricks += 1
            p1_collected_cards.extend(table)
            table = [] 
            continue
        
        if len(table) >= 3 and table[-3:] == list(map(int, seq2[:3])): 
            p2_tricks += 1
            p2_collected_cards.extend(table)
            table = [] 
            continue  

    return p1_tricks, p2_tricks, len(p1_collected_cards), len(p2_collected_cards)


def run_simulation_for_deck(decks: List[List[int]], seq1: str, seq2: str, n_simulations: int) -> Dict[str, float]:
    total_p2_wins_tricks = 0  
    total_p2_wins_cards = 0 
    total_draws_tricks = 0
    total_draws_cards = 0 
    total_games = n_simulations * len(decks)

    for deck in decks:
        for i in range(n_simulations):
            p1_tricks, p2_tricks, p1_cards, p2_cards = simulate_game(deck, seq1, seq2)
            
            if p2_tricks > p1_tricks:
                total_p2_wins_tricks += 1
            elif p2_tricks == p1_tricks:
                total_draws_tricks += 1 
            
            if p2_cards > p1_cards:
                total_p2_wins_cards += 1
            elif p2_cards == p1_cards:
                total_draws_cards += 1  

    p2_win_percentage_tricks = (total_p2_wins_tricks / total_games) * 100
    p2_win_percentage_cards = (total_p2_wins_cards / total_games) * 100
    draw_percentage_tricks = (total_draws_tricks / total_games) * 100
    draw_percentage_cards = (total_draws_cards / total_games) * 100

    return {
        'Player 2 Win % (Tricks)': round(p2_win_percentage_tricks, 2),
        'Player 2 Win % (Cards)': round(p2_win_percentage_cards, 2),
        'Draw % (Tricks)': round(draw_percentage_tricks, 2),
        'Draw % (Cards)': round(draw_percentage_cards, 2)
    }


def compute_win_draw_percentages(n_decks: int, n_simulations: int = 1000) -> Dict[str, Dict[str, Dict[str, Dict[str, float]]]]:
    all_sequences = [
        '000', '001', '010', '011', '100', '101', '110', '111'
    ]

    batches = load_decks_in_batches(n_decks, seed=42)

    all_results = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))

    for batch_index, batch in enumerate(tqdm(batches, desc="Processing Batches", unit="batch")):
        for seq1 in all_sequences:
            for seq2 in all_sequences:
                if seq1 == seq2: 
                    continue

                simulation_result = run_simulation_for_deck(batch, seq1, seq2, n_simulations)

                all_results[batch_index][seq1][seq2] = simulation_result

    # Format the final results
    formatted_results: Dict[str, Dict[str, Dict[str, Dict[str, float]]]] = {}
    for batch_idx, batch_result in all_results.items():
        for seq1 in batch_result:
            if seq1 not in formatted_results:
                formatted_results[seq1] = {}
            for seq2 in batch_result[seq1]:
                result = all_results[batch_idx][seq1][seq2]

                p2_win_tricks = result.get('Player 2 Win % (Tricks)', 0.0)
                p2_win_cards = result.get('Player 2 Win % (Cards)', 0.0)
                p2_draw_tricks = result.get('Draw % (Tricks)', 0.0)
                p2_draw_cards = result.get('Draw % (Cards)', 0.0)

                formatted_results[seq1][seq2] = {
                    'tricks_win': p2_win_tricks,
                    'tricks_draw': p2_draw_tricks,
                    'cards_win': p2_win_cards,
                    'cards_draw': p2_draw_cards
                }

    return formatted_results
