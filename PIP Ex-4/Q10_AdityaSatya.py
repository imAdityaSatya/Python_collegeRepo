# Aditya Satya
'''
Q10. Write a python program to generate and print the first n terms of the Fibonacci numbers using an efficient algorithm. In this case, you need to find a pair of Fibonacci terms, in each iteration and display them and adjust the preceding term b and the term before the preceding term a. Your program should handle all positive values of n.
'''

n= int(input("Enter the value of n: "))
a=0
b=1
c=2
print("Fibonacci series is: ",end='')
while(c<n):
    print(a,b,end=' ')
    a=a+b
    b=a+b
    c=c+2
if c==n:
    print(a,b,end=' ')
else:
    print(b)
