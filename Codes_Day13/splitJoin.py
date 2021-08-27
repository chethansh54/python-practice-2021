# split 

str1 = "Hello how are you doing ?"

strList = str1.split()
print(str1)
print(strList)
print(f"there are {len(strList)} words in str1")

str1 = "Hello,how,are,you,doing ?"
print(strList)
strList = str1.split(",")
print(strList)

# join

str2 = " ".join(strList)
str2 = ",".join(strList)
print(str2)

str1 = "18-08-2021"
dateList = str1.split("-")
print(dateList)
print(f"Today's day is {dateList[0]} | Month is {dateList[1]} | Year is {dateList[2]}")



