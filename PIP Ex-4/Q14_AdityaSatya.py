# Aditya Satya
'''
Q14. Write a python program that reads an integer and displays all its smallest factors in increasing order.
'''

n= int(input("Enter the integer: "))
print("Smallest factors of",n,"in increasing order: ")
while(n!=1):
    for i in range(2, n+1):
        if n%i==0:
            print(i,end=' ')
            n//=i
            break

