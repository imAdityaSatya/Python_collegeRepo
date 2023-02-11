# Aditya Satya
'''
Q11. Write a python program that accepts a positive integer n and reverses the order of its digits.
'''

n=int(input("Enter the value of n: "))
res=0
print("Before reversal:",n)
while n>0:
    tmp= n%10
    res= res*10 + tmp
    n//=10
print("After reversal :",res)
