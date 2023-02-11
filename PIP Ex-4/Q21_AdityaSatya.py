# Aditya Satya
'''
21. Given two numbers d and e are suspected of being consecutive members of the Fibonacci sequence. Write a python program that will refute or confirm this conjecture.
'''


d= int(input("d= "))
e= int(input("e= "))
a=0
b=1
s=0
k=0
for i in range(max(d,e)):
    if ((d==0) and (e==1)) or ((d==1) and (e==0)):
        k=1
        print("confirm")
        break
    else:
        if ((d==a) and (e==b)) or ((d==b) and (e==a)):
            k=1
            print("confirm")
            break
        s=a+b
        a=b
        b=s
if k==0:
    print("refute")
