# Aditya Satya
'''
Q20. For some integer n, write a python program to find the largest factorial number present as
     factor in n.
'''

def chkFact(n):
    i=1
    while True:         
        if n%i==0:
            n//=i  
        else:
            break    
        i+=1
    if n==1:
        return True
    else:
        return False
    
n= int(input("Enter the num: "))
factors=[]
for i in range(1,n+1):
    if n%i==0:
       factors.append(i)
max=0
for i in range(len(factors)):
    if chkFact(factors[i]):
        if(factors[i]>max):
            max=factors[i]
print("The largest factorial num present is:",max)
