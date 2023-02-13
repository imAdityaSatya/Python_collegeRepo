def ana(s1, s2):
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
            return True
        else:
            return False
    else:
        return False

x=input()
y=input()
print(ana(x,y))
