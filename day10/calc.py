from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  should_continue = True
 
  while should_continue:
    num2 = float(input("What's the next number?: "))
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation: ")
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    user_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: or 'e' to exit the program. ")
    if user_input == 'y':
      num1 = answer
    elif user_input=='n':
      should_continue = False
      clear()
      calculator() #recursive function
    else:
      print( "Goodbye!")

calculator()
