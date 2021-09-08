# get the most used application name from given data set

dataSet = ["whatsapp", "whatsapp", "whatsapp", "whatsapp", "whatsapp", "whatsapp", "instagram", "instagram",
           "instagram", "instagram",
           "facebook", "facebook", "facebook"]

# way 1

appUsageFrequency = {}

appUsageFrequency["whatsapp"] = dataSet.count("whatsapp")
appUsageFrequency["instagram"] = dataSet.count("instagram")
appUsageFrequency["facebook"] = dataSet.count("facebook")
print(appUsageFrequency)

maxValue = 0
appName = ""

for k, v in appUsageFrequency.items():
    if v >= maxValue:
        maxValue = v
        appName = k

print(f"The most used app is {appName}")

# way 2

appUsageFrequency = {}

for x in dataSet:
    appUsageFrequency[x] = (appUsageFrequency.get(x, 0)) + 1

print(appUsageFrequency)
for k, v in appUsageFrequency.items():
    print(f"{k} has occurred {v} times")
