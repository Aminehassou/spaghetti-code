n = int(input())
cases = 0   
for y in range(5, 0, -1):
    for x in range(0, 6):
        if x + y == n and x <= y:
            cases +=1
print(cases)