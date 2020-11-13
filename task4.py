#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704

side1=input("The side1 is ")

side2=input("The side2 is ")

side1=int(side1)

side2=int(side2)

import math

hypotenuse=side1**2+side2**2

hypotenuse=math.sqrt(hypotenuse)

print(hypotenuse)
