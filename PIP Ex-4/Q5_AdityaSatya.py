# Aditya Satya
'''
Q5. For a given x and a given n, write a python program to compute xn/n!.
'''

import math as m
n=int(input("n= "))
x=int(input("x= "))
print("(x^n/n!)=",(x**n)/m.factorial(n))
