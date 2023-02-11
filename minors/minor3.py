'''
#2a
total = 0
count = 20
while count > 5:
    total += count
    count -= 1
print(total)


#2b
total=0
N = 5
for i in range(1, N+1):
    for j in range(1, i+1):
        total+= 1
print(total)

#2c
total = 0
N = 10
for i in range(1, N+1):
    for j in range(1, i+1):
        total += 1
print(total)

#2d
total = 0
N = 5
for i in range(1, N+1):
    for j in range(1, i+1):
        total += 1
    total -= 1
print(total)

#2e
total = 0
N = 5
for i in range(1, N+1):
    for j in range(1, N+1): 
        total += i
print(total)

#Q3
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    if(n==sum):
        print("perfect")
    else:
        print("not perfect")


n= int(input())
perfect(n)


#Q4
def lcm(a, b):
    m= max(a,b)    
    while True:
        if(m%a==0 and m%b==0):
            lcm = m
            break
        m+=1
    return lcm

a= int(input("Enter first num: "))
b= int(input("Enter second num: "))
lcm= lcm(a, b)
print("LCM= ",lcm)


# Q5
def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)
    
a= int(input("Enter first num: "))
b= int(input("Enter second num: "))
gcd= gcd(a, b)
print("GCD= ",gcd)

#6a
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
pattern(5)

#6b
n=4
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ', end=' ')
    for j in range(i,0,-1):
        print(j, end=' ')
    for j in range(2,i+1):
        print(j, end=' ')
    print()
#6c
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

#6d
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

#6e
n=5
for i in range(1,n+1):
    print('  '*(i-1),end='')
    for j in range(i,n+1):
        print(j,end=' ')
    print()

#6f
n=5
for i in range(n):
    if i==0 or i==n-1:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')

#6g
n=5
for i in range(1,n+1):
    print('* '*n)

#6h
n=4
s='*'
for i in range(1,n+1):
    print('  '*(n-i)+s)
    s='* '+s+' *'

#6i
n=4
for i in range(1,n+1):
    for j in range(0,i):
        print(' ',end='')
    for j in range(1, (n*2-(2*i-1))+1):
        if i == 1 or j == 1 or j ==(n*2 -(2*i-1)):
            print('*', end='')
        else:
            print(' ', end='')
    print()

#6j
n=4
for i in range(1,n+1):
    print('  '*i,end='')
    for j in range(1, (n*2-(2*i-1))+1):
        print('* ',end='')
    print()

#6k
#6n
n=5
for i in range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print('#',end='')
    print()

#tst
def fact(n):
    f=1
    for i in range(n):
        f*=(i+1)
    return f

print(fact(5))

def isArm():
    sum=0
    num=n
    while(n>0):
        sum+=(n%10)**3
        n//=num
    return sum==num

for i in range(1,10001):
    if isArm(i):
        print(i)     
'''
n=5
for i in range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print('#',end='')
    print()
