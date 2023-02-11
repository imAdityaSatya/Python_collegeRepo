# Aditya Satya
'''
Q18. Write a python program to generate the first n terms of the sequence without using multiplication.
     1 2 4 8 16 32 ……….
'''

n=int(input("Enter the value of n: "))
print("The first n terms of the given sequence are: ")
for i in range(n):
    print(2**i,end=" ")
