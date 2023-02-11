# Aditya Satya
'''
Q7. Write a python program to evaluate the function cos(x) as defined by the infinite series expansion.
    cos(x) =1- x2/2! + x4/4! - x6/6! +...
    The acceptable error for computation is 10^-6.
'''

import math as m
x= int(input("Enter the value of x for cos(x): "))
x= m.radians(x)
i=0
term=1
cos=1
error=0.000001
while(m.fabs(term)>error):
    i+=2
    term= (-term*x*x)/((i-1)*i)
    cos+=term
print("cos(",x,")= ",cos)
