#Print the art
from art import logo, vs
import random
from data import data

#Format the account into printable format:
def format_account(account):
    """Format the account into printable format"""
    account_name=account['name']
    account_description=account['description']
    account_country= account['country']
    return f"{account_name},a {account_description}, from {account_country}"   

#Check the user answer
def check_answer(guess, a_follower, b_follower):
    """Check the answer of user """
    if a_follower > b_follower:
        return guess=="a"
    else:
        return guess =="b"
game_continue=True
b_random=random.choice(data)
score =0
#Repeat the game :
while game_continue:
#Random a name ,  description, country 
    a_random=b_random
    if a_random == b_random:
        b_random=random.choice(data)
    #Print the art logo ,vs 
    print(logo)
    print(f"Compare A: {format_account(a_random)}")
    print(vs)
    print(f"Compare B: {format_account(b_random)}")
    guess=input("Choose 'A'or 'B'").lower()
    a_followers= a_random['follower_count']
    b_followers= b_random['follower_count']
    

    #Check if the user answer it correct:
    is_correct= check_answer(guess,a_followers,b_followers)
    if is_correct:
        score+=1
        
        print(f"You right. Your current score is {score}")
    else:
        print(f"You lose.Your final score is {score}")
        game_continue=False
        