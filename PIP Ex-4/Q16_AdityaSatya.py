# Aditya Satya
'''
Q16. Write a python program to check a number n is prime or not. The number to be inputted through keyboard.
'''

import math as m
n=int(input("Enter the num: "))
tmp=0
for i in range(2, int(m.sqrt(n)+1)):
    if n%i==0:
        tmp=1
        break
    
if tmp==0:
    print("prime")
else:
    print("not prime")
