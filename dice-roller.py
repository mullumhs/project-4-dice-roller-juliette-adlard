"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random

def get_info(msg):
    while True:
        try:
            n = int(input(msg))
            if n > 0:
                return n
            else:
                print("You must enter a positive integer.")
        except:
            print("Enter a valid integer.")

def roll_dice(sides, rolls):
    #roll the freaking dice
    

sides = get_info("How many sides should your dice have? ")
rolls = get_info(f"How many {sides} sided dice should be rolled? ")
roll_dice(sides, rolls)




    