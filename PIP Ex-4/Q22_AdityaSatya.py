# Aditya Satya
'''
Q22. Write a python program that reads in a set of n single digits and converts them into a single decimal integer.
'''

n=int(input("num of digits, n= "))
s=0
print(n,"digits are:
      ")
for i in range(n):
    m=int(input())
    s=(s*10)+m
print("The integer formed is:",s)

