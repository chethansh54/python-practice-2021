x = 1
sum = 0

# # infinite loop
# while x < 11:
#     sum += x


# infinite loop
while x < 11:
    sum += x
    x += 1

print(f"Sum of 1st 10 natural numbers is {sum}")

# mini bank system

account = 1000
username = "prateek"
password = "p123"

qFlag = True

while qFlag:
    print("Welcome to BANK")
    print("Login")
    uname = input("Enter your username  : ")
    passw = input("Enter your password : ")

    if uname == username and password == passw:
        print("Logged in")

        while qFlag:
            print("Choose an Option : ")
            option = int(input("1.Deposit Money\n2.Check Balance\n3.Withdraw Money\n4.Logout\n"))

            if option == 1:
                amt = int(input("Enter amount : "))
                account += amt
                print("Deposit Done.")
            elif option == 2:
                print(f"Your Account Balance is Rs {account}/-")
            elif option == 3:
                amt = int(input("Enter amount : "))
                if amt <= account:
                    account -= amt
                    print(f"Rs {amt} was withdrawn from your account.")
                else:
                    print("Insufficient Funds")

                print(f"Your Available Account Balance is Rs {account}/-")
            elif option == 4:
                print("Thank you for banking with us. You're now logged out.")
                qFlag = False
            else:
                print("YOU'VE ENTERED AN INCORRECT OPTION, PLEASE ENTER ANY OPTION FROM 1-4")

    else:
        print("The login credentials are incorrect, please check and try again.")
