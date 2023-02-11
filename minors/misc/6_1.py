def fun(s):
    c= s[0]
    for i in range(1, len(s)):
        if s[i-1]==s[i]:
            c+='*'
        else:
            c+=s[i]
    return c

s= (input())
print(fun(s))
   
