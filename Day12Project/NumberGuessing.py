from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def set_difficulty():
    level=input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        
def check_answer(guess, answer, turns):
    if guess > answer:
        print('Too high!!')
        return turns-1
    elif guess < answer:
        print("Too Low !!!")
        return turns -1
    else:
        print(f"You got it. The answer was {answer}")
def game():
    print("Welcome to the guessing game!")
    print("I'm thinking a number between 1 and 100.")
    answer= randint(1,100)
    print(f"Psst, the answer is {answer}")
    
    turns=set_difficulty()
    #Repeat the guessing functionality if they get it wrong
    guess=0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")
        
        #LEt the user choose a number:
        guess=int(input("Make a guess: "))
        
        turns= check_answer(guess, answer, turns)
        if turns ==0:
            print("You run out of  guesses, you lose")
            return
        elif guess != answer:
            print("Guess again")
    

game()

