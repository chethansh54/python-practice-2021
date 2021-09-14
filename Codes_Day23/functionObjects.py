def f1():
    print("Hello")


print(f1)  # prints f1 function's reference
print(id(f1))


def wish(name):
    print(f"Hi {name}, good morning")


greet = wish

wish("Raju")  # Hi Raju, good morning
greet("Raju")  # Hi Raju, good morning

print(id(wish))
print(id(greet))

del wish

# wish("Pavan") # cant access because wish is deleted

greet("Pavan")


# NESTED FUNCTIONS
def outer():
    print("This is outer function")

    def inner():
        print("This is inner function")

    print("Outer function is now calling inner() function")

    inner()


outer()


def outer():
    print("This is outer function")

    def inner():
        print("This is inner function")

    print("Outer function is now calling inner() function")

    return inner


f1 = outer()
f1()

f1 = outer
print(f"{f1}")
f1 = outer()
print(f"{f1}")
