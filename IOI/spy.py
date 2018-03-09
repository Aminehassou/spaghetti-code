startDate = int(input())
endDate = int(input())
nbEntered = int(input())
people = 0
for x in range(nbEntered):
    enterDate = int(input())
    if enterDate >= startDate and enterDate <= endDate:
        people += 1
print(people)
