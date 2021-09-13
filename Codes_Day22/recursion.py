# functions which call themselves till a final value is calculated, are recursive functions

def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


print(f"Factorial of 4 is {factorial(4)}")
print(f"Factorial of 5 is {factorial(5)}")  # 120

