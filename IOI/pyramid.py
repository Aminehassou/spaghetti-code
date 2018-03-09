maxRocks = int(input())
hauteur = 0
neededRocks = 0
a = 0
while neededRocks < maxRocks:
    a += 1
    hauteur += 1
    neededRocks += (a*a)    
if neededRocks > maxRocks:
    neededRocks -= (a*a)
    hauteur -= 1
if hauteur < 0:
    hauteur = 0
print(hauteur)
print(neededRocks)