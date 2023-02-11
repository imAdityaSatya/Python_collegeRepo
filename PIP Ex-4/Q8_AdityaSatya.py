# Aditya Satya
'''
Q8. Assume that x is a positive variable of type double. Write a python code fragment that uses the
    Taylor series expansion to set the value of sum to ex = 1 + x + x2/2! + x3/3! +……
'''

import math as m
x= eval(input("Enter the value of x: "))
#print(m.exp(x))
sum=1
term=1
i=0
error=0.000001
while(m.fabs(term)>error):
    i+=1
    term=(x/i)*term
    sum+=term
print("e^",x,"=",sum)
