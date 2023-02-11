'''
n=int(input("Enter the num: "))
rev=0
num=n
while(n>0):
    rev= rev*10 + n%10
    n//=10
if num==rev:
    print("palindrome")
else:
    print("not palindrome")
'''
'''
def sum(n):
    sum=0
    while(n!=0):
        sum+= n%10
        n//=10
    return sum
n=int(input("Enter the num: "))
print(sum(n))
'''

'''
n= int(input("Enter a number: "))
sum = 0
tmp=n
while(tmp > 0):
   r= tmp%10
   sum+= r**3
   tmp//= 10
if n==sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
'''
'''
def gcd(a, b):
    if(b==0):
        return a;
    else:
        return gcd(b, a%b)

a= int(input("Enter num1: "))
b= int(input("Enter num2: "))
if gcd(a,b)==1:
    print("they are coprime")
else:
    print("they are not coprime")
'''

'''
def prod(a,b):
    res=0
    for i in range(0,b):
        res=+a
    print(res)
a= int(input("Enter num1: "))
b= int(input("Enter num2: "))
prod(a,b)     
'''
import math as m

def fct(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x
'''
def seriesSum(x, n):
    sum=1
    term=1
    fct=1
    p=1
    multi = 1
    
    for i in range(1, n):
        fct = fct * multi * (multi+1)
        p = p*x*x
        term = (-1) * term
        multi += 2
        sum = sum + (term * p)/fct
     
    return sum
'''
'''
def pattern(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
pattern(4)
'''
'''
i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
else:
    print(0)
    
x= 'abcd'
for i in range(len(x)):
    print(x)
x='a'

x=123
for i in x:
    print(i)

for i in range(0):
    print(i)

i=0
while i<3:
    print(i)
    i+=1
else:
    print(0)
'''

x= 'abcd'
for i in range(len(x)):
    print(x)
    x='a'
