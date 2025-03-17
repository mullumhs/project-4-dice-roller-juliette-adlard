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
                print("Your integer must be positive.")
        except:
            print("Enter a valid integer.")
   
sides = get_info("How many sides should your dice have? ")
rolls = get_info(f"How many {sides} sided dice should be rolled? ")
num = 1
total = 0


while num <= rolls:
    roll = random.randint(1, sides)
    print(f"Roll {num} is: {roll}")
    num = num + 1
    total = total + roll

print(f"Total: {total}")


    