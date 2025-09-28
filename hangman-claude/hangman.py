#!/usr/bin/env python3
"""
Hangman Game - Main Module
A classic word guessing game with improved code structure and features.
"""

import random
from hangman_words import WORD_LIST
from hangman_art import LOGO, HANGMAN_STAGES


class HangmanGame:
    """Main Hangman game class with all game logic."""
    
    def __init__(self, max_lives=6):
        """Initialize the game with configurable lives."""
        self.max_lives = max_lives
        self.reset_game()
    
    def reset_game(self):
        """Reset game state for a new round."""
        self.chosen_word = random.choice(WORD_LIST).lower()
        self.guessed_letters = set()
        self.correct_guesses = set()
        self.lives_remaining = self.max_lives
        self.game_over = False
        self.won = False
    
    def get_display_word(self):
        """Return the current state of the word with guessed letters revealed."""
        return ' '.join([
            letter if letter in self.correct_guesses else '_' 
            for letter in self.chosen_word
        ])
    
    def is_valid_guess(self, guess):
        """Validate user input."""
        if len(guess) != 1:
            print("❌ Please enter only one letter.")
            return False
        
        if not guess.isalpha():
            print("❌ Please enter only letters.")
            return False
        
        if guess in self.guessed_letters:
            print(f"❌ You already guessed '{guess}'. Try a different letter.")
            return False
        
        return True
    
    def make_guess(self, guess):
        """Process a player's guess."""
        guess = guess.lower()
        
        if not self.is_valid_guess(guess):
            return
        
        self.guessed_letters.add(guess)
        
        if guess in self.chosen_word:
            self.correct_guesses.add(guess)
            print(f"✅ Good guess! '{guess}' is in the word.")
            
            # Check if player won
            if set(self.chosen_word) <= self.correct_guesses:
                self.won = True
                self.game_over = True
        else:
            self.lives_remaining -= 1
            print(f"❌ Sorry, '{guess}' is not in the word.")
            
            # Check if player lost
            if self.lives_remaining <= 0:
                self.game_over = True
    
    def display_game_state(self):
        """Display current game state."""
        print("\n" + "="*50)
        print(f"Word: {self.get_display_word()}")
        print(f"Lives remaining: {self.lives_remaining}")
        
        # Show hangman art if available
        stage_index = self.max_lives - self.lives_remaining
        if stage_index < len(HANGMAN_STAGES):
            print(HANGMAN_STAGES[stage_index])
        
        # Show guessed letters
        if self.guessed_letters:
            sorted_guesses = sorted(list(self.guessed_letters))
            print(f"Guessed letters: {', '.join(sorted_guesses)}")
        print("="*50)
    
    def play_round(self):
        """Play a single round of hangman."""
        print("\n🎮 New game started!")
        self.display_game_state()
        
        while not self.game_over:
            try:
                guess = input("\n💭 Guess a letter: ").strip()
                if not guess:
                    print("❌ Please enter a letter.")
                    continue
                
                self.make_guess(guess)
                self.display_game_state()
                
            except KeyboardInterrupt:
                print("\n\n👋 Game interrupted. Thanks for playing!")
                return False
            except Exception as e:
                print(f"❌ An error occurred: {e}")
                continue
        
        # Game end messages
        if self.won:
            print(f"\n🎉 Congratulations! You won!")
            print(f"🎯 The word was: '{self.chosen_word}'")
            print(f"📊 You had {self.lives_remaining} lives remaining.")
        else:
            print(f"\n💀 Game Over!")
            print(f"🎯 The word was: '{self.chosen_word}'")
            print(f"🔤 You guessed: {', '.join(sorted(self.guessed_letters))}")
        
        return True
    
    def get_game_stats(self):
        """Return current game statistics."""
        return {
            'word': self.chosen_word,
            'guessed_letters': list(self.guessed_letters),
            'correct_guesses': list(self.correct_guesses),
            'lives_remaining': self.lives_remaining,
            'won': self.won,
            'game_over': self.game_over
        }


def play_hangman():
    """Main function to run the hangman game with replay functionality."""
    print(LOGO)
    print("🎯 Welcome to the Improved Hangman Game!")
    print("📝 Guess the word by entering one letter at a time.")
    print("💀 You lose a life for each wrong guess!")
    
    games_played = 0
    games_won = 0
    
    while True:
        game = HangmanGame()
        
        # Play a round
        if game.play_round():
            games_played += 1
            if game.won:
                games_won += 1
        else:
            break  # User interrupted
        
        # Ask to play again
        while True:
            try:
                play_again = input("\n🔄 Would you like to play again? (y/n): ").strip().lower()
                if play_again in ['y', 'yes', '1', 'true']:
                    break
                elif play_again in ['n', 'no', '0', 'false']:
                    # Show final stats
                    if games_played > 0:
                        win_rate = (games_won / games_played) * 100
                        print(f"\n📈 Final Statistics:")
                        print(f"🎮 Games played: {games_played}")
                        print(f"🏆 Games won: {games_won}")
                        print(f"📊 Win rate: {win_rate:.1f}%")
                    
                    print("\n👋 Thanks for playing Hangman! Goodbye!")
                    return
                else:
                    print("❌ Please enter 'y' for yes or 'n' for no.")
            except KeyboardInterrupt:
                print("\n👋 Thanks for playing!")
                return


if __name__ == "__main__":
    play_hangman()