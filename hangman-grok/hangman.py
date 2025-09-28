import random
import hangman_words
import hangman_art

def get_valid_guess(guessed_letters):
    """Prompt for a valid single letter guess, ensuring it hasn't been guessed before."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a letter (A-Z).")
        elif guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
        else:
            return guess

def display_game_state(lives, display, guessed_letters):
    """Display the current game state: hangman stage, word progress, and guessed letters."""
    print(hangman_art.stages[lives])
    print(f"Word: {' '.join(display)}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Lives left: {lives}")

def play_hangman():
    """Main function to run the Hangman game."""
    # Game setup
    print(hangman_art.logo)
    print("Welcome to Hangman!")
    
    # Choose difficulty
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    lives = {"easy": 7, "medium": 5, "hard": 3}.get(difficulty, 5)  # Default to medium
    print(f"Starting with {lives} lives.")

    # Initialize game variables
    chosen_word = random.choice(hangman_words.word_list)
    display = ['_'] * len(chosen_word)
    guessed_letters = set()
    end_of_game = False

    # Main game loop
    while not end_of_game:
        display_game_state(lives, display, guessed_letters)
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        # Check if guess is in the word
        if guess in chosen_word:
            for position, letter in enumerate(chosen_word):
                if letter == guess:
                    display[position] = letter
        else:
            print(f"'{guess}' is not in the word. You lose a life!")
            lives -= 1

        # Check win/loss conditions
        if '_' not in display:
            display_game_state(lives, display, guessed_letters)
            print("Congratulations! You win!")
            end_of_game = True
        elif lives == 0:
            display_game_state(lives, display, guessed_letters)
            print(f"You lose! The word was '{chosen_word}'.")
            end_of_game = True

    # Ask to play again
    if input("Play again? (yes/no): ").lower().startswith('y'):
        play_hangman()

# Start the game
if __name__ == "__main__":
    play_hangman()