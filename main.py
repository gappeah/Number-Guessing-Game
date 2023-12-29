import random
import tkinter as tk
#import ttkbootstrap as ttk
import customtkinter
from tkinter import messagebox

def check_guess():
    global attempts
    guess = int(guess_entry.get())
    guess_entry.delete(0, 'end')

    if guess < number:
        message_label.configure(text="Too low, try again.")
    elif guess > number:
        message_label.configure(text="Too high, try again.")
    else:
        message_label.configure(text="Congratulations! You guessed the number in {} attempts.".format(attempts))
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
    message_label.configure(text="")
    guess_entry.delete(0, 'end')

root = customtkinter.CTk()
root.title("Number Guessing Game")
root.geometry("700x300")


number = random.randint(1, 100)
attempts = 1

label = customtkinter.CTkLabel(root, text="Guess a number between 1 and 100:")
label.pack()

message_label = customtkinter.CTkLabel(root, text="")
message_label.pack(pady=10)

guess_entry = customtkinter.CTkEntry(root, width=40)
guess_entry.pack(pady=5)

guess_button = customtkinter.CTkButton(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

reset_button = customtkinter.CTkButton(root, text="Reset", command=reset_game)
reset_button.pack(pady=5)

root.mainloop()