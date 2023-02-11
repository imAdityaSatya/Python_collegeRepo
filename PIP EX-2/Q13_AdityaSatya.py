# Aditya Satya
'''Enter the basic salary of an employee of an organization through the command prompt. His dearness allowance (DA) is 40% of basic salary, and house rent allowance (HRA) is 20% of basic salary. Write a python program to calculate his gross salary.'''

import sys
basic=float(sys.argv[1])
da=(basic*0.4)
hra=(basic*0.2)
print("DA:",da)
print("HRA:",hra)
print("GROSS:",basic+da+hra)
