MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "water": 500,
    "milk": 200,
    "coffee": 100,
}
order = ""
money_inserted = 0
stop = False

def take_order():
    global order
    global money_inserted
    order = input("what would you like to order? an espresso , latte or a cappuccino ? ")
    if order not in MENU:
        print("Sorry , that's an invalid order")
        return False
    elif resources["water"] < MENU[order]["ingredients"]["water"] or resources["coffee"] < MENU[order]["ingredients"]["coffee"] or resources["milk"] < MENU[order]["ingredients"]["milk"]:
        print("Sorry , the machine ran out of ingredients ")
        return False
    pennies = int(input("Insert pennies"))
    nickels = int(input("Insert nickels"))
    dimes = int(input("insert dimes"))
    quarters = int(input("insert quarters"))
    money_inserted = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25)
    print(f"you have inserted {money_inserted} $ ")
    return True
def make_order(order):
    global money_inserted
    global resources
    drink = MENU[order]
    cost = drink["cost"]
    ingredients = drink["ingredients"]
    if money_inserted >= cost:
        remainder = money_inserted - cost
        resources["water"] -= ingredients["water"]
        resources["coffee"] -= ingredients["coffee"]
        resources["milk"] -= ingredients["milk"]
        print(f"Here's your order and your change is {remainder} $ ")
        money_inserted = 0
    else:
        print("Sorry , you don't have enough money , here's your money back")
while not stop:
    first_command = input("Type 'yes' to order, 'info' for resources, 'stop' to exit: ").lower()

    if first_command == "info":
        print(resources)
    elif first_command == "stop":
        stop = True
        print("Machine stopped")
    elif first_command == "yes":
        can_make = take_order()
        if can_make:
            make_order(order)
    else:
        print("Invalid command")