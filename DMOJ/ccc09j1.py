finalSum = 0
stringSum = "9 7 8 0 9 2 1 4 1 8"
for x in range(3):
    stringSum = stringSum + " " + input()
stringList = stringSum.split(" ")
for x in range(len(stringList)):
    if x % 2 == 0:
        finalSum += (int(stringList[x]) * 1)
    else:
        finalSum += (int(stringList[x]) * 3)
print("The 1-3-sum is", finalSum)
