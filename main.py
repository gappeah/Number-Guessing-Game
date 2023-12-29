
import random 

def number_guessing():
    number = random.randint(1,100)
    guess = None
    attempts = 0
    
#Because guess is set to None, the while loop will run at least once
    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
    
    
        if guess < number:
            print("Too low, try again.")
            guess = int(input("Guess a number between 1 and 100: "))
            
        elif guess > number:
            print("Too high, try again.")
            guess = int(input("Guess a number between 1 and 100: "))

        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
        break

number_guessing()
    
    
