import random 

def number_guessing():
    number = random.randint(1,100)
    guess = None
    attempts = 0
    
    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break

# Call the function to start the number guessing game
number_guessing()           
