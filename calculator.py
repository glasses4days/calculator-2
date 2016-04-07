"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmeticOperations import *


# Your code goes here
    
# While loop
while True:
    try: 
        """Checks if [1] [2] are integers"""
        input = raw_input().lower()
        tokens = input.split(" ")
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        if tokens[0] == "q":
            """ if [0] is q, then it will quit the loop"""
            break
        else:
            if tokens[0] == "+":
                """Checks if [0] is +, then it calls add function"""
                print add(num1, num2)
            elif tokens[0] == "-":
                """Checks if [0] is -, then it calls subtract function"""
                print subtract(num1, num2)
            elif tokens[0] == "*":
                """Checks if [0] is *, then it calls multiply function"""
                print multiply(num1, num2)
            elif tokens[0] == "/":
                """Checks if [0] is /, then it calls divide function"""
                print divide(num1, num2)
            elif tokens[0] == "square":
                """Checks if [0] is square, then it calls square function"""
                print square(num1)
            elif tokens[0] == "cube":
                """Checks if [0] is cube, then it calls cube function"""
                print cube(num1)
            elif tokens[0] == "pow":
                """Checks if [0] is pow, then it calls pow function"""
                print power(num1, num2)
            elif tokens[0] == "mod":
                """Checks if [0] is mod, then it calls mod function"""
                print mod(num1, num2)
    except ValueError: 
        print "Oops! Your input is invalid. Please enter accurate operations."

