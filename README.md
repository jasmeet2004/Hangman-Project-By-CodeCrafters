# Project Title

Building Hangman Game Repository on GitHub


##  Team Members

Jashan Yadav (2310992105)-(Project Tester)

Jasmeet Singh (2310992108)-(Project Manager)

Tanish Wadhwa (2310992149)-(Project Developer)


## Brief description about the project:-
This Python project implements a classic Hangman game, offering players an interactive and entertaining experience with various word categories and difficulty levels. The game begins with a user interface displaying the title "HANGMAN" in colorful ASCII art rendered using the pyfiglet module, creating an appealing visual introduction. Players are prompted to select a category from options like Animals, Fruits, Countries, Sports, and Car Companies, and then choose a difficulty level: easy, medium, or difficult. Once the category and difficulty level are chosen, a random word from the selected category and difficulty is generated for the player to guess. The game provides hints related to the chosen word, aiding players in their guesses. The user interface is designed to enhance the gaming experience, with colorful text and visual prompts guiding players through each step of the game. During gameplay, players input letters to guess the hidden word. Correct guesses reveal the positions of the letters within the word, while incorrect guesses result in the deduction of lives and progression through the Hangman stages. The hangman_stages module likely contains ASCII art representing the Hangman's gallows and stages of completion, adding visual interest and suspense to the game. As players progress, they earn points for each correct guess and lose points for each incorrect guess. The score is displayed throughout the game, providing feedback and motivation for players to continue playing and improve their performance. At the end of each round, players are presented with ASCII art messages indicating whether they have won or lost the game. They are then given the option to play again or exit the game, ensuring a seamless and enjoyable gaming experience. Overall, this Hangman game project combines elements of ASCII art, user interaction, and game mechanics to create a fun and engaging gameplay experience suitable for players of all ages. Its variety of word categories and difficulty levels make it a versatile and replayable game that can entertain players for hours on end.
## Instructions for running this game
(1)Launch the Game: Run the Python script in a Python environment or an IDE capable of running Python scripts.

(2)Install PyFiglet: PyFiglet is used to render ASCII art text in the game. You can install it via pip, Python's package manager.

(3)Title and Instructions: Upon launching, the game displays the title "HANGMAN" in colorful ASCII art. It provides instructions indicating that players will earn points for correct guesses and lose points for incorrect ones. Additionally, players are informed about the categories available for selection: Animals, Fruits, Countries, Sports, and Car Companies.

(4)Choose Category and Difficulty: Players are prompted to choose a category from the available options by entering the corresponding keyword (e.g., "Animals"). Then, they select a difficulty level by entering "easy," "medium," or "difficult."

(5)Receive Hint: After selecting the category and difficulty, the game provides a hint related to the chosen word from the selected category.

(6)Guess Letters: Players start guessing letters to uncover the hidden word. They input one letter at a time, trying to guess the word based on the provided hint and their knowledge of the category.

(7)Progress and Feedback: As players make guesses, the game updates the display to show correctly guessed letters and underscores for letters that have not yet been guessed. Players receive feedback on their guesses, with correct guesses revealing letters in the word and incorrect guesses deducting lives.

(8)Visual Progress: The game visually represents the Hangman's gallows and stages of completion using ASCII art. As players make incorrect guesses, the Hangman's figure progresses, adding suspense to the game.

(9)Win or Lose: The game continues until the player either correctly guesses the word or runs out of lives. If the player guesses the word correctly, they win the game, and an ASCII art message congratulating them is displayed. If the player exhausts all their lives without guessing the word, they lose the game, and an ASCII art message indicating defeat is shown.

(10)Play Again: After each game, players have the option to play again or exit the game. If they choose to play again, they can select a new category and difficulty level to start a new round.

(11)Score Tracking: Throughout the game, players' scores are updated based on their guesses. The final score is displayed at the end of the game, providing feedback on their performance.
