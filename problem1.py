"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue
"""

#! python3


import math
a = float(input("Please enter number "))

if (a % 6) == 0 and (a % 8) != 0:
    print (str(a) +" is frue.")
else:
    print (str(a) +" is not frue.")
