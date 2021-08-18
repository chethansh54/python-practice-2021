# auth spoof

# database

uname = "prateek"
password = "p123"
mobile = "1234567890"

# system

print("AUTHENTICATION")
username = input("Enter your username : ")

if username == uname:
    pwd = input("Enter your password : ")
    if password == pwd:
        print("Logged In")
    else:
        print("Incorrect password")
else:
    print("Your username didnt match our database username.")
    mobilen = input("Enter your mobile number : ")
    if mobile == mobilen:
        print("Logged In Via OTP")
    else:
        print("You are not a registered user.")

        # register code

        name = input("Enter your full name : ")
        mobile = mobilen
        password = input("Enter a password : ")
        uname = name.split()[0].lower() + mobilen[6:]

        print("Your Details : ")
        print(f"Name: {name}\nmobile number:{mobile}\nusername:{uname}\npassword:{password}")
        print("You Can Login now.")

