a = 10
b = 20
c = 30
d = 40
e = 50

t = a, b, c, d, e
print(t)  # (10,20,30,40,50) packing

f, g, h, i, j = t  # unpacking

print(f, g, h, i, j)

# tuple comprehension, actually generator functionality

t = (x ** 2 for x in range(1, 5))
print(type(t))  # generator object
print(t)  # 1 4 9 16 25 (line by line)

for i in t:
    print(i)

# take tuple of numbers and calculate sum and avg

t = eval(input("Enter the numbers : "))
print(t)
print(type(t))
l = len(t)

sum = 0

for x in t:
    sum += x

print(f"Sum = {sum}")
print(f"Avg = {sum/l}")

