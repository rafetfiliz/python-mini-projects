MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}


def ingredient_reducer(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


def money_calculator(q, d, n, p, drink):
    total = 0.25 * q + 0.10 * d + 0.05 * n + 0.01 * p
    change = total - MENU[drink]["cost"]
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        resources["money"] += MENU[drink]["cost"]
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink} ☕. Enjoy!")


def resource_checker(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        insufficient_resource = "water"
        return insufficient_resource
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        insufficient_resource = "milk"
        return insufficient_resource
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        insufficient_resource = "coffee"
        return insufficient_resource
    else:
        insufficient_resource = ""
        return insufficient_resource


machine_on = True
while machine_on:
    user_input = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        resource_check = resource_checker(user_input)
        if resource_check != "":
            print(f"Sorry there is not enough {resource_check}.")
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money_calculator(quarters, dimes, nickles, pennies, user_input)
            ingredient_reducer(user_input)
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif user_input == "off":
        machine_on = False
