'''
def f(one, *two):
    print(type(two))
f(1,2,3,4)

def c(i=1, j=2):
    i+=j
    j+=1
    print(i,j)
    return i
c(j=1, i=2)

a=5
b=4
a+=a-b+10//3**3
b=~2+5<<3
a,b=b,a
print("a=",a,"and b=",b)

def power(m,n):
    return m**n
m=6
n=2
print("6 raised to the power 2 is",power(6,2))

class Student:
    def __init__(self, reg, name):
        self.reg=reg
        self.name=name
ob=Student('Naveen',20190)
print(ob.reg)

import pdb
pdb.set_trace()
def p():
    print('Here it is')
def main():
    p()
if __name__=='__main__':
    main()

x= int(input('Enter first num:'))
y= int(input('Enter sec num:'))
z=x+y/2
print('avg of the numbers is:',z)

a=10
def f():
    a=5
    a=a-2
    def g():
        a=8
        print(a,end=':')
    g()
    print(a*3,end=',')
f()
print(a)

class Person:
    def __init__(self, v1,v2=''):
        self.v1=v1
        self.v2=v2
ob= Person('Hi')
print(ob.v2)

def f(p,q,r):
    global s
    p=10
    q=20
    r=30
    s=40
    print(p,q,r,s)
p,q,r,s=1,2,3,4
f(5,10,15)

a='"ghi"'
print(type(a))

def A():
    t='Honourable'
    n2=(lambda x: t+' '+x)
    return n2
n3= A()
res=n3('President')
print(res)

def S(n):
    sum=0
    for i in range(n,0,-1):
        sum+=i
    return sum
print(S(3))

s1='impossible'
s2=''
v=('a','e','i','o','u')
print(s2.join([c for c in s1 if c not in v]))
#mpssbl

def cnt(n, val):
    tot=0
    if n==1 and val>=0:
        return 1
    for i in range(val+1):
        tot+= cnt(n-1, val-i)
    return tot
def main():
    n=int(input())
    val=int(input())
    print(cnt(n,val))
if __name__=='__main__':
    main()

n=1
def fun(cnt):
    print(cnt,end=' ')
    if(cnt<3):
        cnt+=1
        fun(fun(fun(cnt)))
    return cnt
if __name__=='__main__':
    fun(n)

def fun(s1,s2):
    t1=s1.lower()
    t2=s2.lower()
    cnt=0
    for c1 in t1:
        for c2 in t2:
            if c1==c2:
                cnt+=1
    return cnt
def main():
    n1='Ram Rahim'
    n2='SAMARTH RAHI'
    print(fun(n1,n2))
if __name__=='__main__':
    main()

n=set([1,1,2,3,3,3,4,4])
print(len(n))

def fun(n):
    return n+10
fun('Hello')

a=3
b=2
for i in range(3):
    for j in range(2):
        a=a+b
print(a,b)
'''
'''
import pickle
f= open("Data.txt", 'rb')
d= pickle.load(f)
f.end()
----------------------------
'''
'''
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 2
    else:
        return f(n-1)+f(n-2)
n=5
for i in range (0,n):
    print(f(i),end="")
'''
'''
def p(x,y):
    if x==0:
        return y
    else:
        return p(x-1,x+y)
print(p(6,2))
'''
'''
class A:
    def __init__(self,i):
        self.i=i
        self.multiply(self.i)
    def multiply(self,i):
        self.i=4*i
class B(A):
    def __init__(self):
        super().__init__(15)
        print(self.i)
    def multiply(self,i):
        self.i*=6
obj=B()
'''
'''
def c2f(c):
    return c*9/5+32
print(c2f(100))
print(c2f(0))
'''
'''
l=[(6,7), (2,3), (7,6), (9,8), (10,2), (8,9), (1,1)]
tmp= set(l)&{(b,a) for a,b in l}
r= {(a,b) for a,b in tmp if a<=b}
print(r)
'''
'''
def h():
    print("I am here")
def h():
    print("Now, I am here")
h()
'''
'''
for i in range(1,13):
    sum=0
    for j in range(1,i//2+1):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i)
'''
'''
def f(n):
    if n<=1:
        return 1
    if n%2==0:
        return f(n//2)
    return f(n//2) + f(n//2+1)
print(f(9))
'''
'''
try:
    try:
        a=51+'hello'
    except ValueError:
        print('Value Error')
except:
    print('Type Error')
'''
'''
l=list()
a= input("Enter name: ")
for i in a:
    l=a.split(" ")
for i in range(0, len(l)-1):
    b=l[i][0].upper()
    print(b,".",end=" ")
print(l[len(l)-1].capitalize())
'''
'''
class A:
    def __init__(self, var):
        self.var=var
    def __str__(self):
        return str(self.var)
A=A(1)
print(A)
delattr(a,'temp')
'''
'''
def fact(n):
    return n>>0 +2
print(fact(16))
'''
'''
def main():
    m=110
    try:
        if m<0 or m>100:
            raise ValueError("Marks out of range")
    except:
        pass
    finally:
        print('Welcome')
    print("Program continues after handling exception")
if __name__=='__main__':
    main()
'''
'''
class stud:
    def __init__(self,regd,name):
        self.regd=regd
        self.name=name
ob= stud(20190,'Naveen')
print(ob.regd)
'''
'''
class Person:
    def __init__(self,v1,v2=''):
        self.v1=v1
        self.v2=v2
ob=Person('Hi')
print(ob.v1)
'''
'''
def c():
    x=4
def d():
    c()
    print(x)
d()
'''
'''
a=1
b=4
c=3
d=b*b-4*a*c
if d>0:
    print("eqn has two distinct roots.")
elif d==0:
    print("eqn has one root.")
else:
    print("eqn has no real root.")
'''
'''
class Change:
    def __init__(self,x,y,z):
        self.a= x+y+z
x= Change(2,8,7)
p= getattr(x,'a')
setattr(x,'a',p+1)
print(x.a)
'''
'''
def get(n):
    if n<1 or n>8:
        raise ValueError('Invalid')
    print(n)
get(6)
'''




























