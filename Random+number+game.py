#Ethan/Jessica
#11/2/18

import random
#Menu
def menu():
    x=True
    while x == True:
        print("Welcome to Random Numbers")
        print("Start Game")
        print("Coin Toss Game")
        print("Credits")
        print("Quit")
        user_input = input("what do you want to do, start, coin toss, credits, quit")
        if "start" in user_input:
                number_game()
        elif "coin toss" in user_input:
                coin_toss()
        elif "credits" in user_input:
            credits()
        elif "quit" in user_input:
                print("thank you for playing")
                x=False
        else:
                menu()
                        
#Random Numbers Game
def number_game():
    guesses = 0
    random_number = random.randrange (1,100) 
    player_guess=10000
    while player_guess != random_number and guesses != 5:
        player_guess = int(input("Guess a number from 1 to 100"))
        if player_guess == random_number:
            break
        if player_guess < random_number:
            print("higher")
            guesses +=1
        else:
            print("lower")
            guesses +=1
    if player_guess == random_number:
        print("you win")
        credits()
    else:
        print("you lost")
        print("the number was",random_number)
        credits()




#Coin Toss Game

def coin_toss():
    heads_tails = random.randrange (1,2)
    player_choice = int(input("Heads(1) or Tails(2)!input 1, or 2"))
    if player_choice == heads_tails:
        print("congrats you got it right")
    else:
        print("wrong, better luck next time")

#credits
def credits():
     print("thank you for playing\nCredits to\nEthan Craner\nJessica Weinburger")
     input("press enter to return to menu")
    

menu()
