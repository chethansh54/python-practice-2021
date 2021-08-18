# if block

username = 'prateek'

a, b, c = 30, 20, 5

if username == 'pratek':
    print("Welcome to python classes, Prateek !")

if 10 >= 10:
    print("Ten is Greater/Equal")

if True:
    print("Its True")

# unreachable code
# Futile code
if False:
    print("Its False")

if (a > b) and (b > c):
    print(" A is greater than B")
    print(" B is greater than C")

if (a > b) or (b < c):
    print(" OR BLOCK : A is greater than B")
    print(" B is greater than C")

'''
its 
multi 
line
comment
'''

# username = input("Enter your username")
print(f"You Entered {username}")
print("Logging in ...")

if username == "python":
    print("Logged In Successfully ! ")

print("Thanks.")

# if-elif

username = ""
isIndian = True
hasVisa = hasPassport = False

if username:
    print("You are registered.")

elif isIndian:
    print("You can go and register first.")

elif hasVisa and hasPassport:
    print("Please connect us with your embassy.")

# if else

username = 's'

if username == 'python':
    print("Logged In")
else:
    print("Wrong username...")

# if elif else


username = "Prateek"
isIndian = True
hasVisa = hasPassport = True

if username:
    print("You are registered.")

elif isIndian:
    print("You can go and register first.")

elif hasVisa and hasPassport:
    print("Please connect us with your embassy.")

else:
    print("We are unable to process your request, kindly visit the customer care.")

# nested if else


username = None
password = "p1235"
email = None

if username:
    if password == 'p123':
        print(f"Welcome {username}, you are logged in.")
    else:
        print("Incorrect Password")
elif email:
    if password == 'p123':
        print(f"Welcome {email}... Please create an account userID and Password")
    else:
        print(f"Wrong password for your email id : {email}")

else:
    print("You are not eligible to use this system.")

#  one line if statements

if 10 > 5: a = True

print(f"a = {a}")


