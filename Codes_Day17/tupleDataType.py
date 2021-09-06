myTuple = (1, 2, 3, 4, 5)

print(f"myTuple={myTuple} | type={type(myTuple)}")

t = 10
print(f"myTuple={t} | type={type(t)}")

t = (10)
print(f"myTuple={t} | type={type(t)}")

t = 100,
print(f"myTuple={t} | type={type(t)}")

t = 10, 20, 30
print(f"myTuple={t} | type={type(t)}")

t = (10,)
print(f"myTuple={t} | type={type(t)}")

t = tuple([10, 2, 0, 30, 40, 78])
print(f"myTuple={t} | type={type(t)}")

t = sorted(t)
print(f"myTuple={t} | type={type(t)}")

t = sorted(t, reverse=True)
print(f"myTuple={t} | type={type(t)}")

# resolution
t = tuple(sorted(t))
print(f"myTuple={t} | type={type(t)}")

t = tuple(sorted(t, reverse=True))
print(f"myTuple={t} | type={type(t)}")


t2 = t+t+t
print(f"myTuple={t2} | type={type(t2)}")

t2 = t*4
print(f"myTuple={t2} | type={type(t2)}")


print(f"myTuple Size={len(t2)}")

print(f"occurrence of 78 in t2 = {t2.count(78)}")

print(f"Index of 1st occurence of 40 in t2 = {t2.index(40)}")

print(f"Minimum element of t2 is {min(t2)} | Max element of t2 is {max(t2)}")

