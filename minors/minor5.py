'''
#1
globalVar = 10
def test():
    localVar = 20
    print('Inside function test : globalVar=', globalVar)
    print('Inside function test : localVar =', localVar)
test()
print('Outside function test : globalVar =', globalVar)
print('Outside function test : localVar =', localVar)
'''
'''
#2
globalVar = 10
def test():
    localVar = 20
    globalVar = 30
    print('Inside function test : globalVar =', globalVar)
    print('Inside function test : localVar =', localVar)
test()
print('Outside function test : globalVar =', globalVar)
'''
'''
#3
globalVar = 10
def test():
    global globalVar
    localVar = 20
    globalVar = 30
    print('Inside function test : globalVar =', globalVar)
    print('Inside function test : localVar =', localVar)
test()
print('Outside function test : globalVar =', globalVar)
'''
'''
#4
def test1():
    test1.a = 10
    def test2():
        test1.a = 8
        print('Inside function test2: ', test1.a)
    test2()
    print('Outside function test2 ', test1.a)
test1()
'''

'''
#5
a = 4
def f():
    a = 5
    def g():
        nonlocal a
        a = 10
        print('inside function g,', 'a = ', a)
        def h():
            nonlocal a
            a = 20
            print('inside function h,', 'a = ', a)
        h()
    g()
    print('inside function f,','a = ',a)
f()
'''

'''
x = 2
def test():
    x = x + 1
    print(x)
print(x)


x = 2
def test():
    global x
    x = x + 1
    print(x)
print(x)
'''
'''
#6
x = 2
def test():
    x = x + 1
    print(x)
print(x)
'''

#7
x = 2
def test():
    global x
    x = x + 1
    print(x)
print(x)
