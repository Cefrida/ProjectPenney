@debugger_factory
def create_heatmap(win_draw_percentages):
    sequences = generate_sequences()  # Get the list of all sequences
    n_sequences = len(sequences)
    heatmap_data = np.zeros((n_sequences, n_sequences))  # Dynamically adjust size

    for i, seq1 in enumerate(sequences):
        for j, seq2 in enumerate(sequences):
            if seq1 != seq2:  # No self-matches
                percentage = win_draw_percentages.loc[
                    (win_draw_percentages['Sequence 1'] == seq1) & 
                    (win_draw_percentages['Sequence 2'] == seq2), 'P2 Wins'].values[0]
                heatmap_data[i, j] = percentage

    # Plotting and saving heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_data, annot=True, cmap='RdYlGn', xticklabels=sequences, yticklabels=sequences)
    plt.title('Player 2 Win Percentages')
    plt.xlabel('Opponent Sequence')
    plt.ylabel('Player Sequence')
    plt.savefig('figures/heatmap.png')
    plt.close()
