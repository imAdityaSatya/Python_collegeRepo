class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self,oth):
        x= self.x+oth.x
        y= self.y+oth.y
        return Point(x,y)

    def __str__(self):
        return str((self.x, self.y))

p1= Point(1,2)
p2= Point(3,4)
print(p1)
print(p2)
#print(p1+p2)
p3=p1+p2
print(p3)
        
    
