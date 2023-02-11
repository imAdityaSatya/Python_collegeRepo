# Aditya Satya
'''
Q12. Write a python program to compute the square root of a number using Newton’s method.
'''

n=int(input("Enter the value of n: "))
g1=0
g2=n/2
while True:
    g1=g2
    g2=(g1+(n/g1))/2
    if(abs(g1-g2)<0.000001):
        break
print("Sq root of",n,"is: ",g2)
