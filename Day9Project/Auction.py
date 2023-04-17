from art import logo
print(logo)
print("Welcome to the bid show ")
end_of_bid =False
dict={}
#function find the highest bid
def find_highest_binder(bidding_record):
    winner=""
    max =0
    for name in bidding_record:
        if max < bidding_record[name]:
            max=bidding_record[name]
            winner=name
    print(f"The winner is {winner} with the bid of ${max}")        
    
    
while not end_of_bid:
    names=input("What is your name ?\n ")
    bid_prices=int(input("How much do you want to bid?\n$ "))
    ask=input("If there any body want to bid 'Y' of 'N' \n").lower()
    dict[names]=bid_prices
    if ask == "y":
        end_of_bid = False
    else:
        end_of_bid=True
        find_highest_binder(bidding_record=dict)
        
        
