# for loop

name = "Python Programming"
i = 0
for character in name:
    # print(character, end=",")
    print(f"index of {character} = {i}")
    i += 1

print()

myList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, "hello", "Hi", True]

# size of list is n, then loop will run from 0 to n-1 (as per indexing)

for element in myList:
    print(element)

for i in range(10):
    print(i)

# find sum of 1st 10 numbers
# [m,n)

sum = 0
for i in range(1, 11):
    sum += i

print(f"Sum of 1st 10 natural numbers is {sum}")

for i in range(0, 11, 2):
    print(i)

sum=0

# sum of last 10 2 digit numbers
for i in range(99, 89, -1):
    print(i)
    sum += i

print(f"Sum of last 10 2 digit numbers is {sum}")



sheet1 = [1, 2, 3]
sheet2 = [30, 10, 5, "A", "B", "C"]

products = {"a": "A", "b": "A", "c": "B", "d": "C"}

marketShare = dict()

for k, v in products.items():
    if v == "A":
        marketShare[k] = ((sheet2[0] + sheet2[1] + sheet2[2]) * sheet1[0])

    elif v == "B":
        marketShare[k] = ((sheet2[0] + sheet2[1] + sheet2[2]) * sheet1[1])

    elif v == "C":
        marketShare[k] = ((sheet2[0] + sheet2[1] + sheet2[2]) * sheet1[2])

print(products)
print(marketShare)


