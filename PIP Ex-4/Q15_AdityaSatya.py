# Aditya Satya
'''
Q15. Write a python program GCD that finds the greatest common divisor (gcd) of two integers using Euclid’s algorithm
'''

def gcd(a, b):
    if(b==0):
        return a;
    else:
        return gcd(b, a%b)

x= int(input("Enter the x: "))
y= int(input("Enter the y: "))
print("GCD of",x,"and",y,"is:",gcd(x,y))
