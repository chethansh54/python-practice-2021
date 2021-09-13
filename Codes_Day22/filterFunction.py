# filter only even numbers from a given list by using filter()

# Without lambda function

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


l = [0, 5, 10, 15, 20, 25, 30]

l1 = list(filter(isEven, l))

print(l1)  # [0,10,20,30]

# With Lambda Function:


l = [0, 5, 10, 15, 20, 25, 30]

l1 = list(filter(lambda x: x % 2 == 0, l))
print(l1)  # [0,10,20,30]

# get list of odd numbers
l1 = list(filter(lambda x: x % 2 != 0, l))
print(l1)
