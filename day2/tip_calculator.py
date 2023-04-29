#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = int(input("What's the total bill to be paid?"))
people = int(input("How many people are present?"))
tip = bill * .12
bill += tip
amount_to_be_paid = bill/people

print(f"Each person has to pay {amount_to_be_paid:.2f}")
