for i in range(10):
    if i == 7:
        break
    print(i)

print("Done, Out of the for loop")

# break in nested loops

for k in range(10):
    print("OUTER LOOP k=", k)
    for i in range(10):
        if i == 7:
            break
        print(i)

# the break , stops the for loop where it is present in, it wont break the parent loop

print("Done, Out of the for loop")
