'''
Aditya Satya
Ques 2
Any character is entered through the keyboard, write a python program to determine whether the character entered is a capital letter, a small case letter, a digit or a special symbol.
'''

ch= (input("Enter the Character: "))
if(ch >= 65 and ch <= 90):
    print(ch,"is a capital letter")
elif(ch >= 97 and ch <=122):
    print(ch,"is a small letter")
elif(ch >=48 and ch <= 57):
    print(ch,"is a digit")
elif(ch>=0 and ch<=47 or ch>=58 and ch<=64 or ch>=91 and ch<=96 or ch>=123 and ch<=127):
    print(ch,"is a special symbols")  

