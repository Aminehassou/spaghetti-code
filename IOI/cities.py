nCities = 0
nPlace = int(input())
for x in range(nPlace):
    nPeople = int(input())
    if nPeople > 10000:
        nCities += 1
print(nCities)
