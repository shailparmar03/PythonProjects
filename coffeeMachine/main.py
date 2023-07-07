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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 4.Check resources sufficient?
def is_resource_sufficient(order_ingredients):
    """RETURNS True if ingredients are sufficient, otherwise returns False"""
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


# TODO 5. Process coins.
def process_coins():
    """RETURNS the total calculated from coins inserted"""
    print("Please insert coins: ")
    total=int(input("How many quarters? "))*0.25
    total += int(input("How many dimes? "))*0.1
    total += int(input("How many nickles? "))*0.05
    total += int(input("How many pennies? "))*0.01
    return total


def is_transaction_successful(user_payment, drink_cost):
    """RETURNS True if user has entered sufficient amount of money, otherwise RETURNS False"""
    if user_payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += drink_cost
        change=round(user_payment-drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        return True

def update_resources(ingredients):
    for _item in ingredients:
        resources[_item]-=ingredients[_item]


is_on = True
while is_on:
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    # TODO 2.Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        is_on = False

    # TODO 3. Print report
    elif user_choice == "report":
        for item in resources:
            print(f"{item} : {resources[item]}", end='')
            if item == 'coffee':
                print("g")
            else:
                print("ml")
        print(f"Money : ${profit}")
    else:
        drink = MENU[user_choice]
        print(drink)
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            # TODO 6.Check transaction successful?
            if is_transaction_successful(payment, drink['cost']):
                update_resources(drink['ingredients'])
                # TODO 7. Make Coffee
                print(f"Here is your {user_choice}. Enjoy!")








