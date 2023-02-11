# Aditya Satya
'''Write a python program that prints the sum of two random integers between 1 and 6 (such as you might get when rolling dice).'''

import random,sys
a=int(sys.argv[1])
b=int(sys.argv[2])
x=random.randint(a,b)
y=random.randint(a,b)
sum=x+y
print('The sum is',sum)
