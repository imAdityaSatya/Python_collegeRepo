'''
Aditya Satya
Ques 3
Write a python program that prompts the user to enter values for a, b, and c and displays the result based on the discriminant.
If the discriminant is positive, display two roots. If the discriminant is 0, display one root.
Otherwise, display “The equation has no real roots”.
'''

import math as m
a, b, c= input("Enter a, b, c: ").split()
a, b, c= float(a), float(b), float(c)
d=(b**2)-4*a*c
if(d>0):
   r1=(-b+m.sqrt(d))/(2*a)
   r2=(-b-m.sqrt(d))/(2*a)
   print("The equation has two roots",r1,"and",r2)
elif(d==0):
   r2=(-b-m.sqrt(d))/2*a
   print("The equation has one root",r2)
else:
    print("The equation has no real roots")
