import logo from art
import random

def game():
  print(logo)
  ans = random.randint(1,101)
  print("Welcome to guess the number game!\nI'm thinking of a number between 1 to 100.\nChoose your difficulty type 'easy' or 'hard'.")
  diff = input().lower()
  if diff=='easy':
    lives = 10
  else:
    lives = 5
  while lives:
    lives = lives - 1
    guess = int(input("Enter your guess: "))
    if guess==ans:
      print(f"You win! Your guess is correct, the number is {ans}!")
      break
    elif guess<ans:
      print("Oops, that's not right. Your guess is too low.")
      print(f"You have {lives} lives remaining")
    else:
      print("Oops, that's not right. Your guess is too high.")
      print(f"You have {lives} lives remaining")
    
  if lives==0:
    print(f"You lost. The correct answer was {ans}\n Would you like to try again? ")
  again = input("Type 'y' if you would like to play again, else type 'n'").lower()
  if again=='y':
    game()
  print("Good game.") #else statement.
game()
