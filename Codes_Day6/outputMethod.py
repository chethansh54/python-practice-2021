value = 10
variable = 100
a, b, c = 10, 20, 30

print("string")
print(value)
print(100)
print("string", value, variable, "string")
print("string\nstring\t", variable, "string \n data", value)
print("hi" + "hello")
print("hi" * 5)

# using separator

print(a, b, c)
print(a, b, c, sep=',')
print(a, b, c, sep=' ')
print(a, b, c, sep=':')
print(a, b, c, sep='')


# overriding ending character
print(" some data ")
print(" some data ", end='')
print(" some data ", end=',')
print(" some data ", end=' ')
