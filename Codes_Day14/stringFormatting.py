name = "Karan"
salary = 90000
age = 35

print("{} {} {}".format(name, salary, age))
print("{0} {1} {2}\n {0} {2} {1}".format(name, salary, age))
print("{x} {y} {z}\n {x} {z} {y}".format(z=name, y=salary, x=age))

# numbers formatting

print("The number is {}".format(123))
print("The number is {:d}".format(123))  # 123
print("The number is {:5d}".format(123))  # 123
print("The number is {:05d}".format(123))  # 00123

print("The number is {}".format(123.4567))
print("The number is {:f}".format(123.4567))  # 123.456700
print("The number is {:8.3f}".format(123.4567))  # 123.457
print("The number is {:08.3f}".format(123.4567))  # 0123.457
print("The number is {:08.3f}".format(7878787871.45))  # 7878787871.450

print("{0:b}".format(7))  # 111
print("{0:o}".format(123))  # 173
print("{0:x}".format(154))  # 9a
print("{0:X}".format(154))  # 9A

print("{:+d}".format(123))
print("{:+d}".format(-123))  # -123
print("{:-d}".format(-123))
print("{:+f}".format(123.8765))
print("{:-f}".format(-123.7986))

print()
print()

# alignment
print("{:5d}".format(12))
print("{:<5d}".format(12))
print("{:<05d}".format(12))
print("{:>5d}".format(12))
print("{:^6d}".format(12))
print("{:=5d}".format(-12))
print("{:^10.3f}".format(12.1234456677))
print("{:=8.3f}".format(-12.1234456677))

# string formatting
print()
print()
print()
print()
print("{:5}".format("rat"))
print("{:>5}".format("rat"))
print("{:<5}".format("rat"))
print("{:^5}".format("rat"))
print("{:*^25}".format("Welcome to Function"))

# default alignment is left, for strings


# truncate
print()
print()
print()
print()
print("{:.4}".format("international"))
print("{:5.3}".format("international"))
print("{:>5.3}".format("international"))
print("{:^5.3}".format("international"))
print("{:*^5.3}".format("international"))

# formatting dictionary data
person = {'age': 48, 'name': 'Karan'}
print("{p[name]}'s age is {p[age]}".format(p=person))

print("{name}'s age is {age}".format(**person))


class Person:
    age = 48
    name = 'karan'


print("{p.name}'s age is {p.age}".format(p=Person()))

stringData = "{:{fill}{align}{width}}"
print(stringData.format('cat', fill='*', align='^', width=5))
print(stringData.format('cat', fill='_', align='^', width=6))
print(stringData.format('cat', fill='*', align='<', width=5))
print(stringData.format('cat', fill='*', align='>', width=6))

num = "{:{align}{width}.{precision}f}"

print(num.format(123.12345, align='>', width=8, precision=2))

#date formatting

print()
print()
print()

import datetime
date = datetime.datetime.now()
print("Current Time is  {:%d/%m/%Y %H:%M:%S}".format(date))
print("Current Time is  {:%d-%m-%Y %H:%M:%S}".format(date))
print("Current Time is  {:%d%m%Y}".format(date))
print("Current Time is  {:%d%m%y}".format(date))
print("Current Time is  {:%A %b %y}".format(date))
print("Current Time is  {:%d %B %y}".format(date))
print("Current Time is  {:%d:%m:%Y}".format(date))



