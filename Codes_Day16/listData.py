# ordering list elements

myList = [10, 50, 30, 40]

myList.reverse()

print(myList)

# sort()


myList = [30, 50, 10, 20, 45]

myList.sort()

print(myList)  # [10,20,30,40,50]

myList = ["dog", "cat", "rat", "mat"]

myList.sort()

print(myList)  # ["cat","dog","mat","rat"]

myList.sort(reverse=True)

print(myList)  # ["rat","mat","dog","cat"]

# aliasing

x = [10, 20, 30]
print(f"location of x in memory = {id(x)}")
y = x
print(f"location of y in memory = {id(y)}")

y[0] = 100

print(f"Value of y={y} | Value of x={x}")

# cloning

# slicing

x = [10, 20, 30]

y = x[:]

y[0] = 100

print(f"location of x in memory = {id(x)}")
print(f"location of y in memory = {id(y)}")
print(f"Value of y={y} | Value of x={x}")

x = [10, 20, 30]

y = x.copy()

y[0] = 100

print(f"location of x in memory = {id(x)}")
print(f"location of y in memory = {id(y)}")
print(f"Value of y={y} | Value of x={x}")

# comparison

x = ["Dog", "Cat", "Rat"]
y = ["Dog", "Cat", "Rat"]
z = ["DOG", "CAT", "RAT"]

print(x == y)  # True
print(x == z)  # False
print(x != z)  # True

x = [50, 20, 30]
y = [40, 50, 60, 100, 200]
print(x > y)  # True
print(x >= y)  # True
print(x < y)  # False
print(x <= y)  # False

# membership

n = [10, 20, 30, 40]

if 30 in n:
    print(30)  # no output

if 30 not in n:
    print(30)  # no output

print(30 in n)
print(30 not in n)

# clear

n = [10, 20, 30, 40]
print(n)
n.clear()
print(n)

# nested list and matrix

n = [10, 30, 40, [50, 60, 70]]
print(n)
print(n[3][0])

matrix_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix_3[0][0])  # first row, first element, 1
print(matrix_3[0][1])  # first row, second element, 2

for r in matrix_3:
    print(r)

for r in range(len(matrix_3)):
    for c in range(len(matrix_3)):
        print(matrix_3[r][c], end=' ')
    print()
