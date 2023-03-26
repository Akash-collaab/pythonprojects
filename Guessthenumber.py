"""
import random

def guessnumber(x):
    random_number = random.randint(1,x)
    guessnumber = 0
    while guessnumber != random_number:
        guessnumber = int(input(f' Guess the number 1 and {x}:'))
        if guessnumber < random_number:
            print("Oops soory, the number is too low . Please guess again ")
        elif guessnumber > random_number:
            print("Oops soory, the number is too high . Please guess again")
        
    print(f"Hurry, congrats You have guessed the correct{random_number} correctly")
    



#Second code started

def computer_guess(x):
     low = 1
     high = x 
     feedback = ''
     while feedback != 'c':
        if low != high:       
            guess = random.randint(low, high)
        else:
            guess = low # could also be high bcus low=high   
        feedback = input(f'Is {guess} too high (H), too low(L),or correct (C)?? ' ).lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
     print(f'Yay !the computer guessed the number, {guess}, correctly! ')

computer_guess(10)

"""

import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


computer_guess(10)
