import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Dict

def create_heatmap_tricks(formatted_results: Dict[str, Dict[str, Dict[str, float]]], num_decks: int) -> None:
    """
    Creates a heatmap for win percentages based on trick-based scoring.
    
    Parameters:
    formatted_results (dict): The computed win/draw percentages.
    num_decks (int): The number of decks processed.
    """
    # Define the order of sequences and their corresponding labels
    sequences = ['000', '001', '010', '011', '100', '101', '110', '111']
    sequence_labels = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']  # Replacing 0 → B, 1 → R

    # Initialize matrices for win and draw percentages
    win_matrix = np.zeros((len(sequences), len(sequences)))
    draw_matrix = np.zeros((len(sequences), len(sequences)))

    # Populate the matrices with extracted win and draw percentages
    for i, seq1 in enumerate(sequences):
        for j, seq2 in enumerate(sequences):
            if seq1 != seq2:
                result = formatted_results.get(seq1, {}).get(seq2, {})

                # Extract win and draw percentages for tricks
                win_pct = result.get('tricks_win', 0.0)
                draw_pct = result.get('tricks_draw', 0.0)

                win_matrix[i, j] = win_pct
                draw_matrix[i, j] = draw_pct

    # Create labels for annotation (Win % with Draw % in parentheses)
    labels = np.array([[f"{round(win, 1)}%\n({round(draw, 1)}%)" 
                        for win, draw in zip(win_row, draw_row)] 
                        for win_row, draw_row in zip(win_matrix, draw_matrix)])

    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(win_matrix, annot=labels, fmt="", cmap="Blues", cbar=True, linewidths=0.5, 
                     linecolor="black", xticklabels=sequence_labels, yticklabels=sequence_labels)

    plt.xlabel("My Choice", fontsize=12)
    plt.ylabel("Opponent Choice", fontsize=12)
    plt.title(f"Heat Map of Win Percentage (Tricks)\nDecks Processed: {num_decks}", 
              fontsize=14, fontweight="bold")

    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.show()


def create_heatmap_cards(formatted_results: Dict[str, Dict[str, Dict[str, float]]], num_decks: int) -> None:
    """
    Creates a heatmap for win percentages based on cards collected.
    
    Parameters:
    formatted_results (dict): The computed win/draw percentages.
    num_decks (int): The number of decks processed.
    """
    # Define the order of sequences and their corresponding labels
    sequences = ['000', '001', '010', '011', '100', '101', '110', '111']
    sequence_labels = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']  # Replacing 0 → B, 1 → R

    # Initialize matrices for win and draw percentages
    win_matrix = np.zeros((len(sequences), len(sequences)))
    draw_matrix = np.zeros((len(sequences), len(sequences)))

    # Populate the matrices with extracted win and draw percentages (Cards Collected)
    for i, seq1 in enumerate(sequences):
        for j, seq2 in enumerate(sequences):
            if seq1 != seq2:
                result = formatted_results.get(seq1, {}).get(seq2, {})

                # Extract win and draw percentages for cards
                win_pct = result.get('cards_win', 0.0)
                draw_pct = result.get('cards_draw', 0.0)

                win_matrix[i, j] = win_pct
                draw_matrix[i, j] = draw_pct

    # Create labels for annotation (Win % with Draw % in parentheses)
    labels = np.array([[f"{round(win, 1)}%\n({round(draw, 1)}%)" 
                        for win, draw in zip(win_row, draw_row)] 
                        for win_row, draw_row in zip(win_matrix, draw_matrix)])

    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(win_matrix, annot=labels, fmt="", cmap="Greens", cbar=True, linewidths=0.5, 
                     linecolor="black", xticklabels=sequence_labels, yticklabels=sequence_labels)

    plt.xlabel("My Choice", fontsize=12)
    plt.ylabel("Opponent Choice", fontsize=12)
    plt.title(f"Heat Map of Win Percentage (Cards Collected)\nDecks Processed: {num_decks}", 
              fontsize=14, fontweight="bold")

    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.show()
