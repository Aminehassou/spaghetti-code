from math import *
def smallerThan(entries, maxDiff):
    for x in range(len(entries)-1):
        if abs(entries[x] - entries[x+1]) > maxDiff:
            return False
    return True
            

counter = 0
mesures = []
nMesures = int(input())
maxDiff = float(input())
for x in range(nMesures):
    mesures.append(float(input()))
while not smallerThan(mesures, maxDiff):
    counter += 1
    mesures_next = [mesures[0]]

    for x in range(1, len(mesures)-1):  

        mesures_next.append((mesures[x+1] + mesures[x-1]) / 2) 
        
    mesures_next.append(mesures[-1])
    mesures = mesures_next
print(counter)
