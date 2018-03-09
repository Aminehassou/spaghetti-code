nbEmplacements = int(input())
emplacements = [0] * nbEmplacements
results = [0] * nbEmplacements
for x in range(nbEmplacements):
    n = int(input())
    emplacements[x] = n
    results[n] = x
for x in results:
    print(x)








