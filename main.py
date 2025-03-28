import os
import json
from src.processing import compute_win_draw_percentages
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
    n_decks: int = 1000000
    n_simulations: int = 1

    formatted_results: dict = compute_win_draw_percentages(n_decks, n_simulations)

    if not os.path.exists('data'):
        os.makedirs('data')

    results_file: str = os.path.join('data', "results.json")
    with open(results_file, 'w') as f:
        json.dump(formatted_results, f, default=convert)

    # Save heatmap for Tricks
    create_heatmap_tricks(formatted_results, n_decks)

    create_heatmap_cards(formatted_results, n_decks)
    print("Simulation complete, results saved, and heatmaps visualized successfully.")
    print("Heatmaps saved in the 'saved_heatmaps' folder.")

if __name__ == "__main__":
    main()
