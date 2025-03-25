

import numpy as np
import os
import json

HALF_DECK_SIZE = 26
DECK_SIZE = HALF_DECK_SIZE * 2
N_DECKS = 250000

class Decking:
    def __init__(self, seed: int = 9903):
        self.seed = seed
        self.rng = np.random.default_rng(self.seed)
        self.rounds = 0
        self.storage_dir = os.path.join(os.getcwd(), "files")  # Store files in "files/"
        os.makedirs(self.storage_dir, exist_ok=True)  # Ensure "files" folder exists

    def gen_decks(self, n_decks: int, half_deck_size: int = HALF_DECK_SIZE):
        """
        Generates and stores decks of cards along with their seeds.

        Args:
            n_decks (int): Number of decks to generate.
            half_deck_size (int): Number of cards in each half-deck.

        Returns:
            np.ndarray: Array of shuffled decks.
        """
        init_deck = [0] * half_deck_size + [1] * half_deck_size  # Two halves: 0 and 1
        decks = np.tile(init_deck, (n_decks, 1))  # Create n_decks of identical size
        self.rng.permuted(decks, axis=1, out=decks)  # Shuffle each deck

        # Paths to store deck data and state
        deck_storage_path = os.path.join(self.storage_dir, "deck_storage.npy")
        state_file_path = os.path.join(self.storage_dir, "state.json")

        # Start fresh if it's the first round or a fresh deck generation
        if self.rounds == 0 and os.path.exists(deck_storage_path):
            os.remove(deck_storage_path)

        if os.path.exists(deck_storage_path):
            existing_decks = np.load(deck_storage_path)
            decks = np.vstack((existing_decks, decks))  # Append new decks to existing

        np.save(deck_storage_path, decks)  # Save updated decks

        # Save the current state of the RNG for reproducibility
        state = self.rng.bit_generator.state
        with open(state_file_path, 'w') as f:
            json.dump(state, f)

        self.rounds += 1
        return decks

