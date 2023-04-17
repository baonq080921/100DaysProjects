import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock,paper,scissors]
man_player=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
bot_player=random.randint(0,2)
print(list[man_player])
print(f"Computer choose is {bot_player}")
new_list=list[bot_player]
print(new_list)
if man_player > bot_player:
    print('You won the game!!!')
elif man_player==bot_player:
    print("You have yourself an draw!!!")
elif man_player < 0 or man_player >3:
    print('Invalid value .Please play properly!!!')
else:
    print("You lose loser!!!")

          

