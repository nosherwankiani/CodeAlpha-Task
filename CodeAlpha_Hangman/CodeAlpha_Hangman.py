import random

def play_hangman():
    # 1. Small list of 5 predefined words
    words = ['python', 'developer', 'internship', 'software', 'coding']
    secret_word = random.choice(words)

    # 2. Game variables
    guessed_letters = []
    max_attempts = 6
    incorrect_guesses = 0

    print("Welcome to the CodeAlpha Hangman Game!")
    print(f"You are allowed {max_attempts} incorrect guesses.\n")

    # 3. Main game loop (while loop)
    while incorrect_guesses < max_attempts:
        # Build the current state of the word to display
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(f"Word to guess: {display_word}")
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")

        # Check for win condition (if-else)
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            return

        # Get player input
        guess = input("Guess a single letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter! Try another one.\n")
            continue

        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in secret_word:
            print("Correct guess!\n")
        else:
            print("Incorrect guess!\n")
            incorrect_guesses += 1

    # Loop ends when incorrect_guesses reaches max_attempts (Loss condition)
    print("Game Over! You've run out of guesses.")
    print(f"The secret word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()