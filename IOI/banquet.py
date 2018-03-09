nPositions = int(input())
changes = int(input())
positions = [0] * nPositions
for x in range(nPositions):
    pNumber = int(input())
    positions[x] = pNumber
for x in range(changes):
    pos1 = int(input())
    pos2 = int(input())
    temp = positions[pos1]
    positions[pos1] = positions[pos2]
    positions[pos2] = temp
for x in positions:
    print(x)
