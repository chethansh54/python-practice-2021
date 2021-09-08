# remove duplicate values from user input from keyboard

data = eval(input("Enter the data : "))
dataSet = set(data)
dataSet = list(dataSet)
print(f"Input Data : {data}")
print(f"Output Data : {dataSet}")

# normal algorithm

data = eval(input("Enter the data : "))
dataList = []

for item in data:
    if item not in dataList:
        dataList.append(item)

print(data)
print(dataList)
