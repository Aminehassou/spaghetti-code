nMv = int(input())
reverseMvs = [0, 2, 1, 3, 5, 4]
movements = [0] * nMv
for x in range(nMv):
    move = int(input())
    movements[x] = move
for x in range(nMv-1, -1, -1):
    print(reverseMvs[movements[x]])
