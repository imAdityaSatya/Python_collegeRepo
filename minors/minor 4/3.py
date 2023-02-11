import pdb
pdb.set_trace()

def main():
    totalMarks = 0
    i = 0
    while True:
        marks = input("Enter marks for subject "+str(i+1)+":")
        if marks == '':
            break
        marks = int(marks)
        if marks<0 or marks>100:
            print("Invalid marks")
            continue
        i += 1
        totalMarks += marks
    percentage = totalMarks//i
    print("Total marks",int(totalMarks))
    print("Percentage",round(percentage,2))

if __name__ == '__main__':
    main()


# give 91,91,65
# gives 82% but correct value is 82.3333
