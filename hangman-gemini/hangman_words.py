import random

# A dictionary to hold categories of words.
# This makes it easy to add new themes to the game.
WORD_CATEGORIES = {
    'animals': [
        'antelope', 'baboon', 'badger', 'barracuda', 'chimpanzee', 'cobra',
        'cormorant', 'coyote', 'crocodile', 'dolphin', 'donkey', 'elephant',
        'ferret', 'gazelle', 'gorilla', 'jaguar', 'lemur', 'lizard',
        'mongoose', 'opossum', 'python', 'salamander', 'scorpion', 'squirrel',
        'vulture', 'walrus', 'wombat', 'zebra'
    ],
    'fruits': [
        'apple', 'apricot', 'avocado', 'banana', 'blackberry', 'blueberry',
        'cantaloupe', 'cherry', 'coconut', 'cranberry', 'grapefruit',
        'guava', 'kiwi', 'lemon', 'lime', 'mango', 'nectarine', 'orange',
        'papaya', 'passionfruit', 'peach', 'pear', 'pineapple', 'plum',
        'pomegranate', 'raspberry', 'strawberry', 'tangerine', 'watermelon'
    ],
    'countries': [
        'argentina', 'australia', 'brazil', 'canada', 'denmark', 'egypt',
        'finland', 'germany', 'hungary', 'ireland', 'japan', 'kenya',
        'madagascar', 'mexico', 'netherlands', 'norway', 'philippines',
        'portugal', 'romania', 'singapore', 'sweden', 'switzerland',
        'thailand', 'turkey', 'ukraine', 'vietnam', 'zimbabwe'
    ],
    'programming': [
        'algorithm', 'binary', 'boolean', 'compiler', 'database', 'debug',
        'function', 'variable', 'javascript', 'python', 'integer', 'loop',
        'object', 'recursion', 'software', 'syntax', 'framework', 'library'
    ]
}

def get_random_word():
    """Selects a random category and then a random word from that category."""
    # Choose a random category from the dictionary keys
    random_category_key = random.choice(list(WORD_CATEGORIES.keys()))
    
    # Choose a random word from the list associated with that category
    random_word = random.choice(WORD_CATEGORIES[random_category_key])
    
    # Return both the word and its category
    return random_word, random_category_key
