#1
'''
s= input("Enter the string: ")
x= s[0]
for i in range(1, len(s)):
    if s[i-1]==s[i]:
        x+="*"
    else:
        x+=s[i]
print(x)
'''

#2
s1=input()
s2=input()
len1=0
len2=0
r=0

if len1==len2:
    for i in s1:
        len1+=1
    for i in s2:
        len2+=1
    for i in s1:
        for j in s2:
            if i==j:
                r+=1
    if r==len1:
        print("True")
    else:
        print("false")
else:
    print("flase")
