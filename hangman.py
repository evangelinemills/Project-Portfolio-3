import random  #imports random library
from words import list_of_words  #imports the list of words from words.py


def obtain_word():
    """
    Gets a random word from the imported words list
    Returns it in UPPER case for user readability
    """
    word = random.choice(list_of_words)
    return word.upper()
