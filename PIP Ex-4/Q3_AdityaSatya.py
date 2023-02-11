# Aditya Satya
'''
Q3. Write a python program to compute the sum of the first n terms (n>=1) of the series.
    S=1-3+5-7+9-………
'''

n=int(input("Enter the value of n: "))
sum=0
odd=1
ssum=0
sign=0
for i in range(0,n):
    sign= int(pow(-1,i))
    ssum= odd*sign
    sum+=ssum
    odd+=2
print("The sum of first",n,"terms of the series: ", sum)
