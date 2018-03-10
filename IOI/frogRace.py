def getWinnerIndex(distances):
    counter = 0
    currentWinDistance = max(distances)
    for y in distances:
        if currentWinDistance == y:
            counter += 1
    if counter > 1:
        return -1
    for x in range(len(distances)):
        if currentWinDistance == distances[x]:
            return x
    return -1

nFrogs = int(input())
nTurns = int(input())
distances = [0] * nFrogs
scores = [0] * nFrogs
for x in range(nTurns):
    frogNumber, distanceGone = map(int, input().split(" "))
    winnerIndex = getWinnerIndex(distances)
    if winnerIndex != -1:
        scores[winnerIndex] += 1
    distances[frogNumber-1] += distanceGone
winnerScore = max(scores)


for y in range(len(scores)):
    if winnerScore == scores[y]:
        print(y+1)
        break

