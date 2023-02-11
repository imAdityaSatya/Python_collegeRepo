# Aditya Satya
'''
Q6. Write a python program to evaluate the function sin(x) as defined by the infinite series expansion.
    sin (x) = x- x3/3! + x5/5! - x7/7! +...
    The acceptable error for computation is 10^-6.
'''

import math as m
x= int(input("Enter the value of x for the expansion of sin(x) : "))
x= m.radians(x)
i=1
term=x
sin=x
error=0.000001
while(m.fabs(term)>error):
    i+=2
    term= (-term*x*x)/((i-1)*i)
    sin+=term
print("sin(",x,") =",sin)
