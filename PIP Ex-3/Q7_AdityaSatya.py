'''
Aditya Satya
Ques 7
Write a python program that prompts the user to enter the month and year and displays the number of days in the month.
'''

m=int(input("month: "))
y=int(input("year: "))
if((m==2) and ((y%400==0) or (y%4==0 and y%100!=0))):
    print("February",y,"had 29 days.")
elif(m==2):
    print("February",y,"is of 28 days.")
#elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
elif m==1:
    print("January",y,"had 31 days.")
elif m==3:
    print("March",y,"had 31 days.")
elif m==4:
    print("April",y,"had 30 days.")
elif m==5:
    print("May",y,"had 31 days.")
elif m==6:
    print("June",y,"had 30 days.")
elif m==7:
    print("July",y,"had 31 days.")
elif m==8:
    print("August",y,"had 31 days.")
elif m==9:
    print("September",y,"had 30 days.")
elif m==10:
    print("October",y," had 31 days.")
elif m==11:
    print("November",y,"had 30 days.")
elif m==12:
    print("December",y," had 31 days.")
else:
    print("This is not a correct input.")
