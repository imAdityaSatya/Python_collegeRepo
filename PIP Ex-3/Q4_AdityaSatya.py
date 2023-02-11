'''
Aditya Satya
Ques 4
Write a python program that prompts the user to enter a, b, c, d, e, and f and displays the result.
If ad - bc is 0, report that “The equation has no solution.”
'''

a,b,c,d,e,f= input("Enter a, b, c, d, e, f: ").split()
a,b,c,d,e,f= float(a), float(b), float(c), float(d), float(e), float(f)

if a*d-b*c==0:
   print("The equation has no solution.")
else:
   x=(e*d-b*f)/(a*d-b*c)
   y=(a*f-e*c)/(a*d-b*c)
   print("x is",x,"and y is",y)
