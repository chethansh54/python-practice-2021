d = {}
print(d)

d = dict()
print(d)

d[100] = "Maruti"

print(d)
d = {"model": 2018, "brand": "maruti", "variant": "Baleno zDi"}
print(d)

# accessing

# print(d[100]) # KeyError
print(d["model"])
print(d["brand"])
print(d["variant"])

# checking keys

if 100 in d:
    print(d[100])

if "model" in d:
    print(d["model"])

d = {"model": 2018, "brand": "maruti", "variant": "Baleno zDi"}

d["brand"] = "Tata"
d["variant"] = "Nexon"

print(d)

del d["model"]
print(d)

d.clear()
print(d)

# del d
# print(d)


# dict()

d = dict()
print(d)

d = dict({1: 100, 2: 200, 3: 300})
print(d)

d = dict([(100, "Maruti"), (200, "Tata"), (300, "Merceded")])
print(d)

print(f"Dictionary has {len(d)} elements ")

print(d.get(100))
del d[100]
print(d.get(100, "Suzuki"))

d[100] = "Maruti"
print(d.pop(100))
print(d)

d.popitem()
print(d)
d.popitem()
print(d)
# d.popitem()
# print(d)


# keys,values,items

d = dict([(100, "Maruti"), (200, "Tata"), (300, "Merceded")])
print(d.keys())
print(d.values())
print(d.items())

for k in d.keys():
    print(k, end=",")
print()

for v in d.values():
    print(v, end=",")
print()
for k, v in d.items():
    print(k, "===>", v)

d1 = d.copy()

print(d1, id(d1))
print(d, id(d))

d = dict([(100, "Maruti"), (200, "Tata"), (300, "Merceded")])

print(d.setdefault(100, "Suzuki"))
print(d)
print(d.setdefault(400, "Suzuki"))
print(d)

d1 = {}

d1.update(d)
print(d1)

d = {500: "Something"}

d1.update(d)
print(d1)
