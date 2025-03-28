## ProjectPenney

# Overview

ProjectPenney is a data generation and visualization tool designed to simulate Penney's Game, a probability-based game involving binary sequences (Red/Black). The game is played between two players and revolves around the occurrence of specific three-sequence combinations in a randomly generated sequence.

## How the Game Works:
1. Player 1's Choice: Player 1 selects a three-sequence combination of Red (R) and Black (B). For example, they may choose "RRB".

2. Player 2's Choice: Player 2 then selects a different three-sequence combination, such as "RBB".

3. Sequence Generation: A long random binary sequence of Red and Black is generated (a deck).

4. Trick : The game progresses by checking which player's chosen sequence appears first in the generated sequence. The player whose sequence appears first wins the "trick".

5. The table is then cleared and the cards are collected by the trick winner. The game continues until the deck runs out.

6. Statistical Analysis: Over multiple simulated rounds, the game evaluates the percentage chance of Player 2 winning based on Player 1's selection.
   
## Tricks 
   - A trick is won when a players sequence appears in the shuffled deck
   - Each trick is worth 1 point

## Cards
   - Cards are awarded when a player's sequence matches the generated sequence, winning a trick.
   - The minimum number of cards won is three, corresponding to the length of the sequence. The count of won cards starts from the first card after the previous trick and extends to the       last card of the newly matched trick.

# Folder Structure 

You will find all of the files you will be using in the src/ folder. Inside this folder are 4 files. 

/src
   - __init__.py : Do not modify. This file initializes the module.
   - datagen.py : Generates and prepares decks for analysis.
   - helpers.py : Contains debugging tools.
   - processing.py : Simulates games and calculates percentages.
   - visualization.py : Creates heatmap using Player 2 win percentages.
   - heatmap_player2.png: Final saved heatmap for n=1000000

/data : stores the shuffled decks in .npy files
   - seeds.json : stores the seeds for reproducability
   - results.json : contains the percentage results 
   
   
## Quick Start Guide

# Run the script in a terminal 

python3 main.py

Will Print: Simulation complete, results saved, and heatmaps visualized successfully.
Heatmaps saved in the 'saved_heatmaps' folder.




