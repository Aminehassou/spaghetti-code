n, k = map(int, input().split())
studentProps = []
used1 = []
used2 = []
for x in range(2*n):
    properties = list(map(int, input().split()))
    studentProps.append(properties)
add1 = 0
add2 = 0
for x in studentProps:
    if x[0] not in used1 and len(used1) <= len(used2):
        used1.append(x[0])
        add1 += x[2]
    elif x[1] not in used2 and len(used2) <= len(used1):
        used2.append(x[1])
        add2 += x[2]
if abs(add1 - add2) <= k and len(used1) == len(used2):
    print("YES")
else:
    print("NO")