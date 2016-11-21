# Random 1-10
# Get a guess from the plater
# Compare guess to secret number
# Print hit/miss

import random

def get_guess():
    while True:
        try:
            guess = int(input("What is the number? "))
        except ValueError:
             print("That's not a number")
        else:
            return guess
            break

def check_guess(guess, val):
    if guess == val:
        return True
    else:
        return False
      
def high_or_low(guess, val):
    if guess < val:
        return "too low"
    else:
        return "too high"

def game():
    secret_val = random.randint(1, 10)
    guess = get_guess()
    max_guesses = 5
    curr_guesses = 1

    while not check_guess(guess, secret_val):
        print("Not quite, {}".format(high_or_low(guess, secret_val)))
        if curr_guesses < max_guesses:
            guess = get_guess()
            curr_guesses += 1
        else:
            break
            
    if check_guess(guess, secret_val):
        print("You got it!")
    else:
        print("You are out of guesses, it was {}".format(secret_val))
        
while True:
    if input("Do you want to play a guessing game? (Y/N) ") == "Y":
        game()
    else:
        break