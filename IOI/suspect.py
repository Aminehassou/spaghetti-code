startDate = int(input())
endDate = int(input())
nbInvites = int(input())
suspectCount = 0
for x in range(nbInvites):
    begin = int(input())
    end = int(input())
    notSuspect = ((begin < startDate and end < startDate) or (begin > endDate and end > endDate))
    if not notSuspect:
        suspectCount+=1
print(suspectCount)


