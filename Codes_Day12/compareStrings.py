# comparison
str1 = "hello"
str2 = "hello"
str3 = "hey"

if str1 < str2:
    print("Str1 is less")

if str1 > str2:
    print("Str2 is less")

if str1 == str3:
    print("Both strings are equal")

if str1 != str2:
    print("Not Equal")

# removing spaces

city = "     bandra       "
print(city)
lcity = city.lstrip()
rcity = city.rstrip()
print(lcity)
print(rcity)
city = "     bandra       "
print(city)
city = city.strip()
print(city)

# find(), rfind()
s = "Learning python is very easy"
print(s.find("python"))  # 9
print(s.find("Python"))  # -1
print(s.rfind("very"))  # 19
print(s.rfind("very", 10, 30))  # 19

# index(), rindex()
s = "Learning python is very easy"
print(s.index("python"))  # 9
# print(s.index("Python"))  # ValueError: substring not found
# print(s.index("Python"), 5, 20)  # ValueError: substring not found
print(s.rindex("very"))  # 19
print(s.rindex("very", 5, 30))  # 19

# Display all positions of substring in the main string

strValue = input("Enter the string pattern : ")
substrValue = input("Enter the substring/character pattern to search : ")

flag = False
position = -1

strSize = len(strValue)

while True:
    position = strValue.find(substrValue, position + 1, strSize)
    if position == -1:
        break
    print(f"Found at position {position}")
    flag = True

if flag == False:
    print("Substring Not Found.")

# counting

strValue = "aaaaaabbbbaaaabababababab"
print(f"a has repeated {strValue.count('a')} times")
print(f"a has repeated {strValue.count('a', 10, 20)} times")

# replace

s = "python is easy"
s1 = s.replace("easy", "hard")
print(s)
print(s1)

country = "united states of america"
country_code = country.replace(" ", "_")

print(country)
print(country_code)
