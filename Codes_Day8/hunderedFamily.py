# program to check if a given number falls between 1 - 100


numberValue = int(input("Enter the number : "))

# if numberValue >= 1 and numberValue <= 100:
# short cut 1<=x<=100

if 1 <= numberValue <= 100:
    print(f"The number {numberValue} is a part of 100 Family.")

else:
    print(f"{numberValue} is not a part of 100 Family.")
