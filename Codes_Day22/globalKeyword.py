a = 10


def f1():
    global a  # considers the 'a' which is declared as a=10 globally
    a = 999  # this value is updated in 'a' and the old value 10 is replaced.
    print(a)


def f2():
    print(a)


f1()
f2()
