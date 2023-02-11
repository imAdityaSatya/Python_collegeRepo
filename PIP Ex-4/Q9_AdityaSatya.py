# Aditya Satya
'''
Q9. Write a python program to generate and print the first n terms of the Fibonacci sequence where n>=1. 
'''

n=int(input("Enter the value of n: "))
a=0
b=1
print("The fibonacci series: ")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
