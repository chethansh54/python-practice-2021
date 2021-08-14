# arithmetic

print("Arithmetic Operators")
a = 10
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

print("/ and // Operators")

a = 10.5
b = 2

print(a / b)
print(a // b)

a = 10.5
b = 2.5

print(a / b)
print(a // b)

# overloading of operators + and *
print("Overloading of Operators")

str1 = "Hello"
str2 = "World"

print(str1 + str2)

print(str1 * 10)

# relational Operators

a = 10
b = 20

print("Relational Operators")

print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)

print("Operator Chaining ")

print(a < b < 30)
print(a < b < 30 > 50)
print(a == b == 30 == 50)
print(a != b != 30 != 50)

# logical operators

print("Logical Operators ")

print(True and True)
print(True and False)
print(True or False)
print(not False)

a = ""
b = "hello"

print(a or b)
print(a and b)

print("not" or 0)
print(10 and 0)

# bit wise operators

print("Bitwise Operators")

a = 10
b = 2

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(~b)
print(a << b)
print(a >> b)
print(10 >> 1)  # as good as 10//4
print(10 // 4)

# assignment
print("Assignment Operator")

a = 10
b = 30
c = 20

print(a)
print(b)
print(c)

a -= 10
b += 10
c *= 5

print(a)
print(b)
print(c)

# ternary

strValue = "Tru"

var1 = True if strValue == "True" else False

print(strValue)
print(var1)

a = 10
b = 20

maxNumber = a if a > b else b
minNumber = a if a < b else b

print(maxNumber)
print(minNumber)

# minimum of 3 numbers

a = 20
b = 10
c = 5

# ternary operator nesting
min = a if a < b and a < c else b if b < c else c

print(min)

# special operators

print("Special Operators")

a = 10
b = 10
c = 20

print("ID OF a: ", id(a))
print("ID OF b: ", id(b))
print("ID OF c: ", id(c))

print(a is b)
print(a is not c)
print(a is c)

myList = [10, 20, 30]

print(myList)
print(10 in myList)
print(100 not in myList)

str1 = "Hello i am from RV College"

print("College" in str1)

if 10 in myList:
    print("10 is part of mylist")

# precendence

print("PRECEDENCE")
a = 30
b = 20
c = 10
d = 5

print((a + b) * c / d)
print((a + b) * (c / d))
print(a + (b * c) / d)

print(3 / 2 * 4 + 3 + (10 / 5) ** 3 - 2)

# math module

print("math module")

import math

print(math.sqrt(16))
print(math.ceil(10.5677))
print(math.floor(10.5677))
print(math.pow(10, 3))
print(math.factorial(5))
print(math.fabs(-10.7887))
print(math.gcd(10, 8))
print(math.e)
print(math.pi)

from math import pi

print(pi)
