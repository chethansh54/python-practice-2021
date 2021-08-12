setData = {10, 20, 90.4, "hello", True}

print(type(setData))
print(setData)

setData.add(1000)
print(setData)
setData.remove(1000)
print(setData)

# remove duplicates in a list

listData = [10, 10, 10, 20, 30, 40, 60, 60, 50, 50, 10, 10]
uniqueListData = set(listData)

print(type(listData))
print(listData)

print(type(uniqueListData))
print(uniqueListData)

uniqueListData = list(uniqueListData)
print(type(uniqueListData))
print(uniqueListData)
