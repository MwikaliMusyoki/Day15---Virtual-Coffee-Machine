from multiprocessing.dummy import active_children
from machine_info import resources
from machine_info import MENU
from collections import Counter

profit = 0


def process_total():
    """Calculates and returns the total amount paid by the user"""
    print("Please insert coins")
    total = int(input("How many Quarters? ")) * 0.25
    total += int(input("How many Dimes? ")) * 0.10
    total += int(input("How many Nickels? ")) * 0.05
    total += int(input("How many Pennies? ")) * 0.01
    return total


def check_payment(total, drink_cost):
    """Checks if the user has made a sufficient payment for their order, gives back change and returns True if payment was sufficient"""
    if total >= drink_cost:
        global profit
        profit += drink_cost
        change = round(total - drink_cost, 2)
        print(f"Here is {change} in change")
        return True
    else:
        print("sorry that's not enough money.")
        return False


def check_resources(order_ingredients):
    """Returns True if resources remaining are enough to make the drink ordererd"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there isn't enough {item}")
            return False
        return True


def make_drink(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


order_active = True
while order_active:
    user_order = input("What would you like? ")
    if user_order == "report":
        for key, value in resources.items():
            print(f"{key} : {value}")
    elif user_order == "off":
        order_active = False
    else:
        drink = MENU[user_order]
        drink_cost = drink["cost"]
        if check_resources(drink["ingredients"]):
            payment = process_total()
            if check_payment(payment, drink_cost):
                make_drink(user_order, drink["ingredients"])
