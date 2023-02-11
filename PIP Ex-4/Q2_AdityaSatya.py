# Aditya Satya
'''
Q2. Write a python program that displays all the numbers from 100 to 1,000, ten per line, that are divisible by 5 and 6. Numbers are separated by exactly one space.
'''

j=0
for i in range(100,1001):
    if (i%5==0 and i%6==0):
        print(i," ",end='')
        j+=1
    if j==10:
        j=0
        print()
