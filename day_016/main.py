from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino):​ ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        maker.report()
    else: 
        drink = menu.find_drink(choice) 
        if  drink != None:
            if money_machine.make_payment(drink.cost):
                maker.make_coffee(drink)
            
             
    