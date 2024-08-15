import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = get_valid_word(words)
    word_letter = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has geussed
    
    #getting user input
    user_letter = input("Guess a letter: ").upper()
    
user_input = input("Type something: ")
print(user_input)