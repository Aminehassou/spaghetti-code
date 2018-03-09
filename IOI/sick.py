nPeople = int(input())
nSick = 1
day = 1
while nPeople != nSick:
   nSick += nSick * 2
   if nSick > nPeople:
       nSick = nPeople
   day +=1
print (day)