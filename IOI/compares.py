line1 = input()
line2 = input()
minLen = len(line2)

if len(line1) < len(line2):
    minLen = len(line1)
    
counter = 0
stop = 0
for x in range(minLen):
   if stop == 0:
        if line1[x] < line2[x]:
            print(1)
            stop+=1
        elif line2[x] < line1[x]:
            print(2)
            stop+=1
        else:
            counter +=1

if stop == 0:
   if line1 == line2:
      print("=")
   elif len(line2) > len(line1):
       print(2)
   elif len(line1) > len(line2):
       print(1)
print(counter)