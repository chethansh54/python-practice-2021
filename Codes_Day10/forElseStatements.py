cart = [10, 20, 30, 40, 600]
for item in cart:
    if item >= 500:
        print("Cant process this order")
        break
    print(item, " ordered")
else:
    print("All items processed Successfully")



