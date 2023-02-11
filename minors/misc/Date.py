'''
def __eq__(self,other):
    if isinstance(other,date):
        if self.d==oth.d and self.m==other.m and self.y==self.y:
            return True
        else:
            return False

d1 = date(18,1,2022)
d2 = date(18,1,2022)
print("Date1 equals Date2:",d1==d2)
'''
a=12
def f():
    global a
    a=a-4
    print(a)
f()
