'''
input number of houses
input x
is x > var
var = x

'''
nHouses = int(input())
xMax = 0
xMin = 1000000
yMax = 0
yMin = 1000000
for x in range(nHouses):
    coord = int(input())
    if coord > xMax:
        xMax = coord
    if coord < xMin:
        xMin = coord
    coord =  int(input())
    if coord > yMax:
        yMax = coord
    if coord < yMin:
        yMin = coord
perimetre = ((xMax - xMin) + (yMax - yMin)) * 2
print (perimetre)