s = {10, 30, 4, 0, 90}
print(s)  # {10,30,4,0,90}

s = set()
print(s)

data = [10, 30, 4, 5, 60, 60]

s = set(data)
print(s)

s = set(range(1, 100))
print(s)

# set function

s = {10, 20, 30}
print(s)

s.add(60)
print(s)

listData = [10, 30, 4, 5, 60, 60]
s = {10, 20}
print(s)
s.update(listData)
print(s)
s.update(listData, range(1, 8))
print(s)
s.update(listData, range(1, 8), range(50, 70))
print(s)

s1 = {10, 20, 30, 40}
s2 = s1
print(f"s1={s1}  s2={s2} | s1 id = {id(s1)} s2 id = {id(s2)}")
s2 = s1.copy()
print(f"s1={s1}  s2={s2} | s1 id = {id(s1)} s2 id = {id(s2)}")

# removals

s1 = {10, 20, 30, 40}
print(f"{s1.pop()} was removed from set ")
print(s1)

s1.remove(30)
print(s1)

# s1.remove(80)
# print(s1)

s1.discard(80)
print(s1)

# mathematical ops

# UNION
s1 = {10, 30}
s2 = {20, 40}

s3 = s1.union(s2)  # {10,30,20,40}

print(s3)

# INTERSECTION

s1 = {10, 30, 40, 50}
s2 = {20, 40, 50}

s3 = s1.intersection(s2)  # {40}

print(s3)

# difference()

s1 = {10, 30, 40}
s2 = {20, 40}

s3 = s1.difference(s2)  # {10,30} s1-s2
print(s3)
s3 = s2.difference(s1)  # {20} s2-s1
print(s3)

# Symmetric difference


s1 = {10, 30, 40}
s2 = {20, 40}

s3 = s1.symmetric_difference(s2)  # {10,30,20}
print(s3)

s3 = s2.symmetric_difference(s1)  # {10,30,20}
print(s3)

# Membership operators

s = "PythonProgramming p"

strSet = set(s)
print(strSet)
print('P' in strSet)  # True
print('d' in strSet)  # False
print('d' not in strSet)  # True

# set comprehension

s = {x * x for x in range(1, 5)}
print(s)  # {1,4,9,16}

s = {2 ** x for x in range(2, 10, 2)}
print(s)  # {4,16,64,256}
