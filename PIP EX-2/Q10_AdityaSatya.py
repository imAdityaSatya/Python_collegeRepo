# Aditya Satya
''' Write a python program that takes two int values a and b from the command line and prints a random integer between a and b.'''

import random,sys
a=int(sys.argv[1])
b=int(sys.argv[2])
random=random.randint(a,b)
print('Random integer= ',random)
