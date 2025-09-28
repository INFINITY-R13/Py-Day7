"""
Hangman Art Module
Contains ASCII art for the hangman game including logo and hangman stages.
"""

# Game logo
LOGO = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

🎯 The Ultimate Word Guessing Challenge! 🎯
'''

# Hangman stages (from no mistakes to game over)
HANGMAN_STAGES = [
    # Stage 0: No mistakes
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    
    # Stage 1: Head
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    
    # Stage 2: Body
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    
    # Stage 3: Left arm
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    
    # Stage 4: Right arm
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    
    # Stage 5: Left leg
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    
    # Stage 6: Right leg (Game Over)
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    💀 GAME OVER 💀
    '''
]

# Alternative colorful hangman stages (for terminals that support colors)
COLORFUL_HANGMAN_STAGES = [
    # Stage 0: No mistakes
    '''
    \033[33m  +---+\033[0m
    \033[33m  |   |\033[0m
    \033[33m      |\033[0m
    \033[33m      |\033[0m
    \033[33m      |\033[0m
    \033[33m      |\033[0m
    \033[33m=========\033[0m
    ''',
    
    # Stage 1: Head
    '''
    \033[33m  +---+\033[0m
    \033[33m  |   |\033[0m
    \033[31m  O   \033[33m|\033[0m
    \033[33m      |\033[0m
    \033[33m      |\033[0m
    \033[33m      |\033[0m
    \033[33m=========\033[0m
    ''',
    
    # Stage 2: Body
    '''
    \033[33m  +---+\033[0m
    \033[33m  |   |\033[0m
    \033[31m  O   \033[33m|\033[0m
    \033[31m  |   \033[33m|\033[0m
    \033[33m      |\033[0m
    \033[33m      |\033[0m
    \033[33m=========\033[0m
    ''',
    
    # Stage 3: Left arm
    '''
    \033[33m  +---+\033[0m
    \033[33m  |   |\033[0m
    \033[31m  O   \033[33m|\033[0m
    \033[31m /|   \033[33m|\033[0m
    \033[33m      |\033[0m
    \033[33m      |\033[0m
    \033[33m=========\033[0m
    ''',
    
    # Stage 4: Right arm
    '''
    \033[33m  +---+\033[0m
    \033[33m  |   |\033[0m
    \033[31m  O   \033[33m|\033[0m
    \033[31m /|\  \033[33m|\033[0m
    \033[33m      |\033[0m
    \033[33m      |\033[0m
    \033[33m=========\033[0m
    ''',
    
    # Stage 5: Left leg
    '''
    \033[33m  +---+\033[0m
    \033[33m  |   |\033[0m
    \033[31m  O   \033[33m|\033[0m
    \033[31m /|\  \033[33m|\033[0m
    \033[31m /    \033[33m|\033[0m
    \033[33m      |\033[0m
    \033[33m=========\033[0m
    ''',
    
    # Stage 6: Right leg (Game Over)
    '''
    \033[33m  +---+\033[0m
    \033[33m  |   |\033[0m
    \033[31m  O   \033[33m|\033[0m
    \033[31m /|\  \033[33m|\033[0m
    \033[31m / \  \033[33m|\033[0m
    \033[33m      |\033[0m
    \033[33m=========\033[0m
    \033[91m💀 GAME OVER 💀\033[0m
    '''
]

# Victory ASCII art
VICTORY_ART = '''
    🎉 CONGRATULATIONS! 🎉
    
     \\    o    /
      \\   |   /
       \\ /|\\ /
        \\|_|/
         \\ /
          |
         / \\
        /   \\
    
    You saved the hangman! 
    '''

# Defeat ASCII art  
DEFEAT_ART = '''
    💀 GAME OVER 💀
    
    The word was too tricky...
    Better luck next time!
    
       RIP
    +-------+
    | WORDS |
    |  AND  |
    | HOPES |
    +-------+
    '''

# Loading animation frames
LOADING_FRAMES = [
    "🎯 Loading.",
    "🎯 Loading..",
    "🎯 Loading...",
    "🎯 Loading....",
]

# Emoji sets for different moods
HAPPY_EMOJIS = ["😊", "😃", "🎉", "✨", "🌟", "💫", "🎊", "🥳"]
SAD_EMOJIS = ["😢", "😔", "💔", "😞", "😿", "😭", "☹️", "😩"]
THINKING_EMOJIS = ["🤔", "💭", "🧠", "💡", "❓", "🤷", "🎯", "🔍"]

def get_random_emoji(mood="happy"):
    """
    Get a random emoji based on mood.
    
    Args:
        mood (str): 'happy', 'sad', or 'thinking'
    
    Returns:
        str: A random emoji
    """
    import random
    
    emoji_map = {
        'happy': HAPPY_EMOJIS,
        'sad': SAD_EMOJIS,
        'thinking': THINKING_EMOJIS
    }
    
    return random.choice(emoji_map.get(mood.lower(), HAPPY_EMOJIS))

def print_loading_animation(duration=2):
    """
    Print a loading animation.
    
    Args:
        duration (int): Duration in seconds
    """
    import time
    import sys
    
    frames = LOADING_FRAMES
    frame_duration = duration / (len(frames) * 3)  # Repeat 3 times
    
    for _ in range(3):
        for frame in frames:
            sys.stdout.write(f"\r{frame}")
            sys.stdout.flush()
            time.sleep(frame_duration)
    
    sys.stdout.write("\r" + " " * 20 + "\r")  # Clear the line
    sys.stdout.flush()

# Color codes for terminal output
class Colors:
    """ANSI color codes for terminal output."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colored_text(text, color):
    """
    Return colored text for terminal output.
    
    Args:
        text (str): Text to color
        color (str): Color name from Colors class
    
    Returns:
        str: Colored text
    """
    color_code = getattr(Colors, color.upper(), Colors.ENDC)
    return f"{color_code}{text}{Colors.ENDC}"