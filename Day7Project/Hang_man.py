import random
from Hangman_art import stages, logo
from Hang_man_words import word_list
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word= random.choice(word_list)
word_length=len(chosen_word)
lives=6
#Testing the code:
print(f"Psst the random word is : {chosen_word}")

#Generate the blank for the chosen word:
display=[]
for i in range(word_length):
    display+="_"
print(display)
#fill the blank
end_of_game=False

while  not end_of_game:
    guess=input("Please guess a letters in the blank space : ").lower()
    
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You already guess this word{guess}")
    #Check guess letter:
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i]=guess
            
    #Check if the user wrong:
    if guess not in chosen_word:
        print(f"The word you choose is wrong:{guess}")
        lives-=1
        print(stages[lives])
        if lives ==0:
            end_of_game= True
                             
    print(display)
    
    if "_"  not in display:
        end_of_game = True
        print("You won a game")
          

  
     

      
        
 

    



        

           

