results = []
for x in range(6):
    results.append(input())
winCount = results.count("W")
if winCount >= 5:
    print(1)
elif winCount == 3 or winCount == 4:
    print(2)
elif winCount == 1 or winCount == 2:
    print(3)
else:
    print(-1)
