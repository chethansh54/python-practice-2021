data = {1: "Prateek", 2: "Chetan", 3: "Maruti"}

print(type(data))
print(data)

data = {"USN1": "Prateek", "USN2": "Chetan", "USN3": "Maruti"}

print(data)

print(data["USN1"])
print(data["USN2"])
print(data["USN3"])

data["USN3"] = "Raghav"
print(data)

studentDB = {

    "1": {
        "name": "Chetan",
        "hindi_marks": 90,
        "maths_marks": 100,
        "python_marks": 100
    },

    "2": {
        "name": "Prateek",
        "hindi_marks": 96,
        "maths_marks": 100,
        "python_marks": 100
    },

    "3": {
        "name": "Raghav",
        "hindi_marks": 99,
        "maths_marks": 89,
        "python_marks": 80
    }

}

print(studentDB["2"])
