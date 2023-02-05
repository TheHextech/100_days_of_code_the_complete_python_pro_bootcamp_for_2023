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
            "water": 0,
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
    "water": 250,
    "milk": 250,
    "coffee": 100,
}


def resources_are_sufficient(drink_resources):
    """Return True if there are sufficient resources or False if resources are insufficient. Eventually,
     in the last case it's printed the missing resource."""
    for item in drink_resources:
        if resources[item] < drink_resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def process_coin():
    """Ask user to insert different types of money and return the total as an integer."""
    print("Please, insert your coin here.")
    total = int(input("How much quarter? ")) * 0.25
    total += int(input("How much dimes? ")) * 0.10
    total += int(input("How much nickles? ")) * 0.05
    total += int(input("How much pennies? ")) * 0.01
    return total


def transaction_successful(money_inserted):
    """Returns True if the payment is accepted and eventually calculates the change. Return False if the transaction is
     rejected and shows how much money are missing."""
    if money_inserted < drink["cost"]:
        difference = round(drink["cost"] - money_inserted, 2)
        print(f"Not enough money insert. You have to introduce ${difference} more. Money refund.")
        return False
    else:
        change = round(money_inserted - drink["cost"], 2)
        if change > 0:
            print(f"Here is your change: ${change}.")
        return True


def make_coffee(drink_name, drink_ingredients):
    """Deducts necessary ingredients and subtract them form the resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "return":
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}g")
    else:
        drink = MENU[choice]
        print(f"Your drink cost is: ${drink['cost']}.")
        if resources_are_sufficient(drink["ingredients"]):
            print("Sufficient resources.")
            payment = process_coin()
            if transaction_successful(payment):
                print("Transaction went good.")
                make_coffee(choice, drink["ingredients"])
