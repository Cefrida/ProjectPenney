@debugger_factory
def create_heatmap(win_draw_percentages):
    """
    Creates a heatmap for Player 2 win percentages

    :param win_draw_percentages: Dictionary containing the win results for each sequence matchup.
    """
    sequences = generate_sequences()  # Gets the list of all sequences
    heatmap_data = np.zeros((8, 8))  # Creates an 8x8 grid for the heatmap

    # Fills heatmap with the win percentage data
    for i, seq1 in enumerate(sequences):
        for j, seq2 in enumerate(sequences):
            if seq1 != seq2:  # No self-matches
                percentage = win_draw_percentages[seq1]['Player 2 Wins'].get(seq2, 0)
                heatmap_data[i, j] = percentage  # Stores win percentage

    # Create the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        heatmap_data, 
        annot=True, 
        cmap='RdYlGn', 
        xticklabels=sequences, 
        yticklabels=sequences,
        cbar_kws={'label': 'Win Percentage'}, 
        linewidths=0.5
    )

    plt.title(f"My Chance of Winning by Sequence Pair (n=1000)")
    plt.xlabel("My Opponent's Sequence Choice")
    plt.ylabel("My Sequence Choice")
    
    # Save the heatmap image to the 'figures' folder
    if not os.path.exists('figures'):
        os.makedirs('figures')  # Create 'figures' folder if it doesn't exist
    
    heatmap_filename = os.path.join('figures', 'win_heatmap.png')
    plt.savefig(heatmap_filename)
    plt.close()  # Close the figure to avoid overlapping on multiple runs

    print(f"Heatmap saved to {heatmap_filename}")
