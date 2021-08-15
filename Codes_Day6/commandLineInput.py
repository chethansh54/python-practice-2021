import sys

print(sys.argv)
print(type(sys.argv))
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

# activity
# add 3 numbers from command line input

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

sum = num1 + num2 + num3

print(" The Sum of given numbers = ", sum)
