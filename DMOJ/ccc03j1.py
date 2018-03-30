from math import *
tineHeight = int(input())
tineSpacing = int(input())
handleLength = int(input())
lastLine = (tineSpacing*2)+3
for y in range(tineHeight):
    for x in range(3):
        print("*", end=" "*tineSpacing)
    print("\n", end="")

print("*"*(lastLine))
for z in range(handleLength):
    print(" "*(floor(lastLine/2)), end = "")
    print("*")