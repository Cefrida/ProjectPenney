import numpy as np
import os
from helpers import PATH_DATA, debugger_factory
import random

HALF_DECK_SIZE = 26

@debugger_factory
def get_decks(n_decks: int, seed: int, half_deck_size: int = HALF_DECK_SIZE) -> tuple[np.ndarray, np.ndarray]:
    # Generate shuffled decks
    init_deck = [0] * half_deck_size + [1] * half_deck_size
    decks = np.tile(init_deck, (n_decks, 1))  # Shape (n_decks, 52)
    rng = np.random.default_rng(seed)
    
    for deck in decks:
        rng.shuffle(deck)  # In-place shuffle
    
    return decks, np.random.get_state()  # Ensure the random state is returned for reproducibility



class DeckStorage:
    def __init__(self, storage_dir=PATH_DATA):
        self.decks = {}
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def add_decks(self, n_decks: int, seed: int):
        """
        Add new decks to the storage while keeping the old ones.
        Ensures reproducibility by storing decks with their corresponding seed.
        """
        # Generate new decks
        new_decks = get_decks(n_decks, seed)
        
        # Store the decks using the seed as the key
        self.decks[seed] = new_decks
        
        # Save to file
        self._save_decks(seed, new_decks)

    def get_decks(self, seed: int):
        """
        Get the decks associated with a specific seed from memory.
        """
        decks = self.decks.get(seed, None)
        if decks is None:
            print(f"No decks found for seed {seed}.")
        return decks

    def get_all_decks(self):
        """
        Retrieve all stored decks from memory.
        """
        return self.decks
    
    def _save_decks(self, seed: int, decks: np.ndarray):
        """
        Save the decks to a .npy file for persistence. This allows for reproducibility.
        """
        filename = os.path.join(self.storage_dir, f'decks_{seed}.npy')
        np.save(filename, decks)
        print(f"Decks saved with seed {seed} to {filename}")
    
    def load_decks(self, seed: int):
        """
        Load decks from a .npy file using the seed.
        """
        filename = os.path.join(self.storage_dir, f'decks_{seed}.npy')
        if os.path.exists(filename):
            return np.load(filename)
        else:
            print(f"Decks with seed {seed} not found.")
            return None

def generate_sequences():
    """
    Generate all possible sequences of 3 binary cards and convert them to 'R' and 'B' labels.
    """
    binary_sequences = ['{:03b}'.format(i) for i in range(8)]
    rb_sequences = [seq.replace('0', 'B').replace('1', 'R') for seq in binary_sequences]
    return rb_sequences
