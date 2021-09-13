# make a list of doubled numbers from a given list of numbers.

# without lambda

l = [1, 2, 3, 4, 5]


def doubleIt(x):
    return 2 * x


l1 = list(map(doubleIt, l))

print(l1)  # [2,4,6,8,10]

# with lambda
l = [1, 2, 3, 4, 5]

l1 = list(map(lambda x: 2 * x, l))

print(l1)  # [2,4,6,8,10]

# =======================================================================
# Prepare a list of squared numbers from a given input list of numbers

# without lambda

l = [1, 2, 3, 4, 5]


def squareIt(x):
    return x * x


l1 = list(map(squareIt, l))

print(l1)  # [1,4,9,16,25]

# With lambda

l = [1, 2, 3, 4, 5]

l1 = list(map(lambda x: x * x, l))

print(l1)  # [1,4,9,16,25]

# ====================================================================================

# map() on multiple sequences


l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

l3 = list(map(lambda x, y: x * y, l1, l2))  # prepare a product list of corresponding elements of l1 and l2

print(l3)  # [6,14,24,36,50]
