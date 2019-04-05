#RockPaperScissors.py

import sys
import time
import random

def main():

    #set variables
    playagain = True

    #get the player's name
    print("Hello!  Welcome to rock paper scissors.")
    playername = input("What is your name?\n").capitalize()
    print("Nice to meet you " + playername)

    while playagain:
        input("Press enter to start...")
        print("1...")
        time.sleep(1.0)
        print("2...")
        time.sleep(1.0)
        print("3...")
        time.sleep(1.0)
        print("Shoot...")
        print("I threw " + get_throw())
        win = input("Did I win? Y/N\n").upper()

        if win == "Y":
            print("Hooray!!")
        else:
            print("Aww man! I'll get you next time!")
        
        again = input("Would you like to play again? Y/N\n").upper()

        if again == "N":
            playagain = False

    print("Thanks for playing, " + playername + "!")

    return 0

def get_throw():
    throw = random.randint(0, 2)
    if throw == 0:
        return "Rock"
    elif throw == 1:
        return "Paper"
    else:
        return "Scissors"


if __name__ == "__main__":
    main()