readings = [int(input()) for x in range(4)]
bigger = 0
smaller = 0
equal = 0
for x in range(1, len(readings)):
    if readings[x] > readings[x-1]:
        bigger = 1
    if readings[x] < readings[x-1]:
        smaller = 1
    if readings[x] == readings[x-1]:
        equal = 1
if bigger == 1 and smaller == 0 and equal == 0:
    print("Fish Rising")
elif smaller == 1 and bigger == 0 and equal == 0:
    print("Fish Diving")
elif equal == 1 and bigger == 0 and smaller == 0:
    print("Fish At Constant Depth")
else:
    print("No Fish")
