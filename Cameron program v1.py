#Super early version 1
#Has deviated far from the plan, only now relaising how terrible it is.

import random
import string

def force_number():
    amount_of_games = 0
    while amount_of_games > 3 or amount_of_games <  1:
        try:
            amount_of_games = int(input("Enter the amount of games to play (max 3)"))
        except:
            print("Please enter a valid integer")
        else:
            print()
    print("You have chosen {} amount of games".format(amount_of_games))
    return amount_of_games

def force_letter():
    guess = ("")
    while  str.isalpha(guess) == False or len(guess) > 1:
            guess = input("Please enter a single letter guess")
            print(guess)
    return guess
    

guessed_list = []
word_list = ["campbell", "pie","doom"]
random.shuffle(word_list)
secret_word = word_list[0]
lives = 10
repeat_guess = True
guess = ("")
print(secret_word)

while repeat_guess == True:
    guess = force_letter()
    if guess not in secret_word:
        guessed_list.append(guess)
        lives -= 1
    elif guess in secret_word:
        print("You have chosen wisely")




    



    


    

    



    



        
        
        

    
        

                                  
    
