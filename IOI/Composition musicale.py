entree = list(input())
nbNotes = len(entree)
nbDoublons = -1
while nbDoublons != 0:
   nbDoublons = 0
   iIn = 0
   iOut = 0
   while iIn < nbNotes :
      if (iIn < nbNotes - 1) and (entree[iIn] == entree[iIn+1]):
         iIn = iIn + 2
         nbDoublons = nbDoublons + 1
      else:
         entree[iOut] = entree[iIn]
         iIn = iIn + 1
         iOut = iOut + 1
      print("iIn = {} iOut = {}".format(iIn, iOut))
   nbNotes = nbNotes - 2 * nbDoublons
pos = 0
for loop in range(nbNotes):
   print(entree[pos], end = '')
   pos = pos + 1