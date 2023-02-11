# Aditya Satya
''' Write a python program that prompts the user to enter the minutes (e.g., 1 billion), and 
displays the number of years and days for the minutes.'''

mins= int(input("Enter the num of mins: "))
yrs= mins/(60*24*365)
days= mins%(60*24*365)
print(mins,"minutes is approximately",int(yrs),"years and",int(days),"days.")
