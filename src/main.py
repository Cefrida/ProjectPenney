import os
import json
from datagen import compute_win_draw_percentages
from visualization import create_heatmap

def main():
    # Set default values for number of decks and seed
    n_decks = 1000
    seed = 42

    # If arguments are passed via the command line, use them
    if len(sys.argv) > 1:
        try:
            n_decks = int(sys.argv[1])  # First argument for number of decks
            seed = int(sys.argv[2])     # Second argument for seed
        except ValueError:
            print("Invalid arguments. Using default values.")

    print(f"Generating {n_decks} decks with seed {seed}...")

    # Compute win and draw percentages for all sequence matchups
    win_draw_percentages = compute_win_draw_percentages(n_decks=n_decks, n_simulations=1000)

    # You might want to save the results as a file for future reference
    results_file = os.path.join('data', "results.json")
    with open(results_file, 'w') as f:
        json.dump(win_draw_percentages, f)
    
    # Visualize results (create heatmap)
    create_heatmap(win_draw_percentages)

    print("Simulation complete and visualized successfully.")

if __name__ == "__main__":
    main()
