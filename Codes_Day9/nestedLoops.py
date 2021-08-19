for i in range(10):
    for j in range(10):
        print(f"i = {i}     j={j}")

nameList = ["Hari", "Gopal", "Shyam", "Ghanshyam"]

for name in nameList:
    for j in range(10):
        print(f"Order of {name}     j={j}")

# bubble sort

data = [6, 4, 5, 7, 8, 9]

n = len(data)

print(f"Before Sorting : data = {data}")

for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(f"After Sorting : data = {data}")
