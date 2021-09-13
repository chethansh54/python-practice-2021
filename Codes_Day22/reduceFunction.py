from functools import *

l = [10, 20, 30, 40, 50]

result = reduce(lambda x, y: x + y, l)  # sum of all list elements
print(result)  # 150

l = [10, 20, 30, 40, 50]
result = reduce(lambda x, y: x * y, l)  # product of all list elements
print(result)  # 12000000

# print the sum of all numbers from 1 to 100

result = reduce(lambda x, y: x + y, range(1, 101))
print(result)  # 5050
