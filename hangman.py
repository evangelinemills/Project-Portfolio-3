import random  #imports random library
from words import list_of_words  #imports the list of words from words.py


def obtain_word():
    """
    Gets a random word from the imported words list
    Returns it in UPPER case for user readability
    """
    word = random.choice(list_of_words)
    return word.upper()


def play_game(word):
    """
    Displays the word during the users turn as underscores
    As a correct letter is guessed it will replace
    the underscore with the guessed letter
    """
    word_execution = "_" + len(word)  #displays underscores instead of letters
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6  #number of body parts on hangman = number of guesses
    print("Lets Hang the Man!!")
    print(hangman_display(tries))
    print(word_execution)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a LETTER or WORD: ")  #input field in terminal for guess
        if len(guess) == 1 guess.isalpha():  #checks guess is alphabetic
            if guess in guessed_letters:
                print("You've already guessed this letter silly!!", guess)  #checks if already guessed
            elif guess not in word:
                print(guess, "is not in the word...watch out!")  #checks if guess not in word
                tries -= 1  #one less try
                guessed_letters.append(guess)  #adds guessed letter to list of guessed letters
            else:
                print("Correct! You're safe,", guess, "is in the word!")  #checks if correct guess
                guessed_letters.append(guess)
                word_as_list = list(word_execution)  #converts word into list to allow me to index into it
        elif len(guess) == len(word) and guess.isalpha():

        else:
            print("Not a valid guess!")
        print(hangman_display(tries))
        print(word_execution)
        print("\n")
