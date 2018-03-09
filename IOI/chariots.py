nbCharrettes = int(input())
total = 0
weights = [0] * nbCharrettes
for x in range(nbCharrettes):
    weight = float(input())
    weights[x] = weight
for y in weights:
    total += y
average = total / nbCharrettes
for z in weights:
    print(average - z)


    
