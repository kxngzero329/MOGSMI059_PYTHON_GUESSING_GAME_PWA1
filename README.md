# MOGSMI059_PYTHON_GUESSING_GAME_PWA1

1. Generating a Random Number
The program starts by generating a random number between 1 and 100. This random number is stored in a variable. It will remain hidden, and the user has to guess 
this number during the game.

2. Setting Attempts and Limits
Two variables are set:
attempts is initialized to 0 to track how many guesses the user has made.
max_attempts is set to 10, which means the user can only guess up to 10 times.

3. User Instructions
The program provides a welcome message and explains the rules: the user needs to guess a number between 1 and 100, and they have 10 attempts to get it right.

4. The Guessing Loop
A loop runs that allows the user to guess the random number. Inside the loop:
The user is prompted to input their guess.
Each guess is checked against the random number.

5. Validating the Guess
Once the user enters a guess, the program compares it to the random number:
If the guess is correct: The program congratulates the user and informs them how many attempts they took to guess the number.
If the guess is too low or too high: The program gives feedback, telling the user whether their guess was too low or too high and allows them to try again.

6. Handling Invalid Inputs
If the user enters something that isn’t a valid number (like a string or special character), the program catches the error and prompts the user to enter a valid number.

7. Counting Attempts
Every time the user makes a guess, the program increments the attempts counter. This helps track how many guesses the user has made so far.

8. Game Over Conditions
The game can end in two ways:
The user guesses the number correctly within 10 attempts: The program displays a success message with the correct number and the total number of attempts.
The user fails to guess the number in 10 attempts: Once the user reaches the 10th guess and hasn’t guessed the number correctly, the program ends and reveals 
the correct number with a message indicating they ran out of tries.
This combination of looping, condition checking, and counting creates a simple and interactive guessing game with limited tries, offering feedback after each guess.
