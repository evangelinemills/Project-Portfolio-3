import random  #imports random library
from words import list_of_words  #imports the list of words from words.py
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

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
    word_execution = "_" * len(word)  #displays underscores instead of letters
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6  #number of body parts on hangman = number of guesses
    print(Fore.CYAN + """LETS PLAY
 _     _   _____   _     _   _____    __   __    _____   _     _ 
(_)   (_) (_____) (_)   (_) (_____)  (__)_(__)  (_____) (_)   (_)
(_)___(_)(_)___(_)(__)_ (_)(_)  ___ (_) (_) (_)(_)___(_)(__)_ (_)
(_______)(_______)(_)(_)(_)(_) (___)(_) (_) (_)(_______)(_)(_)(_)
(_)   (_)(_)   (_)(_)  (__)(_)___(_)(_)     (_)(_)   (_)(_)  (__)
(_)   (_)(_)   (_)(_)   (_) (_____) (_)     (_)(_)   (_)(_)   (_)
""")
    
    difficulty_level = False
    while difficulty_level is False:
        difficulty = input(Fore.LIGHTGREEN_EX + """Please select a level: E = Easy, H = Hard: """).upper()
        os.system("clear")
        if difficulty == "E":
            tries = 6
            print(Fore.LIGHTMAGENTA_EX + "You've chosen Easy, you have ", tries, "tries.")
            difficulty_level = True
        elif difficulty == "H":
            tries = 6
            print(Fore.LIGHTMAGENTA_EX + "You've chosen Hard, you have ", tries, "tries.")
            difficulty_level = True
        else:
            print(Fore.LIGHTYELLOW_EX + difficulty, "is not a difficulty!")

    print(hangman_display(tries))
    print(word_execution)
    print(" \n ")
    while not guessed and tries > 0:
        guess = input(Fore.LIGHTRED_EX + "Guess a LETTER or WORD: ").upper()  #input for guess
        if len(guess) == 1 and guess.isalpha():  #checks guess is alphabetic
            if guess in guessed_letters:  #checks if already guessed
                print(Fore.LIGHTRED_EX + "Oh dear! You've already guessed this letter silly!!")  
            elif guess not in word:  #checks if guess not in word
                print(Fore.LIGHTYELLOW_EX + guess, "is not in the word...watch out! Try again!")  
                tries -= 1  #one less try
                guessed_letters.append(guess)  #adds guessed letter to list
            else:  #checks if correct guess
                print(Fore.LIGHTMAGENTA_EX + "Correct! You're safe,", guess, "is in the word!")  
                guessed_letters.append(guess)
                word_as_list = list(word_execution)  #converts word into list
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_execution = "".join(word_as_list)  #Replaces _ with letter
                if "_" not in word_execution:
                    guessed = True 
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(Fore.CYAN + "You've guessed the word!", guess)
            elif guess != word:
                print(Fore.BLUE + "Oh No!", guess , " is not the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True  #Checks for correct guess
                word_execution = word
        else:
            print(Fore.LIGHTBLUE_EX + "Not a valid guess!")
        print(hangman_display(tries))
        print(word_execution)
        print("\n")
    if guessed:
        print(Fore.BLUE + """Phew! You've survived a hanging today!
                                                                         _ 
 _       _  ______  _       _          _____    _____   _     _  ______ (_)
(_)  _  (_)(______)(_)     (_)        (_____)  (_____) (_)   (_)(______)(_)
(_) (_) (_)(_)__   (_)     (_)        (_)  (_)(_)   (_)(__)_ (_)(_)__   (_)
(_) (_) (_)(____)  (_)     (_)        (_)  (_)(_)   (_)(_)(_)(_)(____)  (_)
(_)_(_)_(_)(_)____ (_)____ (_)____    (_)__(_)(_)___(_)(_)  (__)(_)____  _ 
 (__) (__) (______)(______)(______)   (_____)  (_____) (_)   (_)(______)(_)
                                                                           
    """)
    else:
        print(Fore.LIGHTWHITE_EX + "Sorry, your time is up, youre out of luck! The word was " + word, "!")


def hangman_display(tries):
    """
    Phase images of hangman for user feedback
    A new phase appears after each incorrect guess
    """
    phases = [
        # final stage: head, torso, both arms and both legs
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
                                                                           _ 
  _____    _____    __   __   ______      _____   _     _  ______  _____  (_)
 (_____)  (_____)  (__)_(__) (______)    (_____) (_)   (_)(______)(_____) (_)
(_)  ___ (_)___(_)(_) (_) (_)(_)__      (_)   (_)(_)   (_)(_)__   (_)__(_)(_)
(_) (___)(_______)(_) (_) (_)(____)     (_)   (_)(_)   (_)(____)  (_____) (_)
(_)___(_)(_)   (_)(_)     (_)(_)____    (_)___(_) (_)_(_) (_)____ ( ) ( )  _ 
 (_____) (_)   (_)(_)     (_)(______)    (_____)   (___)  (______)(_)  (_)(_)
''',
# head, torso, both arms and one leg
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
# head, torso and both arms
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
# head, torso and one arm
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
# head and torso
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
# head
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
# Initial state: empty
        '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
]
    return phases[tries]


def main():
    word = obtain_word()
    play_game(word)
    while input(Fore.LIGHTYELLOW_EX + "Are you brave enough to try again? (Y/N) ").upper == "Y":
        word = obtain_word()
        play_game(word)


if __name__ == "__main__":
    main()
