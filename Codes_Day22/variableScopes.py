a = 10  # global variable


def f1():
    a = 888  # local variable
    print(a)


def f2():
    print(a)  # this will print global variable 'a' value


#
# def f3():
#     print(a)  ERROR : Unresolved reference, because 'a' declared again below as local variable,
#     and is no more a global variable for f3() function
#     a=999
#     print(a)

f1()
f2()



