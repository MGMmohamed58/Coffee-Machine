from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
is_on = True
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    print(f"Hello , we offer : {menu.get_items()}")
    order = input("What would you like to order ?  ")

    if order == "info":
        coffee_machine.report()
        money_machine.report()
    elif order == "off":
        is_on = False
    else:

        drink = menu.find_drink(order)
        if drink is None:
            print("")
        else:
            if (coffee_machine.is_resource_sufficient(drink)):
                print(f"Your drink costs {drink.cost}$ \n")
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
