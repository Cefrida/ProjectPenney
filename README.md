## ProjectPenney

# Overview

ProjectPenney is a data generation and visualization tool designed to simulate "Penney's Game".  This game is a binary (Red/Black) sequence generating game between two players. One player selects a 3 sequence combination of red and black, then the other player chooses a different sequence. This code is used to simulate this game by analyzing the percentage chance of Player 2 winning given player 1's chosen sequence. The output is a heatmap visualization showing the likelihood of Player 2 winning, in percentages both by tricks and cards. 

Tricks 
   - A trick is won when a players sequence appears in the shuffled deck
   - Each trick is worth 1 point

Cards
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
   - heatmap_player2.png: Final saved heatmap for n=10,000

/data : stores the shuffled decks in .npy files
   - seeds.json : stores the seeds for reproducability
   - results.json : contains the percentage results 
   
   
# Quick Start Guide



