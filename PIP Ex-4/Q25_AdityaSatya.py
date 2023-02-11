# Aditya Satya
'''
Q25. Write a python program that prints all perfect numbers in between 1 and 500.
'''

def isPerfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n

for i in range(1,501):
    if isPerfect(i):
        print(i, end=' ')
    
