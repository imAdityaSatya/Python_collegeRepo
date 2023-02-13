def numOfWords(s):
    cnt=1
    for i in s:
        if i==' ':
            cnt+=1
    return cnt
s= input()
print(numOfWords(s))