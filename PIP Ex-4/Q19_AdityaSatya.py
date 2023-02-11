# Aditya Satya
'''
Q19. Write a python program to determine whether or not a number n is a factorial number.
'''

n=int(input("Enter the num: "))
i=1
while True:         
    if n%i==0:
        n//=i  
    else:
        break    
    i+=1
if(n == 1):
    print("factorial")
else:
    print("not factorial")
