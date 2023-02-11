# Aditya Satya
'''
Q4. Input a number n, write a python program to compute n factorial (written as n!) where n>=0.
'''

n=int(input("Enter the value of n: "))
fact=1
if n<0:
   print("Plz enter a pos int")
else:
   for i in range(1,n + 1):
       fact = fact*i
   print("Factorial of",n,"is",fact)
