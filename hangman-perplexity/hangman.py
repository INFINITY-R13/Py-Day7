import random
import hangman_words
import hangman_art


def display_logo():
    print(hangman_art.logo)


def get_random_word():
    return random.choice(hangman_words.word_list)


def initialize_display(word):
    return ["_" for _ in word]


def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
        elif guess in already_guessed:
            print(f"You have already guessed '{guess}'. Try another letter.")
        else:
            return guess


def update_display(chosen_word, display, guess):
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter


def play_game():
    display_logo()
    print("Welcome to The Hangman Game!")
    lives = 6  # Increased lives to 6
    print(f"Total lives: {lives}")
    chosen_word = get_random_word()
    display = initialize_display(chosen_word)
    guessed_letters = set()
    end_of_game = False

    while not end_of_game:
        print(f"\n{' '.join(display)}")
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in chosen_word:
            update_display(chosen_word, display, guess)
        else:
            lives -= 1
            print(f"You guessed '{guess}', that's not in the word. You lost a life.")
            print(hangman_art.stages[6 - lives])  # Adjusted indexing for 6 lives total

            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was: {chosen_word}")

        if "_" not in display:
            end_of_game = True
            print("You Win!")
            print(f"The word was: {chosen_word}")

        print(f"Lives left: {lives}")


if __name__ == "__main__":
    play_game()
