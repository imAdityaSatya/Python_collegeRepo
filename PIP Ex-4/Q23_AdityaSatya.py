# Aditya Satya
'''
Q23. Input an integer n. Write a java program that will find the smallest exact divisor other than one.
'''

n=int(input("Enter the integer: "))
for i in range(2,n+1):
    if n%i==0:
        print("Smallest exact divisor other than one is: ",i)
        break
