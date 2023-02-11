# Aditya Satya
'''s. Write a 
python program that prompts the user to enter a weight in pounds and height in inches and 
displays the BMI.'''

import math as m
w= float(input("Enter weight in pounds: "))
h= float(input("Enter height in inches: "))
bmi= (w*0.45359237)/(m.pow(h*0.0254,2))
print("BMI is ",bmi)
