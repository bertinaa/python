import random
from hangman_words import word_list
from hangman_art import stages, logo
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
#word_list = ["aardvark", "baboon", "camel"]
#we will be using the word_list from the module hangman_words
chosen_word = random.choice(word_list)

lives = 6
#printing logo
print(logo)
end_of_game = False
print(f'Pssst, the solution is {chosen_word}.')
display = []
for char in chosen_word:
  display.append('_')

while not end_of_game :
  guess = input("Guess a letter: ").lower()
  #to display a message when user guesses the same letter again
  if guess in display:
      print(f"You've already guessed {guess}, please try a different letter :3")
  for i in range(len(chosen_word)):
      if chosen_word[i] == guess:
          display[i]=guess
  #line 74's if statement is not an elif of line 71 because then it will iterate  thro the entire word and then do lives--      
  if guess not in chosen_word:
    print("{guess} is not in the word.")
    lives -= 1
    if lives==0:
      print("You Lose.")
      print(f"The word was {chosen_word}")
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  if '_' not in display:
    print("You win.")
    end_of_game = True
    
  print(stages[lives])
