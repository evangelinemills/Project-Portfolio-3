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
    word_execution = "_" * len(word)  #displays underscores instead of letters
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6  #number of body parts on hangman = number of guesses
    print(f"""LETS PLAY
 _     _   _____   _     _   _____    __   __    _____   _     _ 
(_)   (_) (_____) (_)   (_) (_____)  (__)_(__)  (_____) (_)   (_)
(_)___(_)(_)___(_)(__)_ (_)(_)  ___ (_) (_) (_)(_)___(_)(__)_ (_)
(_______)(_______)(_)(_)(_)(_) (___)(_) (_) (_)(_______)(_)(_)(_)
(_)   (_)(_)   (_)(_)  (__)(_)___(_)(_)     (_)(_)   (_)(_)  (__)
(_)   (_)(_)   (_)(_)   (_) (_____) (_)     (_)(_)   (_)(_)   (_)
""")

    print(hangman_display(tries))
    print(word_execution)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a LETTER or WORD: ").upper()  #input for guess
        if len(guess) == 1 and guess.isalpha():  #checks guess is alphabetic
            if guess in guessed_letters:  #checks if already guessed
                print("You've already guessed this letter silly!!", guess)  
            elif guess not in word:  #checks if guess not in word
                print(guess, "is not in the word...watch out!")  
                tries -= 1  #one less try
                guessed_letters.append(guess)  #adds guessed letter to list
            else:  #checks if correct guess
                print("Correct! You're safe,", guess, "is in the word!")  
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
                print("You've guessed the word!", guess)
            elif guess != word:
                print("Oh No!", guess , " is not the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True  #Checks for correct guess
                word_execution = word
        else:
            print("Not a valid guess!")
        print(hangman_display(tries))
        print(word_execution)
        print("\n")
    if guessed:
        print("Phew! Well done, you've survived a hanging today!")
    else:
        print("Sorry, your time is up, youre out of luck! The word was " + word)


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
=========''',
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
    while input("Are you brave enough to try again? (Y/N) ").upper == "Y":
        word = obtain_word()
        play_game(word)


if __name__ == "__main__":
    main()
