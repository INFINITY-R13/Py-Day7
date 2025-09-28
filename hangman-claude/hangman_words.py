"""
Hangman Words Module
Contains word lists organized by difficulty and category.
"""

# Easy words (4-6 letters, common words)
EASY_WORDS = [
    'apple', 'beach', 'chair', 'dance', 'eagle',
    'flower', 'guitar', 'house', 'island', 'juice',
    'kitchen', 'lemon', 'mouse', 'night', 'ocean',
    'piano', 'queen', 'river', 'smile', 'table',
    'umbrella', 'voice', 'water', 'yellow', 'zebra'
]

# Medium words (6-8 letters, moderate difficulty)
MEDIUM_WORDS = [
    'abruptly', 'adventure', 'bicycle', 'calendar', 'dolphin',
    'elephant', 'festival', 'giraffe', 'harmony', 'internet',
    'jungle', 'keyboard', 'library', 'mountain', 'notebook',
    'october', 'penguin', 'question', 'rainbow', 'sandwich',
    'tornado', 'universe', 'vacation', 'weather', 'xylophone'
]

# Hard words (original challenging words from your list)
HARD_WORDS = [
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward',
    'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou',
    'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm',
    'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom',
    'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness',
    'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl',
    'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip',
    'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable',
    'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove',
    'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy',
    'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph',
    'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard',
    'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy',
    'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy',
    'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging',
    'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo',
    'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk',
    'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths',
    'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz',
    'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub',
    'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize',
    'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz',
    'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling',
    'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes',
    'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw',
    'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz',
    'squawk', 'staff', 'strength', 'strengths', 'stretch',
    'stronghold', 'stymied', 'subway', 'swivel', 'syndrome',
    'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress',
    'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown',
    'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka',
    'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave',
    'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing',
    'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy',
    'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee',
    'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging',
    'zilch', 'zipper', 'zodiac', 'zombie'
]

# Theme-based word lists
ANIMALS = [
    'elephant', 'giraffe', 'penguin', 'dolphin', 'butterfly',
    'kangaroo', 'octopus', 'flamingo', 'cheetah', 'platypus'
]

TECHNOLOGY = [
    'computer', 'internet', 'software', 'keyboard', 'monitor',
    'smartphone', 'bluetooth', 'wifi', 'database', 'algorithm'
]

NATURE = [
    'mountain', 'rainbow', 'thunder', 'waterfall', 'sunshine',
    'blizzard', 'hurricane', 'volcano', 'glacier', 'forest'
]

# Default word list (medium difficulty)
WORD_LIST = MEDIUM_WORDS + HARD_WORDS

def get_words_by_difficulty(difficulty='medium'):
    """
    Get words by difficulty level.
    
    Args:
        difficulty (str): 'easy', 'medium', or 'hard'
    
    Returns:
        list: List of words for the specified difficulty
    """
    difficulty_map = {
        'easy': EASY_WORDS,
        'medium': MEDIUM_WORDS,
        'hard': HARD_WORDS
    }
    
    return difficulty_map.get(difficulty.lower(), MEDIUM_WORDS)

def get_words_by_theme(theme):
    """
    Get words by theme.
    
    Args:
        theme (str): 'animals', 'technology', or 'nature'
    
    Returns:
        list: List of words for the specified theme
    """
    theme_map = {
        'animals': ANIMALS,
        'technology': TECHNOLOGY,
        'nature': NATURE
    }
    
    return theme_map.get(theme.lower(), WORD_LIST)

def get_random_word(difficulty='medium', theme=None):
    """
    Get a random word based on difficulty or theme.
    
    Args:
        difficulty (str): 'easy', 'medium', or 'hard'
        theme (str): 'animals', 'technology', or 'nature'
    
    Returns:
        str: A random word
    """
    import random
    
    if theme:
        word_list = get_words_by_theme(theme)
    else:
        word_list = get_words_by_difficulty(difficulty)
    
    return random.choice(word_list)

# Statistics about word lists
WORD_STATS = {
    'easy_count': len(EASY_WORDS),
    'medium_count': len(MEDIUM_WORDS),
    'hard_count': len(HARD_WORDS),
    'total_count': len(WORD_LIST),
    'theme_counts': {
        'animals': len(ANIMALS),
        'technology': len(TECHNOLOGY),
        'nature': len(NATURE)
    }
}