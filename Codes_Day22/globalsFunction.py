a = 10
b = 20
c = 9000


def f1():
    a = 90
    print(a)  # local variable 'a' value is printed, 90
    print(globals()['a'])  # global variable 'a' value is printed, 10

f1()
print(globals())  # see what's stored in globals()
