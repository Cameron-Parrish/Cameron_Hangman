#Super early version 3
#Has deviated far from the plan, only now relaising how terrible it is.
import random
import string
import time

def force_number():#This function uses try/except block to only allow the use to enter a number < 0 or > 3
    amount_of_games = 0
    while amount_of_games > 3 or amount_of_games <  1:
        try:
            amount_of_games = int(input("Enter the amount of games to play (max 3)"))#This
        except:
            print("Please enter a valid integer")
        else:
            useless = None
    print("You have chosen {} amount of games".format(amount_of_games))
    return amount_of_games

def force_letter():#This function checks to make sure that only a single letter guess is entered, and that it is a lower case letter
    guess = ("")
    while  str.isalpha(guess) == False or len(guess) > 1:#If the imported guess variable contains no ap=lpha characters or the user input is > 1, keep asking the user for a single letter guess
            guess = input("Please enter a single letter guess")
    return guess


def guess_add(guess,blanks):#An improvement over my last iteration of adding the guessed character to the blanks. this doesn't add an entire new element therefore no need for deleting the last element in the blanks list which causes havoc.
    index = secret_word.index(guess)#Still cant deal with words with multiple letters and spaces
    blanks[index] = guess
    return blanks


for i in range(force_number()):#Call function force_number to ask user how many games they want, use a for in range loop to run the game that many times
    guessed_list = []
    word_list = ["pie"]
    random.shuffle(word_list)
    secret_word = word_list[0]
    secret_word = list(secret_word)
    blanks = len(secret_word) * ("_")
    blanks = list(blanks)
    lives = 10
    repeat_guess = True
    guess = ("")#This triggers the force_letter function to ask the user to enter a letter, this is because an empty string variable contains no alpha characters
    print(secret_word)

    while repeat_guess == True:#This loop checks the user input to make sure that it is a letter present in the word. This means that the guess_add function does'nt need to check if the letter is in the word and instead add the letter to blanks list
        guess = force_letter()
        if guess in guessed_list:
            print("You have already guessed that")
        elif guess in secret_word:
            blanks = guess_add(guess, blanks)#Imports the guess and blanks variables(both global) into the guess_add function so that the guess variable can be inserted into blanks
            guessed_list.append(guess)
            print("You have chosen wisely")
            print(blanks)
        elif guess not in secret_word:
           lives -= 1
           print("Oh,  so unwise")
           time.sleep(5)
           print("You have {} lives less child".format(lives))
        if blanks == secret_word:
                 print("curses...")
                 time.sleep(5)
                 print("You cracked the code")
        if  lives <= 0:
                 print("I'm afraid that the shield generator is still operational...")

    
    




    



    


    

    



    



        
        
        

    
        

                                  
    
