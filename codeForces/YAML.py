n = int(input())
used = []
fileLines = []
for x in range(n):
    fileLine = input().split(".")
    fileLines.append(fileLine)
fileLines.sort()
for bigIndex in range(len(fileLines)):
    innerList = fileLines[bigIndex]
    for smallIndex in range(len(innerList)):
        if innerList[smallIndex] != innerList[-1]:
            if innerList[smallIndex] not in used:
                print("{}:".format(innerList[smallIndex]))
                print("  "*(smallIndex + 1), end = "" )
                used.append(innerList[smallIndex])
        else:
            print("{}".format(innerList[smallIndex]))

      