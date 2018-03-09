nbSuspects = int(input())
for x in range(nbSuspects):
    count = 0
    height = int(input())
    age = int(input())
    weight = int(input())
    horse = int(input())
    brownHair = int(input())
    tHeight = (height >= 178 and height <= 182)
    tAge = (age >= 34)
    tWeight = (weight < 70)
    tHorse = (horse == 0)
    tBrownHair = (brownHair == 1)
    if tHeight:
        count+=1
    if tAge:
        count+=1
    if tWeight:
        count +=1
    if tHorse:
        count +=1
    if tBrownHair:
        count +=1
    if count == 5:
        print("Très probable")
    elif count == 3 or count == 4:
        print("Probable")
    elif count == 0:
        print("Impossible")
    else:
        print("Peu probable")

