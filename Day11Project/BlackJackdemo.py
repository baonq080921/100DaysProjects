import random
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_cards=random.choice(cards)
    return random_cards

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_scores, computer_score):
    if user_scores == computer_score:
        return "We have a Draw!!"
    elif computer_score ==0:
        return "Opponent have a BlackJack!!"
    elif user_scores ==0:
        return "User have a Blackjack"
    elif computer_score >21:
        return "Opponent are overload.You win!!"
    elif user_scores >21:
        return "You are overload.You Lose!!"
    elif user_scores >computer_score:
        return "You won!!!"
    else:
        return "You lose!!!"
    
def game_play():
    
    print(logo)
    
    computer_cards=[]
    user_cards=[]
    is_game_over=False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your card is {user_cards}, your score is {user_score}")
        print(f"Opponent first card is {computer_cards[0]}")
        
        if user_score==0 or computer_score ==0 or user_score>21:
            is_game_over=True
        else:
            draw_card=input("Do you want to draw another card.\nPress 'yes'or 'no'").lower()
            if draw_card =="yes":
                user_cards.append(deal_card())
            else:
                is_game_over=True
        
    while computer_score <17 and computer_score !=0:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
        
    print(f"Your card is {user_cards},final point is {user_score}")
    print(f"Opponent card is {computer_cards}, final score is {computer_score}")
    print(compare(user_score,computer_score))

a=input("Do you want to play a game of Blackjack.\nPress 'y'or 'n' to continue ").lower()
while a=="y":
    game_play()
        
    

