# Aditya Satya
''' Write a python program that prompts the user to enter two points (x1, y1) and (x2, y2) and 
displays their distance between them. '''

import math as m
print("Enter x1 and y1: ")
x1, y1= float(input()), float(input())
print("Enter x2 and y2: ")
x2, y2= float(input()), float(input())
d= m.sqrt((x2-x1)**2 + (y2-y1)**2)
print("The distance between the two points is ", d)
