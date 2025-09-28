# --- hangman.py ---
# This is the main file to run the game.

import random
# We import our custom modules for words and art
import hangman_words 
import hangman_art

# --- Game Setup ---
# Get a random word and its category using the new function
chosen_word, category = hangman_words.get_random_word()
word_length = len(chosen_word)

# Set up game state variables
lives = 6
game_is_over = False
guessed_letters = [] # A list to keep track of every letter the user has guessed

# --- Create the initial display (e.g., "_ _ _ _ _") ---
display = ["_"] * word_length

# --- Welcome the Player ---
print(hangman_art.logo)
# Give the player a hint by telling them the word's category
print(f"Hint: The category is '{category.title()}'") 

# Optional: for testing, you can uncomment the line below to see the word
# print(f"Pssst, the solution is {chosen_word}")

# --- Main Game Loop ---
# The loop continues as long as the game is not over
while not game_is_over:
    
    # --- Player Input ---
    guess = input("Guess a letter: ").lower()

    # --- Input Validation ---
    # If the user has already guessed this letter, let them know and restart the loop
    if guess in guessed_letters:
        print(f"You've already tried the letter '{guess}'. Please pick another one.")
        print("-" * 40)
        continue # 'continue' skips to the next iteration of the loop

    # Add the new guess to our list of guessed letters
    guessed_letters.append(guess)

    # --- Check the Guess ---
    # We use a flag to check if the letter was found in this turn
    letter_found = False
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            letter_found = True
            
    # --- Handle Incorrect Guess ---
    if not letter_found:
        lives -= 1
        print(f"Sorry, the letter '{guess}' is not in the word. You lose a life.")
        
        # Check if the player has run out of lives
        if lives == 0:
            game_is_over = True
            print("You lose! 😢")
            print(f"The word was: {chosen_word}")

    # --- Update Display for the Player ---
    # Show the current state of the hangman drawing
    print(hangman_art.stages[lives])
    # Show the word with guessed letters revealed
    print(f"{' '.join(display)}")
    # Show which letters have been tried so far
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print("-" * 40) # Add a separator for better readability

    # --- Check for Win Condition ---
    # If there are no more underscores in the display, the player has won
    if "_" not in display:
        game_is_over = True
        print("Congratulations, you win! 🎉")
