# member aliasing

from addition import x as var1, add as sum, product as prod

print(var1)
print(sum(10, 20))  # 30
print(prod(10, 20))  # 200
