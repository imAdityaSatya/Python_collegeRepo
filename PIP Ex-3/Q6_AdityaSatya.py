'''
Aditya Satya
Ques 6
If the ages of Rahul, Ayush and Ajay are input through the keyboard,
write a python program to determine the elder among them.
'''

x= int(input("Rahul's Age= "))
y= int(input("Ayush's Age= "))
z= int(input("Ajay's Age= "))
age= max(x,y,z)
if age==x:
    print("Rahul is elder among them")
elif age==y:
    print("Ayush is elder among them")
else:
    print("Ajay is elder among them")



'''
if(x>y and y>z):
    print("Rahul is elder among them")
elif(y>x and x>z):
    print("Ayush is elder among them")
elif(z>y and y>x):
    print("Ajay is elder among them")
elif(x==y and x>z):
    print("Rahul and Ayush have the same age and are elder than Ajay")
elif(y==z and y>x):
    print("Ayush and Ajay have the same age and are elder than Rahul")
elif(x==z and x>y):
    print("Rahul and Ajay have the same age and are elder than Ayush")
else:
    print("All have same age")
'''
