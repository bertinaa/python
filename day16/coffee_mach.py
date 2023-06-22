#my code
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turn_on = True

while turn_on:
    drink = input(f"What would you like to drink ({menu.get_items()})? ")
    if drink == 'off':
        turn_on = False
    elif drink == 'report':
        print(coffee_maker.report())
        print(money_machine.report())
    elif menu.find_drink(drink):
        drink_loca = menu.find_drink(drink)
        drink_cost = menu.find_drink(drink).cost
        if coffee_maker.is_resource_sufficient(drink_loca):
            if money_machine.make_payment(drink_cost):
                coffee_maker.make_coffee(drink_loca)
    else:
         print("Invalid Input.")


