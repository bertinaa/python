

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess =input("Guess a letter").lower()
for char in chosen_word:
    if char == guess:
      print(True)
    else:  
      print(False)
