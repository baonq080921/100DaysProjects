from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# drink=MenuItem()

# report_inf1=CoffeeMaker()
# report_inf2=CoffeeMaker()
# report_inf3=CoffeeMaker()
# user_drink=Menu()
# continue_buying=True
# while continue_buying:
#     user_order=input(f" What would you like {user_drink.get_items()} ? ").lower()
    
#     if user_order == "off":
#         continue_buying=False
#     elif user_order =="report":
#         report_inf1.report()
#     else:
#         name_drink=user_drink.find_drink(user_order)
#         report_inf2.make_coffee(name_drink)
#         report_inf3.is_resource_sufficient(name_drink)

money_machine= MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
is_on=True
while is_on:
    choices=input(f"What would you like ? {menu.get_items()}")
    if choices == "off":
        is_on=False
    elif choices== "report":
        coffee_maker.report()
        money_machine.report()
    else:
        list_drink=menu.find_drink(choices)
        if coffee_maker.is_resource_sufficient(list_drink):  
            if money_machine.make_payment(list_drink.cost):
                coffee_maker.make_coffee(list_drink)
        else:
            is_on=False
            
        
    


