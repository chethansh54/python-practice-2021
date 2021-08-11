carName = "Toyota"
modelName = 'INNOVA'

variantName = """Innova 
Cresta"""

mySlogan = "I love 'python' "

otherSlogan = """I love "python" """

print(type(carName))

print(carName)
print(modelName)
print(variantName)
print(mySlogan)
print(otherSlogan)


#slicing

productName = "Skybags 1L 780Rs"

#default step size = 1
#default end index = n-1
#default start index = 0

brandName = productName[0:8:1]
print(brandName)

brandName = productName[0:8:]
print(brandName)

brandName = productName[::]
print(brandName)

brandName = productName[::-1]
print(brandName)

vehicleNumber = "JH01MR9876"
stateName = vehicleNumber[0:2]
districtName = vehicleNumber[2:4]
print(stateName)
print(districtName)
