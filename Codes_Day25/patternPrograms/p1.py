n = int(input("Enter the size : "))

for i in range(n):
    for j in range(n):
        print("*", end='')
    print()

# alternate way

for i in range(1, n + 1):
    print("*" * n)


