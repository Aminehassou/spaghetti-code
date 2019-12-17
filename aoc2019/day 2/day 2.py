# --- Day 2: 1202 Program Alarm --- #
inputFile = open("input.txt", "r")

intList = inputFile.read().split(",")
intList[-1] = intList[-1].strip()
intList = list(map(int, intList))
intList[1] = 12
intList[2] = 2
print(intList)
for i in range(0, len(intList), 4):
    if intList[i] == 1:
        add = intList[intList[i + 1]] + intList[intList[i + 2]]
        intList[intList[i + 3]] = add
    elif intList[i] == 2:
        multiply = intList[intList[i + 1]] * intList[intList[i + 2]]
        intList[intList[i + 3]] = multiply
    else: # intList[i] == 99
        break
print(intList)
