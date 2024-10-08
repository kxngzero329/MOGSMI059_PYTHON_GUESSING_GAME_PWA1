import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0
max_attempts = 10

print("Welcome to the number guessing game!")
print(f"Guess the number (between 1 and 100). You have {max_attempts} attempts.")

# Loop to allow the user 10 attempts to guess the number
while attempts < max_attempts:
    try:
        # Prompt the user to enter a guess
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == random_number:
            print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
            break
        elif guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    
# If the player didn't guess the number in the given attempts
if attempts == max_attempts and guess != random_number:
    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {random_number}.")
