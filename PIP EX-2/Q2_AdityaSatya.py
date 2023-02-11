# Aditya Satya
''' Write a python program that reads an integer between 0 and 1000 and adds all the digits in 
the integer.'''

n= int(input())
a=n%10
n//=10
b=n%10
n//=10
c=n%10
print(a+b+c)
