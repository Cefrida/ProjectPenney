## ProjectPenney

# Overview

ProjectPenney is a data generation and visualization tool designed to simulate "Penney's Game".  This game is a binary (Red/Black) sequence generating game between two players. One player selects a 3 sequence combination of red and black, then the other player chooses a different sequence. This code is used to simulate this game by analyzing the percentage chance of Player 2 winning given player 1's sequence. The output is a heatmap visualization showing the likelihood of Player 2 winning, in percentages.

# Installation and Usage 

1. Ensure you have python installed. It is recommended to use a virtual environment:
   python3 -m venv .venv

2. Run the Datagen script. Modify Datagen to include the number of simulations and decks you want to run.
   python src/visualization.py

3. Run the Visualization script. This will output your heatmap in a new file.
   python src/visualization.py

# Folder Structure 

You will find all of the files you will be using in the src/ folder. Inside this folder are 4 files. 

- __init__.py : Do not modify. This file initializes the module.
- datagen.py : Generates and prepares decks for analysis.
- helpers.py : Contains debugging tools.
- processing.py : Simulates games and calculates percentages.
- visualization.py : Creates heatmap using Player 2 win percentages.
