# Aditya Satya
'''
Q1. Write a python program that takes the value of N through keyboard and prints a table of the power of 2 that are less than or equal to 2N.
'''

n=int(input("Enter a number "))
for i in range(n+1):
    print(i,"\t",2**i)
