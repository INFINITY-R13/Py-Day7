# hangman_art.py

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
'''

stages = [
    # Stage 0 - final state: head, torso, both arms, both legs
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''',
    # Stage 1 - head, torso, both arms, one leg
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    # Stage 2 - head, torso, both arms
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    # Stage 3 - head, torso, one arm
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    # Stage 4 - head and torso
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    # Stage 5 - head only
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    # Stage 6 - empty gallows
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]
