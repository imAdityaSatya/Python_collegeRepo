'''import Flask, render_template
app = Flask(__name__)

def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

def say_hello():
    page = render_template('index.html')
    return page

def show_policy():
    page = render_template('privacy.html')
    return page


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
'''

def binarySearch(lst, searchValue):
    low, high = 0, len(lst)-1
    while low <= high:
        mid = int((low+high)/2)
        if lst[mid] == searchValue:
            return mid
        elif searchValue < lst[mid]:
            high = mid-1
        else:
            low = mid+1
            return None


def isSorted(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True


def main():
    lst = eval(input('Enter a sorted list (ascending order) :'))
    if not(isSorted(lst)):
        print('Given list is not sorted')
    else:
        searchVal = eval(input('Enter the value to be searched :'))
        print(searchVal, 'found at index', binarySearch(lst, searchVal))


if __name__ == '__main__':
    main()
