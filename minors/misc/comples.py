import math as m
class ComplexNumbers(object):

    def __init__(self, real, img=0):
        self.real= real
        self.img= img
        print(self.real+self.img)

    def __add__(self, other):
        return ComplexNumbers(self.real+other.real, self.img+other.img)

    def __sub__(self, other):
        return ComplexNumbers(self.real-other.real, self.img-other.img)

    
    def __mul__(self, other):
        return ComplexNumbers(self.real*other.real - self.img*other.img,self.img*other.real + self.real*other.img)

    def __div__(self, other):
        r= other.real**2 + other.imag**2
        return ComplexNumbers((self.real*other.real-self.img*other.img)/r,(self.img*other.real+self.real*other.img)/r)
                    
