from datagen import compute_win_draw_percentages, generate_sequences
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from helpers import debugger_factory

@debugger_factory
def create_heatmap(win_draw_percentages):
    """
    Creates a heatmap for Player 2 win percentages

    :param win_draw_percentages: Dictionary containing the win results for each sequence matchup.
    """
    sequences = generate_sequences()  # Get the list of all sequences
    heatmap_data = np.zeros((8, 8))  # Create an 8x8 grid for the heatmap

    # Fill the heatmap with the win percentage data
    for i, seq1 in enumerate(sequences):
        for j, seq2 in enumerate(sequences):
            if seq1 != seq2:  # Avoid self-matches
                percentage = win_draw_percentages[seq1]['Player 2 Wins'].get(seq2, 0)
                heatmap_data[i, j] = percentage  # Store win percentage

    # Create the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        heatmap_data, 
        annot=True, 
        cmap='RdYlGn',  # Red to Green for better visualization of win percentages
        xticklabels=sequences, 
        yticklabels=sequences,
        cbar_kws={'label': 'Win Percentage'}, 
        linewidths=0.5
    )

    plt.title(f"My Chance of Winning by Sequence Pair (n=1000)")
    plt.xlabel("My Opponent's Sequence Choice")
    plt.ylabel("My Sequence Choice")
    plt.show()

# Run the analysis
win_draw_percentages = compute_win_draw_percentages(n_decks=100, n_simulations=1000)
#win_draw_percentages

# Create and display the heatmap for win percentages
create_heatmap(win_draw_percentages)
