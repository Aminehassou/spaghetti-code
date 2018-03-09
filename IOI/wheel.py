from math import *
nbZones = int(input())
spins = nbZones // 24
if spins > 0:
    zone = nbZones - (spins * 24)
elif spins < 0:
     zone = nbZones + (-spins * 24)
else:
    zone = nbZones
print(zone)
