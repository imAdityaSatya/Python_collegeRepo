# Aditya Satya
'''Write a python program to exchange the values of two variables of integer type A and B 
without using third temporary variable'''

print("Method-1")
a=23
b=69
print("before swap: ",a,b)
a=a+b
b=a-b
a=a-b
print("after swap : ",a,b)

print("\nMethod-2")
a=23
b=69
print("before swap: ",a,b)
a=a*b
b=a/b
a=a/b
print("after swap : ",a,b)

print("\nMethod-3")
a=23
b=69
print("before swap: ",a,b)
a,b=b,a
print("after swap : ",a,b)
print()
