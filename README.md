# Slot Machine Simulator

This Python program simulates a slot machine within the terminal. It allows users to place bets, spin the slot machine reels, and check their winnings based on the combinations of symbols.

## Technologies Used

- **Python**: Programming language used to develop the slot machine simulator.

## Description

The program operates by defining several constants and dictionaries for symbol counts and values. It contains functions to handle gameplay, including:

- **checkWinnings**: Checks for winning combinations in the slot machine reels.
- **getSlotMachineSpin**: Generates random slot machine reels.
- **printSlotMachine**: Prints the slot machine reels in the terminal.
- **deposit**: Allows the user to input the initial deposit amount.
- **getNumbersOfLines**: Prompts the user to choose the number of lines to bet on.
- **getBet**: Takes the user's bet amount per line.
- **spin**: Executes a spin based on the user's input, calculates winnings, and adjusts the balance accordingly.
- **main**: The main function that controls the flow of the game, allowing users to play until they decide to quit.

The game loop continues until the user chooses to exit by pressing 'q' or 'Q'.

## How to Use

To run the program, execute the Python script. Follow the on-screen prompts to deposit money, place bets, and spin the slot machine reels. The winnings and remaining balance will be displayed throughout the game.

## Usage

```bash
python slot_machine.py
```

Feel free to explore the code and customize it as needed!

**Note:** This README assumes the file containing the code is named `slot_machine.py`. Adjust the command according to your actual file name if necessary.

Enjoy playing the slot machine simulator!
