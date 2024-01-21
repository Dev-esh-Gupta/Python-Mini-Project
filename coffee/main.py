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

def check_resources(user):




def print_report():
    ''' This Function print the report of Available Resources '''
    print(f"Water : {resources["water"]} g")
    print(f"Milk : {resources["milk"]} g")
    print(f"Coffee : {resources["coffee"]} g")
    print(f"Money : {resources["money"]} $")

# TODO: 1. Ask User to What he would like to have

user_req = input("What would you like to have ? (espresso/latte/cappuccino) : ")

# TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt
while user_req != "off":
    if user_req == "report":
        print_report()
# TODO: 3. Print Report that how much resources is left
    else:
        if check_resource(user_req):







# TODO: 4. Check resources are sufficient or not
# TODO: 5. Process the coins
# TODO: 6. Check Transaction successful
# TODO: 7. Make Coffee