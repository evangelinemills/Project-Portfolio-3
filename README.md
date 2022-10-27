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
- Test: After starting the game and selecting a difficulty, I input words that were longer or shorter than the length of word I was tying to guess, I input numbers and I input symbols.
- Result: The game did not allow the player to add any symbols, numbers or word that did not equal the correct length. It told the user their input was incorrect and asked them to guess again. 
- Verdict: Only singular letters or words of the correct length were accepted as guesses and allowed the game to contine. The test was a success.
----
- The user should only be allowed to guess each letter/word once. If it is already guessed the computer should tell them and they do not lose a life.
- Test: Whilst playing the game I repeatedly input the same letter/word. 
- Result: The computer prompted me that I had already guessed that letter/word and should try again. No life was lost.
- Verdict: This test was a success as the game prompted the user with a message and no life was lost.
----
- When the user loses a game, "Game Over" should appear with a message to inform the player of the word they were trying to guess. 
- Test: I played the game multiple time trying to guess incorrectly so as I would lose. 
- Result: Each time I lost the message popped up correctly at the end of the game. 
- Verdict: The test was a success. The message appeared correctly at the correct point in the game.
----
- When the user wins a game, "Well Done" should appear to congratulate the player.
- Test: I played the game multiple times trying to win.
- Result: By winning as many times as I could, the message came up at the end of the game.
- Verdict: The test was a success. Each time I won the game the correct message was displayed at the correct time. 
----
- When the user finishes the game, whether they win or lose, the game should ask them if they want to play again. The player can input Y for yes or N for no. If they select Y the game should restart, if they select N the terminal clears and the game ends. 
- Test: By finishing the game repeatedly I input Y or N to test the outcome. 
- Result: Y restated the game, N cleared the terminal and any other key was not accepted. 
- Verdict: The test was a success as the appropriate key carried out the correct function. 

### Bugs


## Technologies
----
### Languages
- [Python:](https://www.python.org/) This whole project was written using Python.
- [Markdown:](https://www.markdownguide.org/basic-syntax/) The read me is written using Markdown.

### Environment
- [GitHub:](https://github.com/) was used to host the code.
- [GitPod:](https://www.gitpod.io/?utm_source=googleads&utm_medium=search&utm_campaign=dynamic_search_ads&utm_id=16501579379&utm_content=dsa&gclid=EAIaIQobChMIn6TCrsyA-wIVDNPtCh319wDpEAAYASAAEgKK2vD_BwE) was used to write the code.
- [Heroku:](https://id.heroku.com/login) was the cloud hosting platform used to deploy this project.

### Packages
- [Colorama:](https://pypi.org/project/colorama/) was used to create coloured text and images in the game.

### Other
- [Graffiti:](http://patorjk.com/software/taag/#p=display&h=1&v=2&f=Pawp&t=Hangman)was used for the large text images in the game.

## Deployment
----
- I commited and pusehd all code fot the game to GitHub from GitPod.
- I created an account on [Heroku](https://id.heroku.com/login).
- I clicked on 'New' and clicked 'Create New App'.
- I then chose the correct region and named my app. 
- In settings I aorted out the Buildpacks for everything to work.
- I then clicked on the deploy page and linked my GitHub repo with the Heroku app.
- I then deployed the branch at the bottom of the page, ensuring no errors occured.
- I enabled automatic deploys so if I edit and push the code the Heroku automatically updates and redoploys.
- I then opened the game on Heroku to ensure it functions efficiently.

## References
----
- I watched multiple tutotials on YouTube to undertand the basics of Hangman code in Python. The [Kite](https://www.youtube.com/watch?v=m4nEnsavl6w) was especially helpful and helped me to understand the what and why of my code. 
- I used [Random Words Generator](https://randomwordgenerator.com) to get my words for the game. I was able to tailor the length and chose 50 words for each length.

## Acknowledgements
----
- I'd like to thank my mentor Richard Wells for all of the help and support throughout.
- Thank you to my family and friends for testing and feedback.
- Thank you to my peers on Slack for always being supportive. 

Evangeline Mills 2022









