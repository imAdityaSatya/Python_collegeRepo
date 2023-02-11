#Selection sort
def selectionSort(list):
    n= len(list)
    for i in range(0,n-1):
        x=i
        for j in range(i+1, len(list)):
            if list[j]<list[x]:
                x=j
        if x!=i:
            list[x],list[i]=list[i],list[x]
        print(list)


# Bubble sort
def bubbleSort(list):
    n= len(list)
    for i in range(n-1):
        swap=False
        for j in range(0, n-i-1):
            if list[j]>list[j + 1]:
                swap=True
                list[j], list[j + 1] = list[j + 1], list[j]
        if swap==False:
            break
        
# Insertion sort
def insertionSort(list):
    for i in range(len(list)):
        tmp= list[i]
        j= i-1
        while j>=0 and tmp<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=tmp
        
