myList = [10, 20, 30, 50]
print(myList)
print(myList[0])
print(myList[0:3])
print(myList[3:0:-1])

# nested list
myList = [10, 20, [30, 40, 50], [90, [99, 98, 97]], 100]

print(myList[2])  # [30,40,50]
print(myList[2][0])  # 30
print(myList[3][1][1])  # 98

print(myList[3][1][-1])  # 97

print(myList[2][2:0:-1])

# traversing

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0

while i < len(myList):
    print(myList[i] * 10)
    # do any operation on myList
    i += 1

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# way 1
for element in myList:
    print(element * 10)

# way 2

for x in range(len(myList)):
    print(myList[x] * 100)

# list methods

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 2]

print(f"There are {len(myList)} items in myList")

print(myList.count(2))

myList.append(100)
myList.append(200)

print("After appending list : ")
print(myList)

myList.insert(0, 500)
myList.insert(2, 500)
myList.insert(-1, 500)
print("After inserting list : ")
print(myList)

myList1 = [10, 20]
myList2 = [30, 40]

myList1.extend(myList2)  # [10,20,30,40]

print("Extended list : ", myList1)

myList1.extend("Hello")  # [10,20,30,40,"H","e","l","l","o"]

print("Extended list : ", myList1)

data = ["hello", "world"]

myList1.extend(data)  # [10,20,30,40,"hello","world"]

print("Extended list : ", myList1)

# remove

myList1.remove('H')
myList1.remove('e')
myList1.remove('l')

print("After removing list data : ", myList1)

myList1.pop(4)
print(myList1)
myList1.pop(5)
print(myList1)
myList1.pop()


print("After pop() list data : ", myList1)


