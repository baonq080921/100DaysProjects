import random
from art import logo

#Deal_card function
def deal_card():
    """"Return a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card=random.choice(cards)
    return random_card

#Calculate function
def calculate_score(cards):
    """Take a list of cards and return the score calculate from the card """
    sum
    if  sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Compare function:
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw !!!"
    elif computer_score ==0 :
        return "Lose, opponent has a Blackjack"
    elif user_score ==0:
        return "Win with a Blackjack"
    elif user_score >21:
        return 'You went over.You Lose'
    elif computer_score >21:
        return "Opponent went over.You win "
    elif user_score >computer_score:
        return "You win"
    else:
        return "You lose"
    
    
#Main game!!!
def game():
    
    print(logo)
    
    user_cards=[]
    computer_cards=[]
    is_game_over=False


    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"User card is {user_cards}, current score is {user_score}")
        print(f"Computer  first card is {computer_cards[0]}")

        if user_score ==0 or computer_score ==0 or user_score >21:
            is_game_over=True
        else:
            user_should_deal=input("Do you want another card , type 'y' to pass:").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
        
        
    print(f" Your final hand is {user_cards}, final score:{user_score}")
    print(f" Computer final hand is:{computer_cards}, final score :{computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':")== "y":
    game()







