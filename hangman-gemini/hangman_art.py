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

# The stages list is now corrected.
# It is in reverse order and has 7 items (indices 0 to 6).
stages = [
# Index 0: 0 lives left
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', 
# Index 1: 1 life left
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
# Index 2: 2 lives left
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
# Index 3: 3 lives left
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
# Index 4: 4 lives left
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
# Index 5: 5 lives left
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
# Index 6: 6 lives left (start of the game)
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
