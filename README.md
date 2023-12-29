# Number Guessing Game

**This Python code creates an interactive number guessing game with a sleek GUI using Tkinter and customtkinter.**

![image](https://github.com/gappeah/Number-Guessing-Game/assets/114095068/59a17c52-23c2-487f-b8b8-d23be2349ea9)


**Here's a breakdown of how it works:**

**1. Imports Necessary Libraries:**
   - `random`: Generates the random number for the game.
   - `tkinter`: Creates the base GUI elements.
   - `customtkinter`: Enhances the GUI's visual appeal.
   - `messagebox`: Displays prompts and messages.

**2. Defines Game Functions:**
   - `check_guess()`:
     - Takes the player's guess from the entry field.
     - Compares it to the secret number.
     - Provides feedback ("Too low," "Too high," or "Congratulations!").
     - Asks if the player wants to play again.
     - Resets the game or closes the window accordingly.
   - `reset_game()`:
     - Generates a new random number.
     - Resets the attempt count.
     - Clears the message and entry fields.

**3. Sets Up the GUI:**
   - Creates a `CTk` window with a title and size.
   - Generates a random number between 1 and 100.
   - Initializes the attempt count to 1.
   - Adds a label with instructions.
   - Creates a label for displaying feedback.
   - Adds an entry field for the player's guesses.
   - Adds a "Guess" button that calls the `check_guess()` function.
   - Adds a "Reset" button that calls the `reset_game()` function.

**4. Starts the Game Loop:**
   - The `root.mainloop()` function keeps the window open and responsive until it's closed.

**To play the game:**

1. Run the code.
2. The game window will appear.
3. Enter your guess in the entry field.
4. Click the "Guess" button.
5. The feedback label will indicate whether your guess was too high, too low, or correct.
6. If you guess correctly, you'll be asked if you want to play again.
7. Click "Yes" to start a new game or "No" to close the window.
8. You can also click the "Reset" button at any time to start a new game.
