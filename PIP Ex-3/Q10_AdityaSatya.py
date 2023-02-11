'''
Aditya Satya
Ques 9
A University conducts a 100 mark exam for its student and grades them as follows. Assigns a grade based on the value of the marks.
Write a python program to print the grade according to the mark secured by the student.
'''

marks= float(input("Enter your marks: "))
if marks>=90 and marks<=100:
   print("O grade")
elif marks>=80 and marks<90:
   print("'A' grade")
elif marks>=70 and marks<80:
   print("B grade")
elif marks>=60 and marks<70:
   print("C grade")
elif marks>=50 and marks<60:
   print("D grade")
elif marks>=40 and marks<50:
   print("E grade")
elif marks<40 and marks>=0:
   print("F grade")
else:
    print("Invalid marks entered...")
