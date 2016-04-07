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
        if tokens[0] == "q":
            """ if [0] is q, then it will quit the loop"""
            break
        else:
            if tokens[0] == "+":
                """Checks if [0] is +, then it calls add function"""
                print add(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == "-":
                    """Checks if [0] is -, then it calls subtract function"""
                print subtract(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == "*":
                    """Checks if [0] is *, then it calls multiply function"""
                print multiply(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == "/":
                    """Checks if [0] is /, then it calls divide function"""
                print divide(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == "square":
                    """Checks if [0] is square, then it calls square function"""
                print square(int(tokens[1]))
            elif tokens[0] == "cube":
                    """Checks if [0] is cube, then it calls cube function"""
                print cube(int(tokens[1]))
            elif tokens[0] == "pow":
                    """Checks if [0] is pow, then it calls pow function"""
                print power(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == "mod":
                    """Checks if [0] is mod, then it calls mod function"""
                print mod(int(tokens[1]), int(tokens[2]))
    except ValueError: 
        print "Oops! Your input is invalid. Please enter accurate operations."

