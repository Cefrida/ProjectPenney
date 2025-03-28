import numpy as np
import os
import json
from datetime import datetime

HALF_DECK_SIZE = 26  
MAX_DECKS_PER_FILE = 10000 
STORAGE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

class DeckStorage:
    """
    Handles generating, storing, and retrieving shuffled decks while maintaining reproducibility.
    """

    def __init__(self, storage_dir=STORAGE_DIR):
        self.storage_dir = storage_dir
        self.decks = {} 

        os.makedirs(self.storage_dir, exist_ok=True)

        self.seeds_file = os.path.join(self.storage_dir, "seeds.json")
        if not os.path.exists(self.seeds_file):
            with open(self.seeds_file, "w") as f:
                json.dump([], f)  

    def add_decks(self, n_decks: int, seed: int):
        """Generates and stores new decks while keeping existing ones."""
        new_decks = generate_decks(n_decks, seed)
        self._save_seeds(seed)
        self.decks[seed] = new_decks
        self._save_decks(seed, new_decks)

    def get_decks(self, seed: int):
        """Retrieves decks for a specific seed."""
        if seed in self.decks:
            return self.decks[seed] 
        return self.load_decks(seed)

    def _save_decks(self, seed: int, decks: np.ndarray):
        """Saves generated decks to a file, possibly splitting into multiple files if needed."""

        num_files = (decks.shape[0] // MAX_DECKS_PER_FILE) + (1 if decks.shape[0] % MAX_DECKS_PER_FILE > 0 else 0)
        
        for i in range(num_files):
            start_idx = i * MAX_DECKS_PER_FILE
            end_idx = min((i + 1) * MAX_DECKS_PER_FILE, decks.shape[0])
            
            filename = os.path.join(self.storage_dir, f"decks_{seed}_part{i + 1}.npy")
            np.save(filename, decks[start_idx:end_idx])
            print(f"Decks saved with seed {seed} at {filename}")

    def _save_seeds(self, seed: int):
        """Logs seed values for reproducibility."""
        with open(self.seeds_file, "r") as f:
            seeds = json.load(f)
        if seed not in seeds:
            seeds.append(seed)
            with open(self.seeds_file, "w") as f:
                json.dump(seeds, f)

    def load_decks(self, seed: int):
        """Loads decks from saved storage using a seed."""
        with open(self.seeds_file, "r") as f:
            seeds = json.load(f)
        if seed not in seeds:
            print(f"Seed {seed} not found in log. Cannot load decks.")
            return None
        
        matching_files = [f for f in os.listdir(self.storage_dir) if f.startswith(f"decks_{seed}")]
        if not matching_files:
            print(f"Decks with seed {seed} not found.")
            return None

        all_decks = []
        for filename in matching_files:
            file_path = os.path.join(self.storage_dir, filename)
            all_decks.append(np.load(file_path))
        return np.concatenate(all_decks, axis=0)

    def count_decks(self, seed: int):
        """Counts the total number of decks stored for a given seed."""
        matching_files = [f for f in os.listdir(self.storage_dir) if f.startswith(f"decks_{seed}")]
        
        if not matching_files:
            print(f"No decks found for seed {seed}.")
            return 0
    
        total_decks = 0
        for filename in matching_files:
            file_path = os.path.join(self.storage_dir, filename)
            decks = np.load(file_path)
            total_decks += decks.shape[0]
    
        return total_decks



def generate_decks(n_decks: int, seed: int, half_deck_size: int = HALF_DECK_SIZE) -> np.ndarray:
    """
    Generates shuffled decks using the given seed.
    """
    init_deck = [0] * half_deck_size + [1] * half_deck_size
    decks = np.tile(init_deck, (n_decks, 1)) 

    rng = np.random.default_rng(seed)

    for deck in decks:
        rng.shuffle(deck) 

    return decks


def generate_sequences():
    """
    Generates all possible binary sequences of length 3 for Penney’s Game (excluding duplicates).
    Returns a list of lists, where each inner list is a binary sequence.
    """
    return [[int(x) for x in format(i, '03b')] for i in range(8)]  



def generate_and_save_decks(seed: int, n_decks: int) -> None:
    seed = seed  
    n_decks = n_decks 

    deck_storage = DeckStorage()

    deck_storage.add_decks(n_decks, seed)
    print(f"Generated and saved {n_decks} decks with seed {seed}.")
