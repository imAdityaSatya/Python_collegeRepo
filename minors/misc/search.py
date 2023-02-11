'''
def search(list, n, key):   
    for i in range(0, n):  
        if list[i] == key:  
            return i  
    return -1
'''

def search(list, low, high, s):
    low= 0
    high= len(list)-1
    if low <= high:
        mid= int((low+high)/2)
        if list[mid] > s:
            return search(list, low, mid-1, s)
        elif list[mid]< s:
            return search(list, mid+1, high, s)
        else:
            return mid
    return None

list= [1,2,3,4]
s=4
print("found at index",search(list,1,4,s))

'''
def search(list, n, s):
    n=len(list)
    low = 0
    high = n
    while low <= high:
        mid = low + (high - low) // 2
        if (s == list[mid]):
            return mid
        elif (s < list[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return None
list= [4,3,2,1,0]
s=1
print(search(list,4,s))
'''




