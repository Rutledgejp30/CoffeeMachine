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
    "money": 0
}


def print_report():
    """Print the available resources in the coffee maker"""
    for resource in resources:
        if resource == "money":
            print(f"{resource}: ${resources[resource]:.2f}")
        else:
            print(f"{resource}: {resources[resource]}")


def validate_drink_choice(drink):
    """Returns True if the user's choice is a valid option in the MENU"""
    if drink in MENU:
        return True
    else:
        return False


def check_resources(drink):
    """Returns a string if there is not enough of a particular resource and returns None if resources are sufficient"""
    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]

    water_needed = MENU[drink]["ingredients"]["water"]
    coffee_needed = MENU[drink]["ingredients"]["coffee"]
    if drink == "espresso":
        milk_needed = 0
    else:
        milk_needed = MENU[drink]["ingredients"]["milk"]

    if water_available - water_needed <= 0:
        return "Sorry, there is not enough water."
    if milk_available - milk_needed <= 0:
        return "Sorry, there is not enough milk."
    if coffee_available - coffee_needed <= 0:
        return "Sorry, there is not enough coffee."


def take_money(drink_cost):
    """ Prints if the user paid enough or not. Returns True if they paid enough, False if they did not"""
    successful_transaction = True

    print(f"That'll be ${drink_cost:.2f}, please.")
    total_paid = 0
    total_paid += float(input("How many quarters do you want to insert?: ")) * 0.25
    total_paid += float(input("How many dimes do you want to insert?: ")) * 0.10
    total_paid += float(input("How many nickles do you want to insert?: ")) * 0.05
    total_paid += float(input("How many pennies do you want to insert?: ")) * 0.01

    refund_amount = total_paid - drink_cost

    if refund_amount > 0:
        resources["money"] += drink_cost
        print(f"Here is ${refund_amount:.2f} in change.")
        return successful_transaction
    elif refund_amount == 0:
        resources["money"] += drink_cost
        print("You inserted exact change.")
        return successful_transaction
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return not successful_transaction


def make_drink(drink):
    """Deducts ingredients required for drink from available resources"""
    for ingredient in resources:
        if ingredient in MENU[drink]["ingredients"]:
            resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

    return f"Here is your {drink}!"


keep_going = True
is_machine_on = True

while keep_going:
    # TODO: 1. Print a report of all the coffee machine resources
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink_choice == "report":
        print_report()
    elif drink_choice == "off":
        is_machine_on = False
        keep_going = False
        print("Powering machine down...")
    else:
        if drink_choice in MENU:
            resource_check = check_resources(drink_choice)

            if resource_check is None:
                if take_money(MENU[drink_choice]["cost"]):
                    print(make_drink(drink_choice))
            else:
                print(resource_check)
        else:
            print("Invalid drink choice.")

    if is_machine_on:
        another_drink = input("Would you like another drink? Type 'y' or 'n': ").lower()

        if another_drink != 'y' and another_drink != 'n':
            print("Invalid input. Exiting.")
            keep_going = False
        if another_drink == "n":
            keep_going = False

# # TODO: 2. Check if the resources are sufficient
# # TODO: 3. Process coins
# # TODO: 4. Check if transaction is successful
# # TODO: 5. Make the drink

