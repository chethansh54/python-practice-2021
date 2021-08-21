str1 = "Python"

print(str1)
print(str1[0])
print(str1[4])
print(str1[-1])
print(str1[-2])
# print(str1[100])

# accept a string from keyboard display its character by index value

# str1 = input("Enter your string : ")

# way 1

i = 0  # iterator starting from 0

for x in str1:
    print(f"Character present at +ve index {i} and -ve index {i - len(str1)} is {x}")
    i += 1

# slicing

str1 = "Python"

print(str1[1:6:1])  # prints from index 1 to 5-1=4, 1->4
print(str1[::])
print(str1[:])  # start index:end index
print(str1[::-1])  # default start and end but step -1
print(str1[5:200:])  # default start and end but step -1
print(str1[5:200:100])  # default start and end but step -1
print(str1[5:-200:-100])  # default start and end but step -1
print(str1[2:])  # default start and end but step -1
print(str1[:-1:-1])  # backward direction with -1 end value is empty
print(str1[:0:1])  # fwd direction with 0 end value is empty
# print(str1[:0:0])  # slice step cannot be zero


# operations on string

str1 = "hello"
str2 = "world"
i = 3

print(str1 + str2)
print(str1 * i)

# len() function

print(f"Length of given string is {len(str1)}")

# print string characters

# way 2

i = 0  # iterator starting from 0
n = len(str1)

for i in range(n):
    print(f"Character {str1[i]} -> +ve index={i} | -ve index={i - n}")

# way 3


i = 0  # iterator starting from 0
n = len(str1)

print("Forward Direction : ")

while i < n:
    print(str1[i], end=' ')
    i += 1

print("\nBackward Direction : ")

i = -1  # iterator starting from 0

while i >= -n:
    print(str1[i], end=' ')
    i -= 1

print("\nForward Direction : ")
print(str1[::])
print("\nBackward Direction : ")
print(str1[::-1])

