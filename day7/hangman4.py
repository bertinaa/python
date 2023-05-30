import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = 6
end_of_game = False
print(f'Pssst, the solution is {chosen_word}.')
display = []
for char in chosen_word:
  display.append('_')

while not end_of_game :
  guess = input("Guess a letter: ").lower()
  for i in range(len(chosen_word)):
      if chosen_word[i] == guess:
          display[i]=guess
  #line 74's if statement is not an elif of line 71 because then it will iterate  thro the entire word and then do lives--      
  if guess not in chosen_word:
    lives -= 1
    if lives==0:
      print("You Lose.")
      print(f"The word was {chosen_word}")
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  if '_' not in display:
    end_of_game = True
  print(stages[lives])
