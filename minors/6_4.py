def fun(s):
    c= list(s)
    for i in range(len(s)):
	    if i == 0 and c[i] != ' ' or c[i] != ' ' and c[i - 1] == ' ':
		    if c[i] >= 'a' and c[i] <= 'z':
		    	c[i] = chr(ord(c[i]) - ord('a') + ord('A'))
	    elif c[i] >= 'A' and c[i] <= 'Z':
    		c[i] = chr(ord(c[i]) + ord('a') - ord('A'))
    return''.join(c)
str= input()
print(fun(str))



'''
---o/p testing---
s= input()
print(fun("i am tHE coolEST mAN aLIVE"))
'''
