question = int(input())
n = int(input())
dmoj = list(map(int, input().split()))
peg = list(map(int, input().split()))
add = 0
if question == 1:
    minDmoj = sorted(dmoj)
    minPeg = sorted(peg)
    for x in range(len(minDmoj)):
        add += max(minDmoj[x], minPeg[x])
    print(add)
else:
    maxDmoj = sorted(dmoj, reverse = True)
    maxPeg = sorted(peg)
    for x in range(len(maxDmoj)):
        add += max(maxDmoj[x], maxPeg[x])
    print(add)
