'''
#3
class allPossibleSubsets:
    def subsets(self, tmp, s):
        if s:
            return self.subsets(tmp,s[1:]) + self.subsets(tmp+[s[0]],s[1:])
        return [tmp]
    def subset(self, s):
        return self.subsets([],sorted(s))
    
print(allPossibleSubsets().subset([4,5,6]))
'''
'''
#4
class BankAccount:
    account_number = 0
    name = ""
    balance_amount = 0

    def account_creation(self):
        self.account_number = int(input("Enter the account number\t"))
        self.name = input("Enter the account holder name\t")

    def amount_deposition(self, amount):
        self.balance_amount = self.balance_amount + amount

    def amount_withdrawn(self, amount):
        if(amount<=self.balance_amount):
            self.balance_amount = self.balance_amount - amount
        else:
            print("Less Ammount")
    def display_account(self):
        print("Name: ",self.name,"\tAccount Number: ",self.account_number,"\tBalance: ",self.balance_amount)
ch=''
acc=BankAccount()
while ch!=5:
    print("\tMAIN MENU\t")
    print("\t1. NEW ACCOUNT\t")
    print("\t2. DEPOSIT AMOUNT\t")
    print("\t3. WITHDRAW AMOUNT\t")
    print("\t4. BALANCE ENQUIRY\t")
    print("\t5. EXIT\t")
    ch=int(input("\nChoose the desired option: "))
    if ch==1:
        acc.account_creation()
    elif ch==2:
        acc.amount_deposition(int(input()))
    elif ch==3:
        acc.amount_withdrawn(int(input()))
    elif ch==4:
        acc.display_account()
    elif ch==5:
        break
'''
'''
#5
class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def purchase(self,item):
        if(item>self.quantity):
            print("Low quantity")
        else:
            self.quantity-=item
    def increaseStock(self,item):
        self.quantity+=item
    def display(self):
        #return 'Name: '+self.name+"\nPrice: "+str(self.price)+"\nQuantity: "+str(self.quantity)
        #print("Name of item: ",self.name,"\tPrice: ",self.price,"\tQuantity: ",(self.quantity))
        print("Name of item: ",self.name)
        print("Price: ",self.price)
        print("Quantity: ",self.quantity)
'''

#6
class Student:
    def __init__(self, rollNumber, name, marksList, stream, percentange, grade, division):
        self.rollNumber = rollNumber
        self.name = name
        self.marksList = marksList
        self.stream = stream
        self.percentange = percentange
        self.grade = grade
        self.division = division

    def setMarks(self):
        self.marksList = eval(input("Enter the marks in list fashon: "))

    def getStream(self):
        print(self.stream)

    def Percantage(self):
        self.percentange = sum(self.marksList)/len(self.marksList)

    def gradeGen(self):
        if self.percentange>=90:
            self.grade='A'
        elif self.percentange>=80:
            self.grade='B'
        elif self.percentange>=65:
            self.grade='C'
        elif self.percentange>=40:
            self.grade='D'
        else:
            self.grade='E'
    def display(self):
        print('Roll No.: ',(self.rollNumber))
        print('Name: ',self.name)
        print('MarksList: ',(self.marksList))
        print('Stream: ',self.stream)
        print('Percenrage: ',(self.percentange))
        print('Grade: ',self.grade)
        print('Division: ',self.division)
        #return 'Roll No.: '+str(self.rollNumber)+'\nName: '+self.name+'\nMarksList: '+str(self.marksList)+'\nStream: '+self.stream+'\nPercenrage: '+str(self.percentange)+'\nGrade: '+self.grade+'\nDivision: '+self.division
s=Student(2660,"Rituraj",[],"CSE",0,'E',"1st")
print('-------------------------------------------\n',s,'\n-------------------------------------------\n')
s.setMarks()
print('-------------------------------------------\n',s,'\n-------------------------------------------\n')
s.Percantage()
s.gradeGen()
print('-------------------------------------------\n',s,'\n-------------------------------------------\n')

