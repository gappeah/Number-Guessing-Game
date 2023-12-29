import random
import tkinter as tk
import ttkbootstrap as ttk
import customtkinter
from tkinter import messagebox

def check_guess():
    global attempts
    guess = int(guess_entry.get())
    guess_entry.delete(0, 'end')

    if guess < number:
        message_label.config(text="Too low, try again.")
    elif guess > number:
        message_label.config(text="Too high, try again.")
    else:
        message_label.config(text="Congratulations! You guessed the number in {} attempts.".format(attempts))
        play_again = messagebox.askyesno("Number Guessing Game", "Do you want to play again?")
        if play_again:
            reset_game()
        else:
            root.destroy()

    attempts += 1

def reset_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 1
    message_label.config(text="")
    guess_entry.delete(0, 'end')

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x150")

number = random.randint(1, 100)
attempts = 1

label = tk.Label(root, text="Guess a number between 1 and 100:")
label.pack()

message_label = tk.Label(root, text="")
message_label.pack(pady=10)

guess_entry = tk.Entry(root, width=10)
guess_entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack(pady=5)

root.mainloop()