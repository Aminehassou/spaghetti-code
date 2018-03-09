xMin = int(input())
xMax = int(input())
yMin = int(input())
yMax = int(input())
totalHouses = int(input())
insideHouses = 0
for x in range(totalHouses):
    xHouse = int(input())
    yHouse = int(input())
    if xHouse <= xMax and xHouse >= xMin and yHouse <= yMax and yHouse >= yMin:
        insideHouses += 1
print(insideHouses)



