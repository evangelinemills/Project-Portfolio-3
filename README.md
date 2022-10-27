# HANGMAN
# Portfolio Project 3

Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

The game can be found [here]().

(Am I Responsive Images)

## How to play
----
- The game begins with a welcome message. The image was generated using the Ascii graffiti generator [PatorJK.](http://patorjk.com/software/taag/#p=display&h=1&v=2&f=Pawp&t=Hangman). I ensure the style is easy to read.

(IMAGE)

- The game then asks the user to choose a difficulty level. They can select Easy by pressing E or Hard by pressing H on the keyboard. Easy gives the user 6 tries and Hard gives the user 4 tries, to guess the word. If the user tries to input any other key the game will not accept it and will ask the question again. 

(IMAGE)

- The game will then provide an image of the empty gallows with a line of underscores underneath. This shows the length of the word. The game asks the user to guess a letter or word.
 
 (IMAGE)

 - The user begins by picking a letter. If they guess correct, the letter appears on screen in its respective place in the word. The console also provides positive feedback telling the user they are correct.

 (IMAGE)

 - The player continues to guess letters. If incorrect, a body part appears in the galows and the console feeds back to the user saying the letter is not in the word and to try again,

 (IMAGE)

 - If the user should guess a letter again, that they already guessed, the comsole will tell them they already guessed that letter. The player does not lose a life and is prompted to guess again.

 (IMAGE)

 - If the player inputs a guess that is not a letter or word. The computer will feedback that it is not a valid guess and try again. The plater will not lose a life. 

 (IMAGE)

 - If the player guesses each letter correctly or figures out the word and types it in before they run out of tries and all the body parts appear in the gallows, they are congratulated for guessing the word correctly.

 (IMAGE)

 - If the player runs out of tries and they don't guess the word, they get a game over message and the computer reveales the word. The user is asked whether they would like to play again after each game. 

 (IMAGE)


## Features
----
- Random word selection
  * The computer randomly selects a word from the word list.
  * The player cannot access this word, only see the length and input word or letter guesses. 

- The user plays against the computer

- The computer accepts user input and gives responsive feedback

- Input validation and error-handling
  * You cannot enter a number.
  * You cannot enter a string of letters that isn't equal to the length of the word.
  * You cannot enter the same guess twice.

## Testing
----
### Code Validation
- I tested my code using [Python Checker.](https://www.pythonchecker.com/) I had to fix some minor spacing issues otherwise it passed.

### Manual Testing
- At the start of the game the player must select a level. E for Easy or H for Hard. These are the only two letters the computer should accept.
- Test: To test this, I input the E and H individually, both upper and lower case. I then tried other letters, words, numbers and punctuation keys to see if the game would continue.
- Result: Adding anything except E or H did not continue the game and the console told the user that theyre input was not a difficulty and re-asked the question to select E or H. 
- Verdict: Only E and H were accepted so it was a success.
----
- The user should only be able to guess a single letter or a word that equals the length of the word they are tyring to guess. Any number, punctuation mark or word that is longer or shorter than the one to be guessed ahould not be accepted. 
- Test: After starting the game and selecting a difficulty, I input words that were longer or shorter than the length of word I was tying to guess, i input numbers and I input symbols.
- Result: The game did not allow the player to add any symbols, numbers or word that did not equal the correct length. It told the user their input was incorrect and asked them to guess again. 
- Verdict: Only singular letters or words of the correct length were accepted as guesses and allowed the game to contine. The test was a success.
----
- The user should only be allowed to guess each letter/word once. If it is already guessed the computer should tell them and they do not lose a life.
- Test:







