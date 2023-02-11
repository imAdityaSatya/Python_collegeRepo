# Aditya Satya
'''Write a python program 
that asks the user how many eggs she has and then tells the user how many dozen eggs she 
has and how many extra eggs are left over. A gross of eggs is equal to 144 eggs. Extend 
your program so that it will tell the user how many gross, how many dozen, and how many 
left-over eggs she has.'''


eggs= int(input("Num of eggs= "))
gross= eggs/144
tmp= eggs%144
dozens= tmp/12
tmp= tmp%12
print("Your number of eggs is",int(gross),"gross,",int(dozens),"dozens and",tmp)

