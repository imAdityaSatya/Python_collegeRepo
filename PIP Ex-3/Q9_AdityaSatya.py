'''
Aditya Satya
Ques 9
Write a python program that prompts the user to enter a point (x, y) and checks whether the point is within the circle centered at (0, 0) with radius 10.
'''
import math as m
x1=0
y1=0
r=10
x2,y2= input("Enter a point with two coordinates: ").split()
x2, y2= float(x2), float(y2)
d= m.sqrt((x2-x1)**2+(y2-y1)**2)
if d<r:
   print("Point(",x2,",",y2,") is inside the circle")
elif d>r:
   print("Point(",x2,",",y2,") is outside in the circle")
else:
   print("Point(",x2,",",y2,") is on the circle")
