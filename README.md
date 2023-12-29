# Number Guessing Game with GUI

This Python code creates a fun number guessing game with a user-friendly interface!

Here's how it works:

1. Imports the necessary modules:

    random: Generates random numbers for the game.
    tkinter: Creates the graphical user interface (GUI).
    messagebox: Displays pop-up messages for user interaction.

2. Defines the check_guess() function:

    Retrieves the player's guess from the entry field.
    Compares it to the secret number:
        If too low, displays "Too low, try again."
        If too high, displays "Too high, try again."
        If correct, congratulates the player and prompts for a new game.
    Increments the attempt counter.

3. Defines the reset_game() function:

    Generates a new random number for the next round.
    Resets the attempt counter to 1.
    Clears the message label and entry field for fresh gameplay.

4. Sets up the GUI:

    Creates the main window with the title "Number Guessing Game" and a size of 300x150 pixels.
    Generates an initial random number between 1 and 100.
    Sets the initial attempt count to 1.
    Adds the following elements to the window:
        Label: Displays instructions to guess a number.
        Message label: Shows feedback after each guess.
        Entry field: Allows the player to enter their guess.
        Guess button: Triggers the check_guess() function when clicked.
        Reset button: Triggers the reset_game() function to start a new game.

5. Launches the main event loop:

    Activates the GUI and keeps it running until the player closes the window.

To play the game:

    Run the code.
    Enter your guess in the entry field.
    Click the "Guess" button.
    The message label will provide feedback.
    Keep guessing until you get the correct number!
    After a successful guess, choose to play again or exit the game.

Enjoy the guessing challenge!