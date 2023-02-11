# Aditya Satya
'''
Q24. Write a python program that tests whether a given pair of numbers is amicable numbers or not.
'''

print("Enter the pair: ")
x=int(input())
y=int(input())
tmp=y
a=0
b=0
for i in range(1,tmp):
    if tmp%i==0:
        a+=i
tmp=x
for i in range(1,tmp):
    if tmp%i==0:
        b+=i
if a==x and b==y:
    print("amicable")
else:
    print("not amicable")

