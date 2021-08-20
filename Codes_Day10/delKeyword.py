var1 = 10
var2 = 20

print(var1)
print(var2)

# deleting var1

del var1

# print(var1) #error

str1 = "hello"

print(str1)
print(str1[0])

del str1  # deletes the str1

# print(str1)

# del str1[0] # error


myList = [10, 20, 30]

print(myList)
print(myList[0])

del myList[0]  # deletes 10 from myList

print(myList) # list is mutable so we can delete the items as well
