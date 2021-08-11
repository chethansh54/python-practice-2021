numBytes = [1, 2, 67, 89]
numBytes = bytes(numBytes)
print(type(numBytes))
print(numBytes)

#access bytes

byte1 = numBytes[-1]
print(byte1)

numBytes = [1, 2, 67, 89]
numBytes = bytearray(numBytes)
print(type(numBytes))
print(numBytes)

#access bytearray

byte1 = numBytes[-1]
print(byte1)
numBytes[-1] = 90
byte1 = numBytes[-1]
print(byte1)


