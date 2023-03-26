import random
from traceback import print_tb 
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  #randomly chooses something from the list 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word, this will use as a way of keeping track of what's actually already been used
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # lettss used
        # " " .join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have ', lives, 'lives left and you have guessed these letters: ', ' '.join(used_letters))
        
        # what current word is (ie W- R D)
        word_list = [letter if letter in used_letters else '-' for letter in word] 
        print('Current word: ',' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # tales away a life if worng
                print('\nLetter ,', user_letter, 'is not in the word')
                 

        elif user_letter in used_letters:
            print("You have already guessed that word. Please try again...")

        else:
            print("Invalid_character...")

    # gets here when len(words) == 0 OR lives == 0 
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print('Yay! You have guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()