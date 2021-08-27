'''
Password Rules:

1. Minimum 8 characters
2. Minimum 1 upper case character
3. Minimum 1 special character
4. Must contain number
5. Must contain lower case
6. Must not contain anything similar to your username

'''
passwordData = input("Enter your password : ")
username = "prateek"
if len(passwordData) > 8:
    if username not in passwordData.lower():
        if passwordData.isascii():  # bug here, resolve it
            flag = False
            for s in passwordData:
                if s in ["$", "_", "@", "%", "*", "&", "!", "#", "^"]:
                    flag = True
                    break
            if flag:
                flag = False
                for s in passwordData:
                    if s.isupper():
                        flag = True
                        break
                if flag:
                    flag = False
                    for s in passwordData:
                        if s.islower():
                            flag = True
                            break

                    if flag:
                        print("Password successfully created.")
                        print("Password : ", passwordData)
                    else:
                        print("Your password must contain an lower case letter.")
                else:
                    print("Your password must contain an upper case letter.")

            else:
                print("Your password must contain some special characters.")

        else:
            print("Your password must contain alphabets and numbers")
    else:
        print("It must not have anything similar to your username.")

else:
    print("Your password must contain minimum 8 characters")
