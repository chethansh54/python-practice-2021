def hello(name):
    return "Hello " + name  # name variable is a formal parameter


print(hello("Rajesh"))  # "Rajesh" -> this value is an actual parameter

name = "Raghav"

print(hello(name))  # name-> this variable is an actual parameter


# Positional args

def sub(a, b):
    print(a - b)


sub(10, 20)
sub(20, 10)


def wish(name, msg):
    print(f"Hello, {name}, {msg}")


wish("Rajeev", "Good Night")

wish(name="Rajeev", msg="Good Morning")

wish(msg="Good Morning", name="Rajeev")

wish("Rajeev", msg="Good Morning")


def wish(name="guest"):
    print(f"Hello {name}")


wish("Chetan")  # Hello Chetan
wish()  # Hello guest


def sum(a=0, b=0):
    print(f"Total = {a + b}")


sum()  # 0
sum(a=10)  # 10
sum(a=10, b=20)  # 30
sum(b=20)  # 20
sum(20, 30)  # 50
sum(30)  # 30


def diff(a=0, b=0):
    print(f"Total = {a - b}")


diff()  # 0
diff(a=10)  # 10
diff(a=10, b=20)  # 30
diff(b=20)  # 20
diff(20, 30)  # 50
diff(30, 20)  # 50
diff(30)  # 30


# def wish(name="guest", msg):
#     print(f"{msg}, {name}")  # INVALID


def wish(*names):
    print(names)
    for name in names:
        print(f"Hello, {name}")


wish()
wish("Chetan")
wish("Chetan", "Elon")
wish("Chetan", "Elon", "Anil")
wish("Chetan", "Elon", "Anil", "Mukesh")


# overloading
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(f"Sum = {total}")


add()
add(10)
add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)
add(10, 20, 30, 40, 50)


# kwargs with variable length args
def display(**kwargs):
    sum = 0
    print(kwargs)
    for k, v in kwargs.items():
        print(f"keyword={k} , value = {v}")
        sum += v

    print(f"SUM = {sum}")


display()
display(a=10)
display(a=10, b=20)
display(a=10, b=20, c=30)
display(a=10, b=20, c=30, d=40)
display(a=10, b=20, c=30, d=40, e=50)


def sum(**kwargs):
    sum = 0
    for v in kwargs.values():
        sum += v
    print(sum)


sum()
sum(a=10)
sum(a=10, b=20)
sum(a=10, b=20, c=30)
sum(a=10, b=20, c=30, d=40)
sum(a=10, b=20, c=30, d=40, e=50)
