square = []
sums = []
for x in range(4):
    temp = list(map(int, input().split(" ")))
    square.append(temp)
for row in range(len(square)):
    rowSum = 0
    colSum = 0
    for x in range(len(square)):
        colSum += square[x][row]

    for col in range(len(square)):
        rowSum += square[row][col]
    sums.append(rowSum)
    sums.append(colSum)
isMagic = True
for loop in sums:
    if sums[0] != loop:
        print("not magic")
        isMagic = False
        break
if isMagic:
    print("magic")
