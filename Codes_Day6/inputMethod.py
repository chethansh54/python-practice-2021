# input() ways

print("Enter your name : ")
name = input()

print(type(name))
print(name)

mathsMarks = input("Enter your maths marks : ")
print(type(mathsMarks))
print(mathsMarks)

mathsMarks = int(mathsMarks)

scienceMarks = int(input("Enter your science marks : "))
print(type(scienceMarks))
print(scienceMarks)

# multiple inputs

a, b, c, d = [int(x) for x in input("Enter 4 numbers : ").split()]  # [1,2,3,4]

print(a)
print(b)
print(c)
print(d)

# eval()

myList = eval(input("Enter your list elements : "))
print(type(myList))
print(myList)


evaluationValue = eval(input("Enter your expression : "))
print(type(evaluationValue))
print(evaluationValue)
