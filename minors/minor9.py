'''
class demo():
    def __repr__(self):
        return '__repr__built-in fun called'
    def __str__(self):
        return '__str__built-in fun called'
s=demo()
print(s)
'''
'''
f= open('file1','r')
f.readlines(-1)
f.close()
'''

'''
class s:
    def __init__(self, r, g):
        self.r=r
        self.g=g
    def display(self):
        print(self.r," , ", self.g)
s1=s(34,'S')
s1.age=7
print(hasattr(s1,'age'))
'''
'''
def main():
    m=110
    try:
        if m<0 or m>100:
            raise ValueError('err')
    except:
        pass
    finally:
        print('bye')
    print('exep hndl')
if __name__=='__main__':
    main()
'''
'''
f=None
for i in range(5):
    with open('data.txt', 'w') as f:
        if i>2:
            break
print(f.closed)
'''
'''
import pickle
f= open('Data.txt', 'rb')
d= pickle.load(f)
f.end()
'''

def f(n):
    z= int(n)
    if n>2:
        print('Completed')
    else:
        print(z/(n-z))
def main():
    n= int(input("Enter n: "))
    f(n)
main()

