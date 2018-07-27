n, m = map(int, input().split())
count = 0
missingStreets = []
connected = []
for x in range(m):
    u, v = map(int, input().split())
    connected.append(u)
    connected.append(v)

for y in range(1, n+1):
    if y not in connected and y != 1:
        missingStreets.append(y)
        count+=1
print(count)
for x in range(len(missingStreets)):
    if len(missingStreets) > 1:
        if missingStreets[x] != missingStreets[-1]:
            print(missingStreets[x+1], missingStreets[x])
    else:
        print("1", missingStreets[x])
        
            
        

    