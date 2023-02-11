'''
Year= int(input())
if (Year % 4) == 0:
   if (Year % 100) == 0:
       if (Year % 400) == 0:
           print("{0} is a leap year".format(Year))
       else:
           print("{0} is not a leap year".format(Year))
   else:
       print("{0} is a leap year".format(Year))
else:
   print("{0} is not a leap year".format(Year))



def main():
    year = int(input("Enter year: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")

if __name__ == "__main__":
    main()

a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0, len(a))]
print(b)
[1, 3, 6, 10]
'''
'''
import copy
a=[10,23,56,[78]]
b=copy.deepcopy(a)
a[3][0]=95
a[1]=34
print(b)
'''

class subset:
    def subset(self, s):
        return self.subsets([], sorted(s))
    def subsets(self, tmp, s):
        if s:
            return self.subsets(tmp, s[1:]) + self.subsets(tmp + [s[0]], s[1:])
        return [tmp]
print(subset().subset([4,5,6]))
