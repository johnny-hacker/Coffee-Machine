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
# empty money box
profit = 0

# resource dictionary
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# this function checks if the machine has enough resources to make the drink
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        # check if order for item is possible
        # if orders needed ingredients are more than the machines available
        # ingredients 
        if order_ingredients[item] > resources[item]:
            # if they are not enough ingredients
            print(f"​Sorry there is not enough {item}.")
            # return false 
            return False
    # if all ingredients needed are present, return true
    return True


# this function will take payment from the customer
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25 # quarters
    total += int(input("how many dimes?: ")) * 0.1 # dimes
    total += int(input("how many nickles?: ")) * 0.05 # nickles
    total += int(input("how many pennies?: ")) * 0.01 # pennies
    # return total 
    return total

# this function executes transactions, determines whether
# payment recieved is enough and gives back change
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        # figure out how much change you owe the customer
        change = round(money_received - drink_cost, 2) # round function to given precision in decimal digits.
        # give them change back
        print(f"Here is ${change} in change.")
        # import profit from global variable
        global profit
        # profit will equal profit + drink_cost
        # simply adding the cost of the drink to the total
        profit += drink_cost
        # return true
        return True
    # else payment is insuffecient
    else:
        print("Sorry that's not enough money. Money refunded.")
        # return false
        return False

# this function makes the coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    # for each item in order ingredients
    for item in order_ingredients:
        # subtract the ingredient used by drink from ingredrients in machine
        resources[item] -= order_ingredients[item]
    # give them their drink
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
# while the customer still wants to order
while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    # give a report to the user
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice] # retrieve drink info from menu
        # if there are enough resources to make the drink
        if is_resource_sufficient(drink["ingredients"]):
            # proceed to payment
            payment = process_coins()
            # if the transaction is succesful
            if is_transaction_successful(payment, drink["cost"]):
                # funally, make the drink
                make_coffee(choice, drink["ingredients"])

