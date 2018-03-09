count = 0
pos = int(input())
nVillages = int(input())
for x in range(nVillages):
    posVillage = int(input())
    distance = pos - posVillage
    if distance < 0:
        distance = -distance
    if distance <= 50:
        count += 1
print(count)
