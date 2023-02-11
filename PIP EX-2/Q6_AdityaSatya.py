# Aditya Satya
''' Write a python program that prompts the user to enter three points (x1, y1), (x2, y2), (x3, 
y3) of a triangle and displays its area.'''

import math as m
print("Enter three points for a triangle: ")
x1,y1,x2,y2,x3,y3= float(input()),float(input()),float(input()),float(input()),float(input()),float(input())
a= m.sqrt((x2-x1)**2 + (y2-y1)**2)
b= m.sqrt((x3-x2)**2 + (y3-y2)**2)
c= m.sqrt((x3-x1)**2 + (y3-y1)**2)
s= (a+b+c)/2
area = m.sqrt(s*(s-a)*(s-b)*(s-c))
print("The Area of triangle is ", area)
