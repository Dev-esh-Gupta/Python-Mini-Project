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
    "water": 1000,
    "milk": 400,
    "coffee": 200,
}

money = 0


def check_availability(choice):
    ''' This function check the available resource and tell user that coffee is possible or not'''
    for item in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][item] > resources[item] :
            print(f"Sorry, Insufficient {item}")
            return False
    return True


def report_print():
    ''' This Function print the report of Available resources '''
    print("Water : " + str(resources["water"]) + "g")
    print("Milk : " + str(resources["milk"]) + "g")
    print("Coffee : " + str(resources["coffee"]) + "g")
    print("Money : $" + str(money))


def ask_coins(choice):
    '''
    This function Ask the user for coin to be inserted
    '''
    print("Please insert coins.")
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.10
    total += float(input("How many nickels?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    cost = MENU[choice]["cost"]
    global money
    if total >= cost:
        money += cost
        change = round(total - cost,2)
        print("Here is $" + str(change) + " in change.")
        return True
    else:
        print("Sorry, Insufficient Payment, Money Refunded!")
        return False


def make_coffee(choice):
    is_success = False
    if choice == "report":
        report_print()
    elif choice == "espresso":
        if check_availability(choice):
            is_success = ask_coins(choice)
    elif choice == "latte":
        if check_availability(choice):
            is_success = ask_coins(choice)
    else:
        if check_availability(choice):
            is_success = ask_coins(choice)
    return is_success


def update_resource(choice):
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]


machine_on = True


while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'exit':
        machine_on = False
    elif make_coffee(user_choice):
        update_resource(user_choice)
        print("Here is your " + user_choice + " ☕ Enjoy!")
