
#mycode None error
# I'm getting this error > not supported between instances of NoneType and int
from replit import clear
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card(input_cards):
  a = random.choice(cards)
  input_cards.append(a)

def computer_calc(computer_cards):
  score = sum(computer_cards)
  if score <17:
    deal_card(computer_cards)
    computer_calc(computer_cards)
  elif score == 21:
    return 0
  elif score>21:
    return 1
  else:
    return score

def calculate_score(user_cards):
  score = sum(user_cards)
  print(f"Your score is {score}")
  if score==21:
    return 0 
  elif score>21:
    if 11 in user_cards:
      user_cards.remove(11)
      user_cards.append(1)
      calculate_score(user_cards)
    else:
      return 1
  else:
    if input("Would you like to draw another card 'y' or 'n'").lower() == 'y':
      deal_card(user_cards)
      show_cards(user_cards)
      calculate_score(user_cards)

    else:
      return score
    
def show_cards(cards):
  print(cards)
  
def end_result(user_score, computer_score):
  print(f"Your score is {user_score}")
  print(f"Dealers score is {computer_score}")
  if user_score==computer_score:
    print("It's a tie!")
  elif user_score == 0:
    print("You won! Great job!")
  elif user_score ==1:
    print("Oops, you went over 21. Game over.")
  elif computer_score == 0:
    print("Dealer won!")
  elif computer_score ==1:
    print("The dealer went over 21. You win!")
  elif user_score>computer_score:
    print("You won!")
  else:
    print("Oops, you've lost.")
def blackjack():
  clear()
  print(logo)
  user_cards = []
  computer_cards = []
  deal_card(user_cards)
  deal_card(user_cards)
  deal_card(computer_cards)
  
  print("Your cards are ")
  show_cards(user_cards)
  print(f"Dealers cards are {computer_cards}")
  
  deal_card(computer_cards)
  user_score = calculate_score(user_cards)
  
  computer_score = computer_calc(computer_cards)
  print(end_result(user_score,computer_score))
  game()
  
  
def game():
  if input("Would you like a game of bj 'y' or 'n': ").lower()=='y':
    blackjack()
  else:
    print("Okay, bye.")
game()
 
