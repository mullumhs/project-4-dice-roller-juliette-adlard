"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions with parameters in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a function named say_hello that accepts a person's name as a parameter and prints "Hello" followed by the name.
def say_hello(name):
    print(f"Hello {name}.")

# Develop a function named triple that takes one number as a parameter and returns the number multiplied by three.
def triple(x):
    y = x * 3
    return y

# Write a function called add that takes two numbers as parameters and returns their sum. 
def add(x, y):
    sum = x + y
    return sum

# Create a function named draw_line that takes one parameter for the length of the line and prints a straight line of that many hyphens.
def draw_line(length):
    print("-" * length)

# Call your functions, printing out the return result where appropriate
name = input("Enter your name: ").title()
say_hello(name)
x = float(input("Enter a number: "))
y = triple(x)
print(f"Triple your number is {y}.")
x = float(input("Enter a number: "))
y = float(input("Enter a number: "))
sum = add(x, y)
print(f"The sum of your two numbers is {sum}")
length = int(input("Enter a number to determine the length of your line: "))
draw_line(length)