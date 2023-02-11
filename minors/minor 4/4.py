import pdb
pdb.set_trace()

def isLeapYear(year):
    return year%400 == 0 or year%100 == 0 and year%4 == 0

def main():
    year = int(input("Enter year: "))
    value = isLeapYear(year)
    if value:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")

if __name__ == '__main__':
    main()
