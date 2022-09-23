# Pokemon Battle

## Description:
A turn-based Pokemon Battle simulator  written in Python using OOP. The program will randomly generate each Pokemon and 3 element-based attacks and 1 normal (non-elemental) attack by importing them from csv files.

## Game Rules:
The User will choose a Pokemon from their list to battle against a computer’s randomly generated Pokemon. The Pokemon will alternate attacks with its corresponding damage and accuracy. The winner is determined once the opponent’s Pokemon’s health points reach zero. 

**Additional playing rules:**

Every turn, the user can decide whether to **FIGHT**, reach for **BAG**, or **RUN** away from battle.

* **FIGHT:** This will prompt the Pokemon’s randomized list of moves to display. The User will input the number that corresponds to the attack they wish to command their Pokemon to execute.

* **BAG:** This will prompt the list of health potions to display. The User will input the number that corresponds to the health potion they wish to use on their Pokemon. If no items exist in the bag, the user will waste their turn.

* **RUN:** This will immediately end the battle. 

**Extra Features:**

* Displays health bar and health points after exchanging attacks from both Pokemon

* Randomly generates Computer's Pokemon, Computer's Pokemon move set, and Computer's attack choice

* Imports and reads data from CSV file to implement Pokemon attributes and Pokemon move set

* Determines the Pokemon who attacks first by comparing the speed attribute of the Pokemon
