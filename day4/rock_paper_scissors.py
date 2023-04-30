import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choose = int(input("Enter '0' for Rock, '1' for Paper and '2' for Scissors."))

rps = [rock,paper,scissors]
print(f"You chose {choose} \n {rps[choose]}")
comp = random.randint(0,2)
print(f"Computer chose {comp} \n {rps[comp]}")
if choose==comp:
  print("It's a draw")
elif choose==0:
  if comp==1:
    print("Paper beats rock. You lose.")
  else:
    print("Rock beats scissors. You win!")
elif choose==1:
  if comp == 0:
    print("Paper beats rock. You win!")
  else:
    print("Scissor beats paper. You lose.")
elif choose==2:
  if comp==0:
    print("Rock beats paper. You lose")
  else:
    print("Scissor beats paper. You win!")
else:
    print("You've typed an invalid number. Please enter within the range 0-2.")
