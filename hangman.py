# Hangman Game

import random
import hangman_words

#from hangman_art import logo
#print(logo)

print("The Hangman Game!") 
lives = 5
print(f"Total lives: {lives}")

#word_list = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(hangman_words.word_list)

#print(chosen_word)

display = []
for letter in chosen_word:
    display += "_"


end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}.")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You Win!")
    
    print(f"Lives left: {lives}")
    

