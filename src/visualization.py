import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datagen import generate_sequences

@debugger_factory
def create_heatmap(win_draw_percentages):
    # Generate all possible sequences
    sequences = generate_sequences()  
    n_sequences = len(sequences)

    # Initialize the heatmap data
    heatmap_data = np.zeros((n_sequences, n_sequences))  # Dynamically adjust size

    # Populate the heatmap data with Player 2's win percentages
    for i, seq1 in enumerate(sequences):
        for j, seq2 in enumerate(sequences):
            if seq1 != seq2:  # Avoid self-matches
                # Assuming 'win_draw_percentages' is a DataFrame
                percentage = win_draw_percentages.loc[
                    (win_draw_percentages['Sequence 1'] == seq1) & 
                    (win_draw_percentages['Sequence 2'] == seq2), 'P2 Wins'].values[0]
                heatmap_data[i, j] = percentage

    # Plotting the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_data, annot=True, cmap='RdYlGn', xticklabels=sequences, yticklabels=sequences)
    plt.title('Player 2 Win Percentages')
    plt.xlabel('Opponent Sequence')
    plt.ylabel('Player Sequence')
    
    # Save the figure to the specified location
    plt.savefig('figures/heatmap.png')
    plt.close()
