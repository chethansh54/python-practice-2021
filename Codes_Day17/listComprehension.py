# generate a list of square numbers from n= 1 to 5

myList = [x * x for x in range(1, 6)]

print(myList)

myList = [2 ** x for x in range(1, 6)]
print(myList)

myList = [x for x in range(1, 101) if x % 2 == 0]  # list of even numbers
print(myList)

myList = [x for x in range(1, 101) if x % 2 != 0]  # list of odd numbers
print(myList)

words = ["Argentina", "USA", "India", "Australia", "Japan"]
print(words)
eligibleCountries = ["USA", "India", "Japan"]
print(eligibleCountries)
countryCodeList = [word[0] for word in words]
print(countryCodeList)
countryCodeList = [word[0:3] for word in words]
print(countryCodeList)

countryCodeList = [word[0:3] for word in words if word in eligibleCountries]

print(countryCodeList)

myList = [letter for letter in "Argentina" if letter.lower() in ['a', 'e', 'i', 'o', 'u']]
# fetch all the vowels in given string

print(myList)

# in a given string or a line of text, get the words and their letter  count
# input: hello my name is chetan
# output : [ ["hello",5], ["my",2], ["name",4], ["is",2],["chetan",6]]

line = "the quick brown fox jumped over the lazy dog"

words = line.split()

myList = [[word, len(word)] for word in words]

print(line)
print(words)
print(myList)
