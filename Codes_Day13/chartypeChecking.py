str1 = "hello"

print(str1.isalnum())

print("Prateek1234".isalnum())
print("Prateek1234".isalpha())
print("Prateek".isalpha())
print("Prateek1234".isdigit())
print("1234".isdigit())
print("Hello Guys".istitle())
print("     ".isspace())

# remove multiple spaces in data

dataText = "Hello guys its nice        meeting you  all  here at the python  coding     contest."
dataTextList = dataText.split()
print(f"raw data => {dataText}")
dataFormattedList = []

for data in dataTextList:
    if not data.isspace():
        dataFormattedList.append(data)

print(f"formatted data => {' '.join(dataFormattedList)} ")

