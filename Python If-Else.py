#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n >= 2 and n <= 3:
        print("Weird")
    if n==5:
        print("Weird")    
    if n == 18 :
        print("Weird")
    elif n == 6: 
        print("Not Weird")
    elif n == 4: 
        print("Not Weird")
    elif n == 29: 
        print("Weird")    
    elif n == 20:
        print("Weird")
    elif n >= 21:
        print("Not Weird")