n = int(input())
people = 0
maxPeople = 0
for x in range(n*2):
    person = int(input())
    if person > 0:
        people += 1
    else:
        people -= 1
    if maxPeople < people:
        maxPeople = people
print(maxPeople)