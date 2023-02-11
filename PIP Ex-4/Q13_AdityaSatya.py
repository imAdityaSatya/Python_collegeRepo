# Aditya Satya
'''
Q13. Write a python program that puts the binary representation of a positive integer N into a String s.
'''

n= int(input("Enter the num: "))
s=""
m=n
while n>0:
    rem=n%2
    s=str(rem)+s
    n//=2
print("Binary of",m,"is:",s)
