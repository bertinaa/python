import random
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
      #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  print(display)
  if '_' not in display:
    end_of_game = True
