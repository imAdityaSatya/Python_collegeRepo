# Aditya Satya
'''Write a python program that takes two int values m and d from the command line and prints true if day d of month m is between 3/20 and 6/20, false otherwise.'''

import sys
m= int(sys.argv[1])
d= int(sys.argv[2])
res= (m==3 and(d>20 and d<=31)) or (m==4 and d<=31) or (m==5 and d<=31) or (m==6 and d<=20)
print(res)
