""" Task
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird 
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20 , print Not Weird """

import math
import os
import random
import re
import sys

nw=range(2,6)
w=range(6,21)
c=range(0,101)
if __name__ == '__main__':
    n = int(input().strip())
    mod=n%2
    if (n in c and mod==0 and ((n in nw) or (n > 20))):
            print("Not Weird")
    elif (n in c and ( mod!=0 or n in w)):
        print("Weird")
    else:
        print("Given number is out of range!")
