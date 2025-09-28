# hangman.py
import random
from hangman_words import word_list
from hangman_art import logo, stages

def play_game():
    print(logo)
    print("Welcome to the Hangman Game!\n")
    
    lives = len(stages) - 1  # number of stages = lives
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    
    display = ["_"] * word_length
    guessed_letters = set()
    
    print(f"The word has {word_length} letters.")
    print(" ".join(display))
    print(f"You have {lives} lives.\n")
    
    while lives > 0 and "_" in display:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.\n")
            continue
        
        guessed_letters.add(guess)
        
        if guess in chosen_word:
            for idx, letter in enumerate(chosen_word):
                if letter == guess:
                    display[idx] = letter
            print("Good guess!")
        else:
            lives -= 1
            print(f"Wrong guess. You lost a life. ({lives} left)")
            print(stages[lives])  # show the hangman stage
        
        print(" ".join(display))
        print()
    
    if "_" not in display:
        print("🎉 You Win!")
    else:
        print(f"💀 You Lose. The word was '{chosen_word}'.")
        

if __name__ == "__main__":
    play_game()
