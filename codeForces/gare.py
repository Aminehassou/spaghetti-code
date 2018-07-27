#n = station numbers
#d = constant
#k = number of station changes
t = int(input())
for x in range(t):
    n, d, k = map(int, input().split())
    if d == 1:
        print(0, 0, 0, 0, 0)

