setData = {10, 20, 90.4, "hello", True}

setData = frozenset(setData)

print(type(setData))
print(setData)

for data in setData:
    print(data)

