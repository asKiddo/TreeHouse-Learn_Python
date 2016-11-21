# Make a list of words
# Pick a random word
# Draw spaces
# Take a guess
# Draw guessed letters and strikes
# Print out win/lose

import random
word_list = ['apple','banana','orange','red','blue','summer','wine','xylophone']

def get_guess():
    return input("Guess a letter: ").lower()

def game():
    word = random.choice(word_list)
    guessed_word = list("_"*len(word))
    max_guesses = 10
    guessed_letters = []
    wrong_letters = []
	
    while list(word) != guessed_word:
	    print("Here is what you know so far: {}".format(''.join(guessed_word)))
	    print("Here are the letters not in the word: {}".format(', '.join(wrong_letters)))
		
	    if len(wrong_letters) < max_guesses:
		    guessed_letters.append(get_guess())
		    if guessed_letters[-1] in word: # correct guess
			    indices = [i for i, x in enumerate(word) if x == guessed_letters[-1]]
			    for idx in indices:
				    guessed_word[idx] = guessed_letters[-1]
		    else: # incorrect guess
			    wrong_letters.append(guessed_letters[-1])
	    else:
		    break
	
    if list(word) != guessed_word:
	    print("Sorry, you ran out of guesses, the word was {}".format(word))
    else:
	    print("You got it! The word was {}".format(word))
		
game()