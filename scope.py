a = [1,2,3]

def f1():
    a[0] = 10
    print(a)

def f2():
    a = 50
    print(a)

f1()
f2()
print(a)