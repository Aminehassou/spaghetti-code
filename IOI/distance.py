maxDistance = 0
nDays = int(input())
for x in range (nDays):
    dailyDistance = int(input())
    if dailyDistance > maxDistance:
        maxDistance = dailyDistance
print(maxDistance)
