# built in functions

x = 10
print(f"x is at {id(x)}")  # id() is a function which returns the address location of variable
print(f"x is at {type(x)}")  # id() is a function which returns the data type of the variable

print("Print() itself is a function, to print data on screen.")


# user defined

# function definition
def hello():
    print("hello")


hello()  # function call


# function with parameters

def hello(name):
    print(f"Hello {name}")


hello("Raghav")
hello("Monty")
hello("XAE129D")


# function with return

def sumOfTwo(a, b):
    return (a + b)


s = sumOfTwo(10, 20)
print(s)
print(f"Sum of 10 and 20 is {sumOfTwo(10, 20)}")


# return multiple values

def arithmetic(a, b):
    print("Calculating...")
    sum = a + b
    diff = a - b
    pr = a * b
    div = a / b
    return sum, diff, pr, div


s, d, pr, div = arithmetic(100, 5) # packing unpacking of data

print(f"Sum={s}\ndifference={d}\nproduct={pr}\ndivision={div}")
