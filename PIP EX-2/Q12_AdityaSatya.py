# Aditya Satya
'''Write a python program that takes three double values x, y, and z as command-line arguments and prints true if the values are strictly ascending or descending (x < y < z or x > y > z), and false otherwise.'''

import sys
x=float(sys.argv[1])
y=float(sys.argv[2])
z=float(sys.argv[3])
res=(((x<y)and(y<z))or((x>y)and(y>z)))
print(res)
