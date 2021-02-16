#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

import math
a = float(input("Please enter integer "))
b = float(input("Please enter integer "))
c = float(input("Please enter integer "))

if b > c:
    x = c
    y = b
else:
    x = b
    y = c

if a**2 + x**2 == y**2:
    print(str(a) + str(x) + str(y) +" form a Pythagorean triple")
elif a**2 + x**2 != y**2:
    print(str(a) + str(x) + str(y) +" do not form a Pythagorean triple")

#test1 6,10,8 form a triple
#test2 3,4,5 form a triple