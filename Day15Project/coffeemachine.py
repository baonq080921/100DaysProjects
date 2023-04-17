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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#4.Check resources sufficient? 
def is_resources_sufficient(order_ingredient):
    """Check the resources sufficient: """
    for item in order_ingredient:
        if order_ingredient[item]> resources[item]:
            print(f" Sorry there is not enough {item}. ")
            return False
    return True
        
#5.Processing coins
def processing_coin():
    """Return the total calculated from coins inserted"""
    print("Please insert the coin:")
    total= int(input("How many quarters?: "))*0.25
    total+=int(input("How many dimes ?: "))*0.1
    total+=int(input("How many nickles?: "))*0.05
    total+=int(input("How many pennies?: "))*0.01
    return total

#6.Check transaction successful:
def is_transaction_successful(money_input,cost):
    """Return True when the payment is accepted ,or False if the money is insufficient """
    if money_input == cost:
        global profit
        profit+=cost
        return True
    elif money_input < cost:
        print("Sorry that's not enough money.Money refunded. ")
        return False
    else:
        change= round(money_input - cost)  
        profit+=cost      
        print(f"Here is ${change} dollars in change.")
        return True

#7.Make the coffee:
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}  ")
    
#1Input the coffee user want espresso/latte/cappuccino
is_on=True
while is_on:
    user_order=input("What do you like ?(espresso/latte/cappuccino)")
    #2 .Turn off the Coffee Machine by entering "off" to te prompt
    if user_order =="off":
        is_on=False
    #3.Print out the report:
    elif user_order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[user_order]
        if is_resources_sufficient(drink["ingredients"]):
            payment=processing_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_order,drink["ingredients"])
        
        

    
