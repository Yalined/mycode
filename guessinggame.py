#!/usr/bin/env python3
"""Number guessing game!"""

import random

def main():
    num= random.randint(6,10)

    while True:
        
       
        try:
 
                guess= int(input("Guess a number between 6 and 10. Quit by pressing 'q'."))
        
                if guess > 11:
                        print("Too high!")

                elif guess < 6:
                        print("Too low!")

                elif guess == q:
                        print('Quitter alert! Exiting...')
                        break

                elif round == 5:
                        print('Chances are over!')
                        break

                else:
                        print("Correct!")
                        break

        except ValueError as err:
            print("Use only numbers or q. Try again")

main()
