# squaring a number without and with lambda

def squareIT(n):
    return n * n


print(squareIT(7))
print(squareIT(100))

squareIT = lambda n: n * n  # single lined function, lambda function

print(squareIT(7))
print(squareIT(100))

# lambda function to get MAX of 2 numbers

maxOfTwo = lambda a, b: a if a > b else b

print(f"Max of 10 and 20 is {maxOfTwo(10, 20)}")  # 20
print(f"Max of 100 and 50 is {maxOfTwo(100, 50)}")  # 100
