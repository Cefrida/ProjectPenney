import os
import json
from src.datagen import compute_win_draw_percentages
from src.visualization import create_heatmap
import numpy as np

def convert_to_serializable(obj):
    """
    Convert non-serializable objects (like numpy arrays) into a serializable format.
    """
    if isinstance(obj, np.ndarray):
        return obj.tolist()  # Convert numpy arrays to lists
    return obj

def main():
    # Ask the user for the number of decks and seed
    try:
        n_decks = int(input("Enter the number of decks: "))  # Get user input for number of decks
        seed = int(input("Enter the seed value: "))  # Get user input for seed
    except ValueError:
        print("Invalid input. Using default values.")
        n_decks = 1000  # Default value for number of decks
        seed = 42  # Default value for seed

    print(f"Generating {n_decks} decks with seed {seed}...")

    # Compute win and draw percentages for all sequence matchups
    win_draw_percentages = compute_win_draw_percentages(n_decks=n_decks, n_simulations=1000)

    # Ensure 'data' directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    # Save results to JSON file
    results_file = os.path.join('data', "results.json")
    with open(results_file, 'w') as f:
        json.dump(win_draw_percentages, f, default=convert_to_serializable)
    
    # Visualize results (create heatmap)
    create_heatmap(win_draw_percentages)

    print("Simulation complete and visualized successfully.")

if __name__ == "__main__":
    main()
