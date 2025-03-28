import os
import json
from src.processing import compute_win_draw_percentages, generate_and_save_decks
from src.visualization import create_heatmap_tricks, create_heatmap_cards
import numpy as np
from src.datagen import DeckStorage

def convert(obj: np.ndarray) -> list:
    """
    Convert numpy arrays to lists.
    """
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj

def main() -> None:
    # Initial number of decks
    n_decks: int = 1000000
    n_simulations: int = 1


    while True:
        try:
            seed = int(input("Please enter a seed value for deck generation: "))
            break
        except ValueError:
            print("Please enter a valid integer for the seed.")


    add_decks = input("Would you like to add more decks to the simulation? (yes/no): ").strip().lower()

    while add_decks == 'yes':
        try:
            additional_decks = int(input("How many decks would you like to add? "))
            n_decks += additional_decks
            print(f"Added {additional_decks} decks. Total decks now: {n_decks}")
        except ValueError:
            print("Please enter a valid number of decks.")
        
        add_decks = input("Would you like to add more decks? (yes/no): ").strip().lower()

    
    print(f"Generating and saving {n_decks} decks with seed {seed}...")
    generate_and_save_decks(seed, n_decks) 


    formatted_results: dict = compute_win_draw_percentages(n_decks, n_simulations)


    if not os.path.exists('data'):
        os.makedirs('data')


    results_file: str = os.path.join('data', "results.json")
    with open(results_file, 'w') as f:
        json.dump(formatted_results, f, default=convert)


    create_heatmap_tricks(formatted_results, n_decks, save_path='saved_heatmaps')
    create_heatmap_cards(formatted_results, n_decks, save_path='saved_heatmaps')


    print("Simulation complete, results saved, and heatmaps visualized successfully.")
    print("Heatmaps saved in the 'saved_heatmaps' folder.")

if __name__ == "__main__":
    main()
