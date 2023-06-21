MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def update_resources(drink,existing_resources):
    resources["water"] = resources["water"] - MENU[drink]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        resources["milk"] = resources["milk"] - MENU[drink]["ingredients"]["milk"]

def payment(drink,existing_resources):
    global money
    print("Please make your payment")
    quarter = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickel = int(input("How many nickels?"))
    penny = int(input("How many pennies?"))
    amount_received = (0.25 * quarter) + (0.1 * dimes) + (0.05 * nickel) + (0.01 * penny)
    drink_cost = MENU[drink]["cost"]

    if amount_received > drink_cost:
        change = round(amount_received - drink_cost,2)
        print(f"Here is your drink and balance change ${change}")
        money += drink_cost
        update_resources(drink,existing_resources)
    elif amount_received == drink_cost:
        print(f"Here is your drink, have a nice day!")
        money += drink_cost
        update_resources(drink,existing_resources)
    else:
        print("Sorry, that's not enough money. Money refunded.")


def check_resource(drink_name, existing_resource,money):
    required_resource = MENU[drink_name]["ingredients"]
    if existing_resource["water"] >= required_resource["water"]:
        if existing_resource["coffee"] >= required_resource["coffee"]:
            if drink_name=="espresso" or existing_resource["milk"] >= required_resource["milk"] :
                print("We have enough resources, proceed to payment.")
                payment(drink_name,existing_resource)
            else:
                print("Sorry, we do not have enough milk.")
        else:
            print("Sorry, we do not have enough coffee.")
    else:
        print("Sorry, we do not have enough water.")


def format_report(resource, cash):
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    return f"Remaining Resources\nWater : {water}ml\nMilk :{milk}ml\nCoffee : {coffee}g\nMoney : ${cash}"


turn_off = False
money = 0
while not turn_off:
    drink = input("What would you like? (espresso/latte/cappuccino):").lower()
    if drink == 'report':
        print(format_report(resources, money))
    elif drink == 'espresso':
        check_resource(drink, resources,money)
    elif drink == 'latte':
        check_resource(drink, resources,money)
    elif drink == 'cappuccino':
        check_resource(drink, resources,money)
    elif drink == 'off':
        turn_off = True
    else:
        print("Invalid Input")
