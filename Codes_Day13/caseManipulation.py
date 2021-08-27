str1 = "learning python is very easy"
print(str1)
print(str1.upper())
print(str1.lower())
print(str1.swapcase())
print(str1.title())
print(str1.capitalize())

# format text data
str1 = "learning python is very easy.you need daily practice.good luck"

dataList = str1.split(".")
print(dataList)

str2 = ""
dataList2 = []

for d in dataList:
    str2 = str2 + d.capitalize() + "."

for d in dataList:
    dataList2.append(d.capitalize())

print(dataList2)
str2 = ".".join(dataList2)
print(str2)
