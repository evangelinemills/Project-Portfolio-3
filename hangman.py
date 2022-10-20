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
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_execution = "".join(word_as_list)  #Replaces underscore with letter guessed correctly
                if "_" not in word_execution:
                    guessed = True 
        elif len(guess) == len(word) and guess.isalpha():  #Checks for correctly guessed words
            if guess in guessed_words:
                print("You've guessed the word!", guess)
            elif guess != word:
                print("Oh No!", guess , "is not the word!")
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
    phases = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    return phases[tries]


def main():
    word = obtain_word()
    play(word)
    while input("Are you brave enough to try again? (Y/N) ").upper == "Y":
        word = obtain_word()
        play(word)


if __name__ == "__main__":
    main()
