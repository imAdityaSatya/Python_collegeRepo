'''
class Item:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def purchase(self, n):
        if self.quantity>=n
    def increaseStocks(self, n):
        self.quantity+=n
    def display(self):
        print('Enter name:',self.name)
        print('Enter price:',self.price)
        print('Enter quantity:',self.quantity)
'''

class Student:
    def __init__(self, rollNum, name, stream):
        self.rollNum = rollNum
        self.name = name
        self.stream = stream
        self.marksList = []
        self.percentage = 0
        self.grade = []
        self.division = ""

    def setMarks(self):
        marksList = []
        for i in range(5):
            marks = int(input("Enter marks for subject " + str(i + 1) + ": "))
            marksList.append(marks)
        self.marksList = marksList

    def getStream(self):
        return self.stream

    def percentageGen(self):
        self.percentage = sum(self.marksList)/5

    def gradeGen(self):
        for mark in self.marksList:
            if mark >= 90:
                self.grade="A"
            elif mark >= 80:
                self.grade="B"
            elif mark >= 65:
                self.grade="C"
            elif mark >= 40:
                self.grade="D"
            else:
                self.grade="E"

    def divisionGen(self):
        if self.percentage >= 60:
            self.division = "First"
        elif self.percentage >= 50:
            self.division = "Second"
        elif self.percentage >= 40:
            self.division = "Third"
        else:
            self.division = "Fail"


rollNum = int(input("Enter roll number: "))
name = input("Enter name: ")
stream = input("Enter stream(A: Arts, C: Commerce, S: Science): ")
student = Student(rollNum, name, stream)
student.setMarks()
student.percentageGen()
student.gradeGen()
student.divisionGen()
print("Name: ", student.name)
print("Roll number: ", student.rollNum)
print("Stream: ", student.getStream())
print("Marks: ", student.marksList)
print("Percentage: ", student.percentage)
print("Grade: ", student.grade)
print("Division: ", student.division)
