nMesure = int(input())
tempMin = int(input())
tempMax = int(input())
temp = int(input())
n = 1
while temp <= tempMax and temp >= tempMin and n < nMesure:
    print ("Rien à signaler")
    if nMesure > 1:
       temp = int(input())
    n += 1
print("Alerte !!")