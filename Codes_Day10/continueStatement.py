for i in range(10):
    if i == 7:
        continue
    print(i)

print("Done, Out of the for loop")

# continue in nested loops

for k in range(10):
    print("OUTER LOOP k=", k)
    for i in range(10):
        if i == 7:
            continue
        print(i)

# the continue , skips the statment in loop where it is present in, it wont skip anything in the parent loop

print("Done, Out of the for loop")

# get odd numbers in a list

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numList:
    if num % 2 == 0:
        continue
    print("Odd Number = ", num)


