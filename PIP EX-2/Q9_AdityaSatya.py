# Aditya
'''Write a python program that takes two positive integers as command-line arguments and prints true if either evenly divides the other.'''

import sys
a= int(sys.argv[1])
b= int(sys.argv[2])
res= (a%b==0 or b%a==0)
print(res)
