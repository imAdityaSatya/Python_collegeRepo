'''
n = int(input("Enter the num: "))
print(n, "x", 1, " =", n * 1)
print(n, "x", 2, " =", n * 2)
print(n, "x", 3, " =", n * 3)
print(n, "x", 4, " =", n * 4)
print(n, "x", 5, " =", n * 5)
print(n, "x", 6, " =", n * 6)
print(n, "x", 7, " =", n * 7)
print(n, "x", 8, " =", n * 8)
print(n, "x", 9, " =", n * 9)
print(n, "x", 10, "=", n * 10)


def f1():
    x=15
    print(x)
x=12
f1()

def f1():
    x=100
    print(x)
x+=1
f1()

def san():
    print(x+1)
x=-2
x=4
san(12)


def f1():
    global x
    x+=1
    print(x)
x=12
print("x")


def f1(x):
    g
    lobal x
    x+=1
    print(x)
f1(15)
print("hello")

def san(x):
    print(x+1)
x=-2
x=4
san(12)
'''
'''
def f1():
    x=100
    print(x)
x=+1
f1()
'''
'''
def fun(n):
    for i in range(1,n+1):
        print('#'*i)
n= int(input())
print(fun(n))
'''
'''
cc=2
if False:
    cc=66
def h():
    if True:
        cc=40
h()
print(cc)


def f(p,q,r):
    global s
    p=10
    q=20
    r=30
    s=40
    print(p,q,r,s)
p,q,r,s= 1,2,3,4
f(5,10,15)
'''
x=6
def h():
    x=15
    def f():
        x=16
        def g():
            nonlocal x
            print(x, end='')
            x=20
            print(x,end='')
        g()
        print(x,end='')
    f()
    print(x,end='')
h()
print(x,end=''
      )
