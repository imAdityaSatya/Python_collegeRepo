'''x= ['ab', 'cd']
for i in x:
    i.upper()
print(x)
'''
'''
i=1
while True:
    if i%3==0:
        break
    print(i)
    i+=1
'''

'''
i=1
while True:
    if i%7==0:
        break
    print(i)
    i+=1
'''
'''
i=1
while False:
    if i%2==0:
        break
    print(i)
    i+=2
'''
'''
print("#############################")
total=0
cnt=10
while(cnt>5):
    total+=cnt
    cnt-=1
print(total)
'''

'''
x= (i for i in range(3))
for i in x:
    print(i)
for i in x:
    print(i)
'''
'''
string= "my name is x"
for i in string:
    print(i, end=", ")
'''
'''
def ex(a):
    a=a+'2'
    a=a*2
    return a

x= (i for i in range(3))
for i in x:
    print(i)
for i in x:
    print(i)

tot=0
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        for k in range(1,j+1):
            tot+=1
print(tot)

s=0
for i in range(2,9):
    if(i%2==0):
        s+=i
        break
print(s)
'''

row= int(input())
for i in range(row,0,-1):
    print(i,end)
    j=i-1
    while(False):
        print(j, end='')
        if j==1:
            break
        j-=1
    print()
print(1)
