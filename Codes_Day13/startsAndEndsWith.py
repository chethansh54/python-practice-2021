str1 = "Hello Hi Great"

print(str1.startswith("Hello"))
print(str1.startswith("hello"))
print(str1.startswith("H"))
print(str1.endswith("Great"))
print(str1.endswith("t"))
print(str1.endswith("great"))

collegesList = [
    "College of Engineering", "Indian institute of technology", "all india medical college",
    "national institute of Technology"]

# get the list of all engineering colleges

for college in collegesList:
    if college.lower().endswith("technology") or college.lower().endswith("engineering"):
        print(college)
